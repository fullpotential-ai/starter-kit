# 🏗️ Lesson 3: Build Your Service

> **Time:** 30 minutes - 2 hours (depending on complexity)  
> **Goal:** Customize the template and implement your assigned functionality

---

## What You'll Do

By the end of this lesson, you'll have:
- ✅ Customized the Service configuration
- ✅ Added your business logic
- ✅ Implemented your assigned mission
- ✅ Maintained UDC compliance

---

## 📋 Before You Start

Make sure you have:
- [ ] Your mission assignment from your Coordinator
- [ ] The template set up from Lesson 2
- [ ] Your development server running
- [ ] A clear understanding of what your Service should do

**If you don't have a mission yet:** Follow along with a simple example (we'll build a "Hello World" processor).

---

## 🎯 Understanding the Template Structure

Open `src/main.py` in your editor. You'll see it's organized into sections:

```python
# ============================================================================
# SERVICE CONFIGURATION - CUSTOMIZE THIS
# ============================================================================
SERVICE_INFO = {...}

# ============================================================================
# UDC ENDPOINTS - REQUIRED (Do not remove these!)
# ============================================================================
@app.get("/health")
...

# ============================================================================
# CUSTOM ENDPOINTS - ADD YOUR BUSINESS LOGIC BELOW
# ============================================================================
# Your code goes here!
```

**Golden Rule:** Keep the UDC endpoints as-is. Add your logic in the custom section.

---

## Step 1: Customize Service Information (5 minutes)

### Edit `SERVICE_INFO` in `src/main.py`

```python
SERVICE_INFO = {
    "id": 0,                           # Will be assigned by Coordinator
    "name": "hello-world-service",     # ← CHANGE THIS
    "version": "1.0.0",                # Your version
    "status": "active"                 # Keep as "active"
}
```

**Name your service:**
- Use lowercase with hyphens
- Be descriptive but concise
- Examples: `pdf-processor`, `image-analyzer`, `notification-sender`

### Update the FastAPI app info

```python
app = FastAPI(
    title="Hello World Service",       # ← CHANGE THIS
    version="1.0.0",
    description="Processes greetings"  # ← CHANGE THIS
}
```

**Save and check:** Visit http://localhost:8000/docs - your new name should appear!

---

## Step 2: Declare Your Capabilities (5 minutes)

### Edit the `/capabilities` endpoint

```python
@app.get("/capabilities")
async def capabilities():
    return {
        "service": SERVICE_INFO["name"],
        "version": SERVICE_INFO["version"],
        "features": [                     # ← ADD YOUR FEATURES
            "greeting-generation",
            "name-validation"
        ],
        "dependencies": [],               # ← ADD DEPENDENCIES
        "udc_version": "1.0"
    }
```

**Features:** What can your Service do?  
**Dependencies:** What other Services or systems do you need?

**Example for an OCR Service:**
```python
"features": ["text-extraction", "pdf-support", "multi-language"],
"dependencies": ["storage-service"]
```

---

## Step 3: Define Dependencies (2 minutes)

### Edit the `/dependencies` endpoint

```python
@app.get("/dependencies")
async def dependencies():
    return {
        "required": ["postgresql"],      # ← Must have these
        "optional": ["redis-cache"]      # ← Nice to have these
    }
```

**Required:** Your Service won't work without these  
**Optional:** Your Service can work but prefers these

**Example:**
```python
"required": [],      # No dependencies (simple service)
"optional": []
```

---

## Step 4: Implement Message Handling (Core Logic)

This is where your Service's main functionality goes!

### Understanding the Message Format

Messages coming to your Service look like this:

```json
{
  "type": "command",
  "payload": {
    "action": "specific_action",
    "data": {...}
  },
  "trace_id": "unique-id-for-tracking"
}
```

### Basic Implementation Pattern

```python
@app.post("/message")
async def receive_message(message: dict):
    """
    Main entry point for work requests from other Services.
    """
    trace_id = message.get("trace_id", "unknown")
    payload = message.get("payload", {})
    action = payload.get("action")
    
    logger.info(f"[{trace_id}] Received action: {action}")
    
    # Route to appropriate handler
    try:
        if action == "greet":
            result = handle_greet(payload)
        elif action == "validate":
            result = handle_validate(payload)
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Unknown action: {action}"
            )
        
        return {
            "received": True,
            "trace_id": trace_id,
            "result": result
        }
    
    except Exception as e:
        logger.error(f"[{trace_id}] Error: {e}")
        raise HTTPException(status_code=500, detail="Processing failed")
```

---

## Step 5: Add Your Business Logic Functions

**Add your functions BELOW the UDC endpoints:**

```python
# ============================================================================
# BUSINESS LOGIC - Your custom functions
# ============================================================================

def handle_greet(payload: dict) -> dict:
    """
    Generate a personalized greeting.
    
    Args:
        payload: Must contain 'name' field
        
    Returns:
        dict with 'greeting' field
    """
    name = payload.get("name", "Friend")
    greeting = f"Hello, {name}! Welcome to Full Potential AI."
    
    return {
        "greeting": greeting,
        "processed_at": datetime.utcnow().isoformat()
    }


def handle_validate(payload: dict) -> dict:
    """
    Validate a name meets requirements.
    
    Args:
        payload: Must contain 'name' field
        
    Returns:
        dict with 'valid' boolean and 'reason' if invalid
    """
    name = payload.get("name", "")
    
    if len(name) < 2:
        return {"valid": False, "reason": "Name too short"}
    
    if not name.replace(" ", "").isalpha():
        return {"valid": False, "reason": "Name must be alphabetic"}
    
    return {"valid": True}
```

---

## Step 6: Use Pydantic for Validation (Best Practice)

**Instead of plain dicts, use Pydantic models for type safety:**

Add at the top of `src/main.py`:

```python
from pydantic import BaseModel, validator

class GreetRequest(BaseModel):
    action: str
    name: str
    
    @validator('name')
    def name_must_be_valid(cls, v):
        if len(v) < 2:
            raise ValueError('Name must be at least 2 characters')
        return v

class Message(BaseModel):
    type: str = "command"
    payload: dict
    trace_id: str
```

**Then use it in your endpoint:**

```python
@app.post("/message")
async def receive_message(message: Message):  # ← Now validated!
    trace_id = message.trace_id
    payload = message.payload
    # ... rest of your code
```

**Why?** Pydantic automatically validates incoming data and returns helpful errors.

---

## Step 7: Add Custom Endpoints (Optional)

You can add endpoints beyond the 5 required ones:

```python
# ============================================================================
# CUSTOM ENDPOINTS
# ============================================================================

@app.post("/greet")
async def greet_endpoint(name: str):
    """
    Quick greeting endpoint (alternative to /message).
    """
    return {"greeting": f"Hello, {name}!"}


@app.get("/stats")
async def stats():
    """
    Service statistics.
    """
    return {
        "total_requests": 0,  # Track this with a counter
        "uptime": int(time.time() - START_TIME)
    }
```

---

## Step 8: Add Logging (Important for Debugging)

Add at the top of your file:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
```

**Use throughout your code:**

```python
logger.info(f"[{trace_id}] Processing greeting request")
logger.error(f"[{trace_id}] Failed to process: {error}")
logger.debug(f"[{trace_id}] Payload: {payload}")
```

---

## 🧪 Testing Your Changes

### Manual Testing

```bash
# Test with curl
curl -X POST http://localhost:8000/message \
  -H "Content-Type: application/json" \
  -d '{
    "type": "command",
    "payload": {"action": "greet", "name": "Alice"},
    "trace_id": "test-123"
  }'

# Expected response:
# {
#   "received": true,
#   "trace_id": "test-123",
#   "result": {
#     "greeting": "Hello, Alice! Welcome to Full Potential AI.",
#     "processed_at": "2023-10-27T10:00:00"
#   }
# }
```

### Interactive Testing

Visit http://localhost:8000/docs and use the "Try it out" button!

### Automated Testing

Create `tests/test_business.py`:

```python
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_greet_message():
    response = client.post("/message", json={
        "type": "command",
        "payload": {"action": "greet", "name": "Bob"},
        "trace_id": "test-1"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["received"] is True
    assert "Hello, Bob" in data["result"]["greeting"]

def test_invalid_action():
    response = client.post("/message", json={
        "type": "command",
        "payload": {"action": "unknown"},
        "trace_id": "test-2"
    })
    assert response.status_code == 400
```

**Run tests:**
```bash
pytest tests/ -v
```

---

## 📋 Real-World Examples

### Example 1: PDF Processor Service

```python
from PyPDF2 import PdfReader
import io

@app.post("/message")
async def receive_message(message: dict):
    trace_id = message.get("trace_id")
    payload = message.get("payload", {})
    action = payload.get("action")
    
    if action == "extract_text":
        pdf_url = payload.get("pdf_url")
        # Download PDF from storage service
        # Extract text
        # Return results
        return {
            "received": True,
            "trace_id": trace_id,
            "result": {"text": extracted_text, "pages": page_count}
        }
```

### Example 2: Image Analysis Service

```python
from PIL import Image
import requests

@app.post("/message")
async def receive_message(message: dict):
    trace_id = message.get("trace_id")
    payload = message.get("payload", {})
    action = payload.get("action")
    
    if action == "analyze":
        image_url = payload.get("image_url")
        # Fetch image
        # Run ML model
        # Return analysis
        return {
            "received": True,
            "trace_id": trace_id,
            "result": {"objects": detected_objects, "confidence": scores}
        }
```

### Example 3: Notification Service

```python
import smtplib

@app.post("/message")
async def receive_message(message: dict):
    trace_id = message.get("trace_id")
    payload = message.get("payload", {})
    action = payload.get("action")
    
    if action == "send_email":
        recipient = payload.get("email")
        subject = payload.get("subject")
        body = payload.get("body")
        # Send email
        return {
            "received": True,
            "trace_id": trace_id,
            "result": {"sent": True, "message_id": msg_id}
        }
```

---

## ✅ Build Checklist

Before moving to testing, verify:

- [ ] `SERVICE_INFO` updated with your service name
- [ ] `/capabilities` lists your features and dependencies
- [ ] `/dependencies` lists what you need
- [ ] `/message` endpoint handles your specific actions
- [ ] Business logic functions implemented
- [ ] Pydantic models for validation (recommended)
- [ ] Logging added for debugging
- [ ] Code follows naming conventions (snake_case, etc.)
- [ ] No secrets hardcoded (use environment variables)
- [ ] Service still runs without errors

---

## 🐛 Common Mistakes to Avoid

### ❌ Don't Break UDC Endpoints
```python
# BAD - Removing required endpoint
# @app.get("/health")  ← Don't comment these out!
```

### ❌ Don't Hardcode Secrets
```python
# BAD
API_KEY = "sk-1234567890"

# GOOD
from src.config import settings
API_KEY = settings.api_key  # From environment
```

### ❌ Don't Use Blocking Code
```python
# BAD - Blocks the entire server
import time
time.sleep(10)

# GOOD - Async sleep
import asyncio
await asyncio.sleep(10)
```

### ❌ Don't Accept Unvalidated Input
```python
# BAD
@app.post("/message")
async def receive_message(message: dict):  # No validation!
    name = message["data"]["name"]  # Could crash!

# GOOD
from pydantic import BaseModel

class Message(BaseModel):
    type: str
    payload: dict
    trace_id: str

@app.post("/message")
async def receive_message(message: Message):  # Validated!
    # Now safe to access
```

---

## 🎓 What's Next?

You've built your Service! Now it's time to test it thoroughly.

**Next Lesson:** `04_TESTING.md`  
You'll learn how to test your Service to ensure it's production-ready.

---

## 💡 Pro Tips

### Tip 1: Start Simple
Get the basic functionality working first. Add complexity later.

### Tip 2: Test as You Go
Don't wait until the end. Test each function as you write it.

### Tip 3: Use the Interactive Docs
http://localhost:8000/docs is your friend for quick testing.

### Tip 4: Keep trace_id Everywhere
Always pass `trace_id` through your functions for debugging.

### Tip 5: Read the Error Messages
Python's error messages are helpful! Read them carefully.

---

**Happy coding!** When you're ready, move to: `04_TESTING.md`

