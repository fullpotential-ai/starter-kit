# 🚀 Full Potential Service Template (FastAPI)

> **This is your starting point.** Copy this entire folder to create a new Service.

---

## 📋 Quick Start (5 Minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
# Copy the example file
cp env.example .env

# Edit .env and fill in YOUR values (get from Coordinator)
nano .env  # or use your editor
```

### 3. Run the Service
```bash
uvicorn src.main:app --reload
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### 4. Test It Works
```bash
# In another terminal
curl http://localhost:8000/health
```

Expected response:
```json
{"status": "active", "service": "template-service", "uptime": 5, "timestamp": "..."}
```

✅ **If you see JSON, you're ready to build!**

---

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_udc.py -v
```

---

## 📂 What's Inside

```
template/
├── src/
│   ├── main.py          # 👈 START HERE - UDC endpoints & app entry
│   ├── config.py        # Environment variable management
│   └── udc/             # UDC protocol implementations
│       ├── health.py
│       ├── capabilities.py
│       ├── state.py
│       └── message.py
│
├── tests/
│   ├── __init__.py
│   └── test_udc.py      # Pre-written UDC compliance tests
│
├── Dockerfile           # Ready to deploy
├── requirements.txt     # Python dependencies
├── env.example          # Environment variable template
└── README.md            # You are here
```

---

## ✏️ Customizing for Your Service

### Step 1: Update Service Info
Edit `src/main.py`:
```python
SERVICE_INFO = {
    "id": 0,                    # Coordinator will assign this
    "name": "my-awesome-service",  # 👈 Change this
    "version": "1.0.0",
    "status": "active"
}
```

### Step 2: Update Capabilities
Edit the `/capabilities` endpoint in `src/main.py`:
```python
@app.get("/capabilities")
async def capabilities():
    return {
        "service": "my-awesome-service",
        "version": "1.0.0",
        "features": ["feature-1", "feature-2"],  # 👈 Add your features
        "dependencies": ["other-service"],       # 👈 Add dependencies
        "udc_version": "1.0"
    }
```

### Step 3: Implement Your Logic
Add your business logic in `src/main.py` or create new modules:

```python
# Add new endpoint for your custom logic
@app.post("/process")
async def process_data(data: dict):
    # Your custom logic here
    return {"result": "success"}
```

### Step 4: Handle Messages
Update the `/message` endpoint to handle your specific tasks:
```python
@app.post("/message")
async def receive_message(message: dict):
    payload = message.get("payload", {})
    action = payload.get("action")
    
    if action == "analyze":
        result = analyze_something(payload)
    elif action == "process":
        result = process_something(payload)
    else:
        raise HTTPException(status_code=400, detail="Unknown action")
    
    return {
        "received": True,
        "trace_id": message.get("trace_id"),
        "result": result
    }
```

---

## 🐳 Docker Deployment

### Build the Image
```bash
docker build -t my-service:1.0.0 .
```

### Run the Container
```bash
docker run -p 8000:8000 \
  -e SERVICE_ID=42 \
  -e SERVICE_NAME=my-service \
  -e REGISTRY_URL=https://registry.example.com \
  -e JWT_SECRET=your-secret-here \
  my-service:1.0.0
```

### Test the Container
```bash
curl http://localhost:8000/health
```

---

## 🔧 Development Tips

### Auto-reload During Development
```bash
# --reload watches for file changes
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### View Auto-Generated API Docs
FastAPI automatically creates interactive docs:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

### Debug Mode
```python
# In src/main.py, add debug logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 📚 Next Steps

1. **Read the Docs:** Check `../../docs/` for standards and requirements
2. **Implement Logic:** Add your Service's specific functionality
3. **Write Tests:** Add tests for your custom logic in `tests/`
4. **Fill Out Mission:** Use `../../MISSION_TEMPLATE.md` to document your work
5. **Submit:** Use `../../HANDOFF_TEMPLATE.md` when ready

---

## 🆘 Troubleshooting

### "Module not found" error
```bash
# Make sure you installed dependencies
pip install -r requirements.txt
```

### Port 8000 already in use
```bash
# Use a different port
uvicorn src.main:app --port 8001

# Or kill the process using 8000
lsof -ti:8000 | xargs kill -9
```

### Tests failing
```bash
# Make sure service is NOT running when testing
# Tests start their own test server
```

---

## 📝 Environment Variables Reference

| Variable | Required | Example | Description |
|----------|----------|---------|-------------|
| `SERVICE_NAME` | Yes | `my-service` | Your service's name |
| `SERVICE_ID` | Yes | `42` | Assigned by Coordinator |
| `REGISTRY_URL` | Yes | `https://registry...` | Registry endpoint |
| `JWT_SECRET` | Yes | `your-secret` | For auth |
| `LOG_LEVEL` | No | `INFO` | Logging level |

