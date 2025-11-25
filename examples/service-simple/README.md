# 💡 Simple Service Example

> **Purpose:** A minimal UDC-compliant Service in ~20 lines. Great for learning!

---

## What This Shows

This example demonstrates the **absolute minimum** to be UDC-compliant:
- ✅ All 5 required endpoints (`/health`, `/capabilities`, `/state`, `/dependencies`, `/message`)
- ✅ Returns correct JSON format
- ✅ Can be tested and run

**For production Services, use `../templates/python-fastapi` instead** (includes proper structure, config, tests).

---

## Run It

```bash
# Install dependencies
pip install -r requirements.txt

# Start the service
uvicorn src.main:app --reload
```

Visit: http://localhost:8000/docs to see the auto-generated API docs.

---

## Test It

```bash
# Health check
curl http://localhost:8000/health

# Capabilities
curl http://localhost:8000/capabilities

# Send a message
curl -X POST http://localhost:8000/message \
  -H "Content-Type: application/json" \
  -d '{"type":"test", "payload":{}, "trace_id":"example-123"}'
```

---

## The Code (Explained)

```python
from fastapi import FastAPI

app = FastAPI()

# 1. Health: "Are you alive?"
@app.get("/health")
async def health():
    return {"status": "active", "service": "simple-service"}

# 2. Capabilities: "What can you do?"
@app.get("/capabilities")
async def capabilities():
    return {"features": [], "udc_version": "1.0"}

# 3. State: "How are you doing?"
@app.get("/state")
async def state():
    return {"status": "active"}

# 4. Dependencies: "What do you need?" (none in this case)
@app.get("/dependencies")
async def dependencies():
    return {"required": [], "optional": []}

# 5. Message: "Here's work for you"
@app.post("/message")
async def message(msg: dict):
    # In production, you'd process the message here
    return {"received": True, "trace_id": msg.get("trace_id")}
```

**That's it!** This is the minimum to participate in the Full Potential AI network.

---

## What's Missing (For Production)?

This example is intentionally simple. For real Services, you need:
- ✅ Proper configuration management (`config.py`)
- ✅ Environment variables (`.env`)
- ✅ Input validation (Pydantic models)
- ✅ Error handling
- ✅ JWT authentication
- ✅ Comprehensive tests
- ✅ Logging
- ✅ Dockerfile

**👉 Use `templates/python-fastapi` for production work!**

---

## Learn More

- **Full Template:** `../templates/python-fastapi/`
- **UDC Spec:** `../docs/UDC_COMPLIANCE.md`
- **Standards:** `../docs/SERVICE_STANDARDS.md`

