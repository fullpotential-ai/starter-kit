# 📏 Service Standards

> **Purpose:** How to write clean, maintainable Python code for Services.

---

## Python Coding Standards

We follow industry best practices to keep code readable and bug-free.

### Core Rules
- ✅ **Style Guide:** Follow PEP 8 (Python's official style guide)
- ✅ **Type Hints:** Required for all function arguments and return values
- ✅ **Async/Await:** Use `async def` for I/O operations (database, API calls)
- ✅ **Docstrings:** Document all public functions and classes

### Why These Matter
- **Type hints** catch bugs before runtime
- **Async/await** prevents blocking (keeps your Service fast)
- **Docstrings** help the next person (or future you) understand your code

### Naming Conventions

| What | Style | Example | Why |
|------|-------|---------|-----|
| Functions/Variables | `snake_case` | `calculate_total`, `user_id` | Python standard |
| Classes | `PascalCase` | `UserProfile`, `DataProcessor` | Easy to spot classes |
| Constants | `UPPER_CASE` | `MAX_RETRIES`, `DEFAULT_TIMEOUT` | Shows it's a constant |
| Private methods | `_leading_underscore` | `_internal_helper` | Signals "don't call me directly" |

**Good Examples:**
```python
MAX_UPLOAD_SIZE = 10_000_000  # Constant

class ImageProcessor:  # Class in PascalCase
    def process_image(self, image_path: str) -> dict:  # Function in snake_case
        return {"status": "processed"}
```

---

## 📂 File Structure

**Always follow this structure:**

```
my-service/
├── src/
│   ├── main.py          # Entry point & UDC endpoints (start here)
│   ├── config.py        # Environment variables & settings
│   ├── udc/             # UDC protocol implementation
│   │   ├── __init__.py
│   │   ├── health.py
│   │   └── ...
│   └── business/        # Your custom logic goes here
│       ├── __init__.py
│       └── processor.py
├── tests/
│   ├── test_udc.py      # UDC compliance tests (pre-written)
│   └── test_business.py # Your custom logic tests
├── Dockerfile
├── requirements.txt
├── env.example
└── README.md
```

**Why this structure?**
- Keeps UDC protocol separate from your business logic
- Easy to find what you're looking for
- Consistent across all Services

---

## 🧪 Testing Requirements

### Coverage Target
**>80% code coverage** - Use `pytest --cov` to check

### Testing Framework
**pytest** is the standard. Already configured in the template.

### Types of Tests

| Test Type | What It Tests | Example |
|-----------|---------------|---------|
| **Unit Tests** | Individual functions | `test_calculate_score()` |
| **Integration Tests** | API endpoints + database | `test_message_endpoint()` |
| **UDC Compliance** | All 5 required endpoints | `test_health()` (pre-written) |

### Example Test Structure
```python
# tests/test_business.py
def test_process_image():
    """Test image processing logic"""
    result = process_image("test.jpg")
    assert result["status"] == "success"
    assert "data" in result
```

---

## 📖 Documentation Requirements

### Docstrings (Required)
All public functions need docstrings explaining what they do:

```python
def analyze_sentiment(text: str) -> dict:
    """
    Analyze sentiment of input text.
    
    Args:
        text: The text to analyze
        
    Returns:
        dict with keys: sentiment (str), confidence (float)
    """
    # implementation
```

### README (Required)
Your service-specific README must include:
1. What this Service does (one sentence)
2. How to run it (copy env.example, install deps, run)
3. How to test it (pytest command)
4. What endpoints it has (beyond the standard UDC ones)

---

## 🚨 Error Handling

### Use FastAPI Exceptions
```python
from fastapi import HTTPException

@app.get("/data/{item_id}")
async def get_data(item_id: int):
    if not item_exists(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return get_item(item_id)
```

### Log Errors (Don't Expose Them)
```python
import logging

logger = logging.getLogger(__name__)

try:
    result = risky_operation()
except Exception as e:
    logger.error(f"Failed to process: {e}", exc_info=True)
    raise HTTPException(status_code=500, detail="Processing failed")
```

**❌ DON'T:** Return raw error messages like "Database connection string is invalid"
**✅ DO:** Return generic messages like "Internal error occurred"

---

## 🚫 Anti-Patterns (Don't Do These!)

### ❌ Global Mutable State
```python
# BAD - Don't do this
counter = 0

@app.post("/increment")
async def increment():
    global counter
    counter += 1  # This breaks in multi-process environments
```

### ❌ Hardcoded Values
```python
# BAD
DATABASE_URL = "postgresql://user:pass@localhost/db"

# GOOD
from config import settings
DATABASE_URL = settings.database_url  # From environment
```

### ❌ Blocking Code in Async Functions
```python
# BAD
async def fetch_data():
    time.sleep(5)  # This blocks the entire event loop!
    
# GOOD
async def fetch_data():
    await asyncio.sleep(5)  # This doesn't block
```

### ❌ No Type Hints
```python
# BAD
def calculate(x, y):
    return x + y

# GOOD
def calculate(x: int, y: int) -> int:
    return x + y
```

---

## ✅ Quick Standards Checklist

Before submitting:
- [ ] All functions have type hints
- [ ] All public functions have docstrings
- [ ] No hardcoded secrets or URLs
- [ ] No `time.sleep()` in async code
- [ ] Naming follows conventions (snake_case, PascalCase)
- [ ] Tests cover >80% of code
- [ ] No mutable global variables

