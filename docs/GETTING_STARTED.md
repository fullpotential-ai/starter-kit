# 🎯 Getting Started Guide

> **For New Apprentices:** Start here if this is your first time building a Service.

---

## The Big Picture

```
┌─────────────────────────────────────────────────────────┐
│                  Full Potential AI Network              │
│                                                         │
│  ┌─────────┐     ┌─────────┐     ┌─────────┐          │
│  │Service  │────▶│ Service │────▶│ Service │          │
│  │   #1    │     │   #2    │     │   #3    │          │
│  │(Storage)│     │  (OCR)  │     │(Analysis)│          │
│  └─────────┘     └─────────┘     └─────────┘          │
│       ▲               ▲               ▲                 │
│       │               │               │                 │
│       └───────────────┴───────────────┘                 │
│                       │                                 │
│                  ┌────────┐                             │
│                  │Registry│ ← All Services register here│
│                  └────────┘                             │
└─────────────────────────────────────────────────────────┘
```

**You're building ONE Service** that joins this network.

---

## Step-by-Step: Your First Service

### 📖 Step 1: Understand UDC (5 minutes)

**Read:** `UDC_COMPLIANCE.md`

**Key Takeaway:** Every Service needs these 5 endpoints:

| Endpoint | Purpose | Example Response |
|----------|---------|------------------|
| `/health` | "Are you alive?" | `{"status": "active"}` |
| `/capabilities` | "What can you do?" | `{"features": ["ocr"]}` |
| `/state` | "How are you?" | `{"uptime_seconds": 123}` |
| `/dependencies` | "What do you need?" | `{"required": ["db"]}` |
| `/message` | "Do this work" | `{"received": true}` |

---

### 💡 Step 2: See a Working Example (3 minutes)

```bash
cd examples/service-simple
pip install -r requirements.txt
uvicorn src.main:app --reload
```

Visit http://localhost:8000/docs

**Try the endpoints:**
```bash
curl http://localhost:8000/health
curl http://localhost:8000/capabilities
```

**Key Takeaway:** This 20-line file is a complete UDC-compliant Service!

---

### 🔧 Step 3: Build Your Service (30 minutes)

#### 3.1 Copy the Template
```bash
# From starter-kit root
cp -r templates/python-fastapi ../my-first-service
cd ../my-first-service
```

#### 3.2 Set Up Environment
```bash
# Copy environment template
cp env.example .env

# Install dependencies
pip install -r requirements.txt
```

#### 3.3 Customize Service Info
Edit `src/main.py`:
```python
SERVICE_INFO = {
    "id": 0,
    "name": "my-first-service",  # 👈 Change this
    "version": "1.0.0",
    "status": "active"
}
```

#### 3.4 Add Your Features
Still in `src/main.py`, update capabilities:
```python
@app.get("/capabilities")
async def capabilities():
    return {
        "service": "my-first-service",
        "version": "1.0.0",
        "features": ["example-feature"],  # 👈 Add your features
        "dependencies": [],
        "udc_version": "1.0"
    }
```

#### 3.5 Implement Business Logic
Add your logic to the `/message` endpoint:
```python
@app.post("/message")
async def receive_message(message: dict):
    payload = message.get("payload", {})
    
    # 👇 YOUR LOGIC GOES HERE
    if payload.get("action") == "greet":
        result = {"greeting": "Hello, World!"}
    else:
        result = {"error": "Unknown action"}
    
    return {
        "received": True,
        "trace_id": message.get("trace_id"),
        "result": result
    }
```

#### 3.6 Test Your Service
```bash
# Start the service
uvicorn src.main:app --reload

# In another terminal, test it
curl http://localhost:8000/health

curl -X POST http://localhost:8000/message \
  -H "Content-Type: application/json" \
  -d '{"payload": {"action": "greet"}, "trace_id": "test-1"}'
```

Expected:
```json
{
  "received": true,
  "trace_id": "test-1",
  "result": {"greeting": "Hello, World!"}
}
```

---

### ✅ Step 4: Verify Compliance (2 minutes)

Run the test suite:
```bash
pytest -v
```

All tests should pass:
```
tests/test_udc.py::test_health PASSED
tests/test_udc.py::test_capabilities PASSED
tests/test_udc.py::test_state PASSED
tests/test_udc.py::test_message PASSED
```

**🎉 Congratulations! You've built a UDC-compliant Service!**

---

## What's Next?

### For Simple Services
If your Service is straightforward:
1. Add more logic to `/message` endpoint
2. Write tests for your custom logic
3. Fill out `HANDOFF_TEMPLATE.md`
4. Submit to your Coordinator

### For Complex Services
If you need more structure:
1. Create separate modules in `src/` for different concerns
2. Add Pydantic models for validation
3. Implement JWT authentication
4. Add proper logging and error handling

**Read these docs next:**
- `SERVICE_STANDARDS.md` - Code quality guidelines
- `SERVICE_INTEGRATION.md` - How to call other Services
- `SECURITY_REQUIREMENTS.md` - Keep your Service secure

---

## Common First-Time Questions

### "Do I need all 5 endpoints?"
**Yes.** All Services must be UDC-compliant. The template already has them - just customize the responses.

### "How do I call other Services?"
**Through the Registry.** See `SERVICE_INTEGRATION.md` for the Service Discovery pattern.

### "Can I use Django/Flask instead of FastAPI?"
**No.** FastAPI is the standard for async performance and auto-docs.

### "Where do I put my API keys?"
**Environment variables only!** Never in code. See `SECURITY_REQUIREMENTS.md`.

### "How do I test with the Registry?"
**You don't yet.** Build and test locally first. Your Coordinator will help with Registry integration when you're ready to deploy.

---

## Troubleshooting

### "Module not found" error
```bash
# You forgot to install dependencies
pip install -r requirements.txt
```

### "Port 8000 already in use"
```bash
# Kill the existing process
lsof -ti:8000 | xargs kill -9

# Or use a different port
uvicorn src.main:app --port 8001
```

### "Tests are failing"
```bash
# Make sure the service is NOT running
# pytest starts its own test server

# If still failing, check the error message
pytest -v
```

---

## Learning Path Summary

```
✅ Step 1: Read UDC_COMPLIANCE.md → Understand the protocol
✅ Step 2: Run examples/service-simple → See it working
✅ Step 3: Copy templates/python-fastapi → Build your own
✅ Step 4: Run pytest → Verify compliance

Next Steps:
→ Read SERVICE_STANDARDS.md for best practices
→ Read SERVICE_INTEGRATION.md for multi-service patterns
→ Read SECURITY_REQUIREMENTS.md for safety
→ Build your assigned Service!
```

---

## Need Help?

- **Template issues?** Check `templates/python-fastapi/README.md`
- **UDC questions?** Re-read `UDC_COMPLIANCE.md`
- **Code standards?** See `SERVICE_STANDARDS.md`
- **Still stuck?** Ask your Coordinator

**Good luck building your first Service! 🚀**

