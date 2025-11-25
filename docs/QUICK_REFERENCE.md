# ⚡ Quick Reference Cheat Sheet

> **For experienced developers:** All the key info on one page.

---

## UDC Endpoints (Required)

```python
@app.get("/health")
async def health():
    return {"status": "active", "service": "name", "uptime": 123, "timestamp": "..."}

@app.get("/capabilities")
async def capabilities():
    return {"service": "name", "version": "1.0.0", "features": [], "dependencies": [], "udc_version": "1.0"}

@app.get("/state")
async def state():
    return {"uptime_seconds": 123, "status": "active"}

@app.get("/dependencies")
async def dependencies():
    return {"required": [], "optional": []}

@app.post("/message")
async def receive_message(message: dict):
    return {"received": True, "trace_id": message.get("trace_id")}
```

---

## Quick Start Commands

```bash
# Copy template
cp -r templates/python-fastapi ../my-service
cd ../my-service

# Setup
cp env.example .env
pip install -r requirements.txt

# Run
uvicorn src.main:app --reload

# Test
pytest -v
curl http://localhost:8000/health

# Docker
docker build -t my-service .
docker run -p 8000:8000 my-service
```

---

## Environment Variables

```bash
# .env (NEVER commit this!)
SERVICE_NAME=my-service
SERVICE_ID=42
REGISTRY_URL=[PROVIDED BY COORDINATOR]
JWT_SECRET=[PROVIDED BY COORDINATOR]
LOG_LEVEL=INFO
```

---

## Pydantic Validation

```python
from pydantic import BaseModel

class TaskRequest(BaseModel):
    action: str
    data: dict

@app.post("/task")
async def process_task(request: TaskRequest):
    return {"status": "ok"}
```

---

## Calling Another Service

```python
import httpx
import jwt
from config import settings

async def call_service(service_name: str, payload: dict):
    # 1. Discover service
    async with httpx.AsyncClient() as client:
        reg_resp = await client.get(f"{settings.registry_url}/services/{service_name}")
        url = reg_resp.json()["url"]
    
    # 2. Create JWT
    token = jwt.encode({"service_id": settings.service_id}, settings.jwt_secret, algorithm="HS256")
    
    # 3. Call service
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{url}/message",
            json=payload,
            headers={"Authorization": f"Bearer {token}"}
        )
    
    return response.json()
```

---

## JWT Authentication

```python
from fastapi import Header, HTTPException
import jwt
from config import settings

def verify_jwt(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(401, "No token")
    
    try:
        token = authorization.replace("Bearer ", "")
        return jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
    except jwt.InvalidTokenError:
        raise HTTPException(401, "Invalid token")

@app.post("/protected")
async def protected(auth: dict = Depends(verify_jwt)):
    return {"message": "authenticated"}
```

---

## Logging

```python
import logging

logger = logging.getLogger(__name__)

@app.post("/message")
async def receive_message(message: dict):
    trace_id = message.get("trace_id")
    logger.info(f"[{trace_id}] Processing message")
    # ...
```

---

## Error Handling

```python
from fastapi import HTTPException

@app.get("/data/{item_id}")
async def get_data(item_id: int):
    if not exists(item_id):
        raise HTTPException(404, "Not found")
    return get_item(item_id)
```

---

## Testing

```python
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert "status" in response.json()
```

---

## Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## requirements.txt

```txt
fastapi>=0.104.0
uvicorn>=0.23.0
pydantic>=2.0.0
pydantic-settings>=2.0.0
httpx>=0.25.0
pytest>=7.4.0
python-multipart
PyJWT>=2.8.0
```

---

## File Structure

```
my-service/
├── src/
│   ├── main.py          # Endpoints
│   ├── config.py        # Settings
│   └── business/        # Your logic
├── tests/
│   └── test_*.py
├── Dockerfile
├── requirements.txt
├── .env                 # Local only (gitignored)
├── env.example          # Template (commit this)
└── README.md
```

---

## Naming Conventions

| Type | Convention | Example |
|------|-----------|---------|
| Functions | `snake_case` | `process_data()` |
| Classes | `PascalCase` | `DataProcessor` |
| Constants | `UPPER_CASE` | `MAX_SIZE` |
| Private | `_leading` | `_internal()` |

---

## Security Checklist

- [ ] No secrets in code
- [ ] All secrets in environment variables
- [ ] `.env` in `.gitignore`
- [ ] JWT validation on protected endpoints
- [ ] Pydantic models for input validation
- [ ] No SQL string concatenation (use ORM)
- [ ] Rate limiting on public endpoints
- [ ] HTTPS in production

---

## Compliance Checklist

- [ ] All 5 UDC endpoints implemented
- [ ] Endpoints return correct JSON schema
- [ ] `pytest` passes
- [ ] Docker builds successfully
- [ ] `curl http://localhost:8000/health` returns 200
- [ ] No hardcoded IPs or URLs
- [ ] Code coverage >80%
- [ ] README updated with service-specific info

---

## Common Commands

```bash
# Development
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# Testing
pytest                           # Run all tests
pytest -v                        # Verbose
pytest --cov=src                 # With coverage
pytest tests/test_udc.py -v      # Specific file

# Docker
docker build -t my-service:1.0 .
docker run -p 8000:8000 --env-file .env my-service:1.0
docker logs <container-id>

# Debugging
curl http://localhost:8000/docs  # Swagger UI
curl http://localhost:8000/health -v  # Verbose
```

---

## Status Codes

| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | Successful request |
| 400 | Bad Request | Invalid input |
| 401 | Unauthorized | Missing/invalid token |
| 404 | Not Found | Resource doesn't exist |
| 422 | Unprocessable | Pydantic validation failed |
| 500 | Server Error | Internal error |

---

## Message Format

```json
{
  "type": "command",
  "payload": {
    "action": "process",
    "data": {...}
  },
  "trace_id": "uuid-v4"
}
```

---

## Useful Links

- FastAPI Docs: https://fastapi.tiangolo.com
- Pydantic Docs: https://docs.pydantic.dev
- pytest Docs: https://docs.pytest.org
- httpx Docs: https://www.python-httpx.org

