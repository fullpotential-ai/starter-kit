# ✅ Lesson 4: Testing Your Service

> **Time:** 15 minutes  
> **Goal:** Verify your Service works correctly and meets UDC compliance

---

## What You'll Do

By the end of this lesson, you'll have:
- ✅ Run automated tests
- ✅ Manually tested all endpoints
- ✅ Verified UDC compliance
- ✅ Confidence your Service is ready for deployment

---

## Why Testing Matters

```
No Tests → Deploy → Crash in Production → Emergency Fix → Chaos
                                                              ❌

Tests Pass → Deploy → Works Correctly → Happy Users → Success
                                                           ✅
```

**Testing catches bugs before they reach production.**

---

## 🧪 Three Types of Testing

### 1. Automated Tests (pytest)
Run `pytest` to test everything automatically.

### 2. Manual Endpoint Testing (curl)
Test individual endpoints by hand.

### 3. Interactive Testing (Swagger UI)
Use the browser-based API docs.

**You should do ALL THREE before submitting!**

---

## Step 1: Run Automated Tests (5 minutes)

### Basic Test Run

```bash
# Make sure your server is NOT running
# (Tests start their own test server)
pkill -f uvicorn

# Run all tests
pytest

# Expected output:
# tests/test_udc.py::test_health PASSED
# tests/test_udc.py::test_capabilities PASSED
# tests/test_udc.py::test_state PASSED
# tests/test_udc.py::test_message PASSED
# ======================== 4 passed in 0.50s ========================
```

### Verbose Output

```bash
# See detailed output
pytest -v

# See print statements (for debugging)
pytest -s
```

### Test Coverage

```bash
# See how much of your code is tested
pytest --cov=src --cov-report=html

# Open coverage report in browser
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

**Target: >80% coverage**

---

## Step 2: Add Tests for Your Custom Logic (10 minutes)

Create `tests/test_business.py`:

```python
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_your_specific_action():
    """
    Test your Service's main functionality.
    """
    response = client.post("/message", json={
        "type": "command",
        "payload": {
            "action": "your_action",
            "data": "test_data"
        },
        "trace_id": "test-123"
    })
    
    # Check status code
    assert response.status_code == 200
    
    # Check response structure
    data = response.json()
    assert data["received"] is True
    assert data["trace_id"] == "test-123"
    assert "result" in data
    
    # Check result content
    result = data["result"]
    assert "expected_field" in result


def test_invalid_input():
    """
    Test error handling with bad input.
    """
    response = client.post("/message", json={
        "type": "command",
        "payload": {
            "action": "unknown_action"
        },
        "trace_id": "test-456"
    })
    
    # Should return 400 for unknown action
    assert response.status_code == 400


def test_missing_required_field():
    """
    Test validation catches missing fields.
    """
    response = client.post("/message", json={
        "type": "command",
        "payload": {},  # Missing required data
        "trace_id": "test-789"
    })
    
    # Check it fails appropriately
    assert response.status_code in [400, 422]
```

**Run your new tests:**
```bash
pytest tests/test_business.py -v
```

---

## Step 3: Manual Endpoint Testing (10 minutes)

### Test All 5 UDC Endpoints

Start your server:
```bash
uvicorn src.main:app --reload
```

**In a new terminal:**

#### 1. Test /health

```bash
curl http://localhost:8000/health

# Expected response:
# {
#   "status": "active",
#   "service": "your-service-name",
#   "uptime": 123,
#   "timestamp": "2023-10-27T10:00:00Z"
# }
```

✅ Check:
- Returns 200 status
- Has all required fields
- `status` is "active"
- `timestamp` is in ISO 8601 format

---

#### 2. Test /capabilities

```bash
curl http://localhost:8000/capabilities

# Expected response:
# {
#   "service": "your-service-name",
#   "version": "1.0.0",
#   "features": ["feature1", "feature2"],
#   "dependencies": ["dep1"],
#   "udc_version": "1.0"
# }
```

✅ Check:
- Lists your actual features
- Lists your actual dependencies
- Version matches your SERVICE_INFO

---

#### 3. Test /state

```bash
curl http://localhost:8000/state

# Expected response:
# {
#   "uptime_seconds": 123,
#   "status": "active"
# }
```

✅ Check:
- Returns current uptime
- Status reflects actual state

---

#### 4. Test /dependencies

```bash
curl http://localhost:8000/dependencies

# Expected response:
# {
#   "required": ["postgresql"],
#   "optional": ["redis"]
# }
```

✅ Check:
- Lists what you actually need
- Distinguishes required vs optional

---

#### 5. Test /message

```bash
curl -X POST http://localhost:8000/message \
  -H "Content-Type: application/json" \
  -d '{
    "type": "command",
    "payload": {
      "action": "your_action",
      "data": "test"
    },
    "trace_id": "manual-test-1"
  }'

# Expected response:
# {
#   "received": true,
#   "trace_id": "manual-test-1",
#   "result": {...}
# }
```

✅ Check:
- Returns 200 for valid actions
- Returns 400 for unknown actions
- `trace_id` is echoed back
- Result contains expected data

---

### Test Error Cases

```bash
# Test with missing fields
curl -X POST http://localhost:8000/message \
  -H "Content-Type: application/json" \
  -d '{}'

# Should return 422 (validation error)

# Test with unknown action
curl -X POST http://localhost:8000/message \
  -H "Content-Type: application/json" \
  -d '{
    "type": "command",
    "payload": {"action": "unknown"},
    "trace_id": "error-test"
  }'

# Should return 400 (bad request)
```

---

## Step 4: Interactive Testing with Swagger UI (5 minutes)

Visit http://localhost:8000/docs

### Test Each Endpoint:

1. **Click on `/health`**
   - Click "Try it out"
   - Click "Execute"
   - Verify response

2. **Click on `/message`**
   - Click "Try it out"
   - Fill in example JSON:
     ```json
     {
       "type": "command",
       "payload": {
         "action": "your_action",
         "data": "test"
       },
       "trace_id": "swagger-test"
     }
     ```
   - Click "Execute"
   - Verify response

3. **Try invalid input**
   - Remove required fields
   - See validation errors

---

## Step 5: UDC Compliance Verification (5 minutes)

### Checklist

Run through this checklist manually:

#### /health Endpoint
- [ ] Returns JSON
- [ ] Has "status" field (string: "active" or "degraded")
- [ ] Has "service" field (string: your service name)
- [ ] Has "uptime" field (integer: seconds)
- [ ] Has "timestamp" field (string: ISO 8601 with Z suffix)
- [ ] Returns within 1 second

#### /capabilities Endpoint
- [ ] Returns JSON
- [ ] Has "service" field (string)
- [ ] Has "version" field (string)
- [ ] Has "features" field (array of strings)
- [ ] Has "dependencies" field (array of strings)
- [ ] Has "udc_version" field (string: "1.0")

#### /state Endpoint
- [ ] Returns JSON
- [ ] Has "uptime_seconds" field (integer)
- [ ] Has "status" field (string)

#### /dependencies Endpoint
- [ ] Returns JSON
- [ ] Has "required" field (array of strings)
- [ ] Has "optional" field (array of strings)

#### /message Endpoint
- [ ] Accepts POST requests
- [ ] Accepts JSON payload
- [ ] Returns "received" field (boolean: true)
- [ ] Returns "trace_id" field (echoed from request)
- [ ] Handles unknown actions gracefully (400 error)
- [ ] Validates input structure (422 for invalid)

---

## Step 6: Load Testing (Optional)

Test how your Service handles multiple requests:

```bash
# Install apache bench (if not installed)
# macOS: brew install httpd
# Ubuntu: sudo apt-get install apache2-utils

# Test with 100 requests, 10 concurrent
ab -n 100 -c 10 http://localhost:8000/health

# Look for:
# - Requests per second
# - Time per request
# - Failed requests (should be 0)
```

**Goal:** No failures, reasonable response time

---

## 🐛 Troubleshooting Test Failures

### "ModuleNotFoundError"
```bash
# Make sure you're in the right directory
pwd

# Reinstall dependencies
pip install -r requirements.txt
```

### "Address already in use" during tests
```bash
# Kill existing uvicorn
pkill -f uvicorn

# Run tests again
pytest
```

### Tests pass but manual testing fails
```bash
# Make sure server is running
uvicorn src.main:app --reload

# Check logs for errors
```

### 422 Validation Errors
```bash
# Your input doesn't match expected format
# Check the Pydantic model definition
# Look at error message details
```

---

## ✅ Testing Checklist

Before moving to deployment, verify:

### Automated Tests
- [ ] `pytest` passes all tests
- [ ] Code coverage >80%
- [ ] No warnings or errors in output

### Manual Testing
- [ ] All 5 UDC endpoints return correct JSON
- [ ] Your custom logic works as expected
- [ ] Error cases handled gracefully
- [ ] Invalid input returns appropriate errors

### UDC Compliance
- [ ] All required fields present in responses
- [ ] Field types match specification
- [ ] Response times are reasonable (<1s for /health)

### Security
- [ ] No secrets in code
- [ ] Input validation working
- [ ] Error messages don't leak internal details

---

## 🎓 What's Next?

Your Service is tested and working! Time to package it for deployment.

**Next Lesson:** `05_DOCKER_DEPLOYMENT.md`  
You'll learn how to build a Docker container for your Service.

---

## 💡 Testing Best Practices

### 1. Test Early, Test Often
Don't wait until you're "done". Test as you build.

### 2. Write Tests for Bugs
When you find a bug, write a test that reproduces it, then fix it.

### 3. Test the Happy Path AND Error Cases
```python
# Good test suite covers:
test_valid_input()         # Happy path
test_invalid_input()       # Error case
test_missing_fields()      # Edge case
test_unexpected_values()   # Edge case
```

### 4. Use Meaningful Test Names
```python
# BAD
def test_1(): ...

# GOOD
def test_greeting_with_valid_name(): ...
```

### 5. Keep Tests Independent
Each test should work on its own, not depend on others.

---

**All tests green?** Move to: `05_DOCKER_DEPLOYMENT.md`

