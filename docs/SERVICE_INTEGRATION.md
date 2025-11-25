# 🔗 Service Integration Guide

> **Purpose:** How your Service talks to other Services and the Registry.

---

## 🔐 Getting Your Credentials

**Your Coordinator will provide these when you're ready to deploy:**

| What | Where It Goes | Example |
|------|---------------|---------|
| **Service ID** | `SERVICE_ID` env var | `42` |
| **Registry URL** | `REGISTRY_URL` env var | `[PROVIDED BY COORDINATOR]` |
| **JWT Secret** | `JWT_SECRET` env var | `[PROVIDED BY COORDINATOR]` |

**⚠️ NEVER hardcode these values!** Always use environment variables.

### Setup in Your Service
```python
# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    service_id: int
    registry_url: str
    jwt_secret: str
    
    class Config:
        env_file = ".env"

settings = Settings()
```

```bash
# .env (get real values from Coordinator)
SERVICE_ID=42
REGISTRY_URL=[PROVIDED BY COORDINATOR]
JWT_SECRET=[PROVIDED BY COORDINATOR]
```

---

## 🔄 How Services Communicate

### The Big Picture
```
Service A wants to talk to Service B:

1. Service A asks Registry: "Where is Service B?"
2. Registry responds: "Service B is at http://10.0.5.3:8000"
3. Service A sends request to Service B's /message endpoint
4. Service B processes and responds
```

**Key Point:** Services NEVER hardcode each other's IPs. They always discover through the Registry.

---

## 🔑 Authentication Flow

### When Your Service Starts
```
1. Your Service reads JWT_SECRET from environment
   ↓
2. Contacts Registry at REGISTRY_URL
   ↓
3. Sends authentication request with Service ID
   ↓
4. Registry validates and responds: "You're registered!"
   ↓
5. Your Service starts accepting requests
```

### When Calling Another Service
```python
import httpx
import jwt
from config import settings

async def call_other_service(service_name: str, payload: dict):
    # 1. Get target service address from Registry
    async with httpx.AsyncClient() as client:
        registry_response = await client.get(
            f"{settings.registry_url}/services/{service_name}"
        )
        target_url = registry_response.json()["url"]
    
    # 2. Create JWT token
    token = jwt.encode(
        {"service_id": settings.service_id},
        settings.jwt_secret,
        algorithm="HS256"
    )
    
    # 3. Call the target service
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{target_url}/message",
            json=payload,
            headers={"Authorization": f"Bearer {token}"}
        )
    
    return response.json()
```

### When Receiving Requests
```python
from fastapi import Header, HTTPException
import jwt
from config import settings

def verify_jwt(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="No token")
    
    try:
        token = authorization.replace("Bearer ", "")
        payload = jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
        return payload
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/message")
async def receive_message(message: dict, auth: dict = Depends(verify_jwt)):
    # Process message from authenticated service
    return {"received": True}
```

---

## 📡 Service Discovery (Finding Other Services)

### How to Find Another Service

**DON'T do this:**
```python
# BAD: Hardcoded IP
response = await client.get("http://10.0.5.3:8000/data")
```

**DO this:**
```python
# GOOD: Discover through Registry
async def get_service_url(service_name: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{settings.registry_url}/services/{service_name}"
        )
        return response.json()["url"]

# Then use it
storage_url = await get_service_url("storage-service")
response = await client.get(f"{storage_url}/data")
```

---

## 📨 Message Passing (Service-to-Service)

### Standard Message Format
All Service communication uses this format:

```json
{
  "type": "command",           // Type: command, query, event
  "payload": {                 // Your custom data
    "action": "analyze",
    "image_id": "12345"
  },
  "trace_id": "uuid-string"    // For tracking across services
}
```

### Complete Example: Calling Another Service

```python
import httpx
import uuid
from config import settings

async def request_image_analysis(image_id: str):
    # 1. Discover the analysis service
    async with httpx.AsyncClient() as client:
        registry_resp = await client.get(
            f"{settings.registry_url}/services/image-analysis"
        )
        analysis_url = registry_resp.json()["url"]
    
    # 2. Create message
    message = {
        "type": "command",
        "payload": {
            "action": "analyze",
            "image_id": image_id
        },
        "trace_id": str(uuid.uuid4())
    }
    
    # 3. Send authenticated request
    token = create_jwt_token()  # Your JWT creation function
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{analysis_url}/message",
            json=message,
            headers={"Authorization": f"Bearer {token}"}
        )
    
    return response.json()
```

### Complete Example: Receiving Messages

```python
from pydantic import BaseModel
from typing import Any, Dict

class Message(BaseModel):
    type: str
    payload: Dict[str, Any]
    trace_id: str

@app.post("/message")
async def receive_message(message: Message, auth: dict = Depends(verify_jwt)):
    # Log the trace_id for debugging
    logger.info(f"Received message {message.trace_id} from service {auth['service_id']}")
    
    # Route based on message type
    if message.type == "command":
        result = await process_command(message.payload)
    elif message.type == "query":
        result = await process_query(message.payload)
    else:
        raise HTTPException(status_code=400, detail="Unknown message type")
    
    return {
        "received": True,
        "trace_id": message.trace_id,
        "result": result
    }
```

---

## 🔍 Trace IDs (Debugging Across Services)

### What's a Trace ID?
A unique identifier that follows a request as it moves through multiple Services.

### Why They Matter
When debugging, you can trace a request's entire journey:
```
User Request (trace: abc-123)
  → Gateway Service (trace: abc-123)
    → Image Service (trace: abc-123)
      → Storage Service (trace: abc-123)
```

All logs with `abc-123` show the full story.

### How to Use Them
```python
import uuid
import logging

logger = logging.getLogger(__name__)

@app.post("/message")
async def receive_message(message: dict):
    trace_id = message.get("trace_id", str(uuid.uuid4()))
    
    # Log with trace_id
    logger.info(f"[{trace_id}] Processing message")
    
    # Pass trace_id to any downstream services
    result = await call_another_service({
        "type": "query",
        "payload": {"action": "fetch"},
        "trace_id": trace_id
    })
    
    return {"received": True, "trace_id": trace_id}
```

---

## 💓 Heartbeat (Staying Alive)

### What It Is
Every 30 seconds, your Service pings the Registry to say "I'm still alive."

### How to Implement
```python
import asyncio
import httpx
from config import settings

async def heartbeat_loop():
    """Send heartbeat every 30 seconds"""
    while True:
        try:
            async with httpx.AsyncClient() as client:
                await client.post(
                    f"{settings.registry_url}/heartbeat",
                    json={"service_id": settings.service_id}
                )
        except Exception as e:
            logger.error(f"Heartbeat failed: {e}")
        
        await asyncio.sleep(30)

@app.on_event("startup")
async def start_heartbeat():
    asyncio.create_task(heartbeat_loop())
```

---

## ✅ Integration Checklist

Before deploying:
- [ ] Service ID, Registry URL, JWT Secret loaded from environment
- [ ] JWT validation implemented on `/message` endpoint
- [ ] Service discovery used (not hardcoded IPs)
- [ ] All outgoing requests include trace_id
- [ ] Heartbeat running every 30 seconds
- [ ] Tested calling another service (or mock)

---

## 🆘 Troubleshooting

### "401 Unauthorized" when calling another Service
- Check JWT_SECRET matches what Registry expects
- Verify token is in `Authorization: Bearer <token>` header

### "Connection refused" when calling another Service
- Don't hardcode IPs - use Service Discovery
- Check the service is registered and healthy

### Can't register with Registry
- Verify REGISTRY_URL is correct
- Check SERVICE_ID was assigned by Coordinator
- Ensure network connectivity (Docker network, firewall)

