# 🛠️ Technology Stack

> **Purpose:** What tools and libraries are approved for building Services.

**Golden Rule: If it's not on this list, ask your Coordinator before using it.**

---

## ✅ Approved Technologies

### Core Framework
| Component | Version | Why We Use It |
|-----------|---------|---------------|
| **Python** | 3.11+ | Modern, fast, great async support |
| **FastAPI** | 0.104+ | High performance, auto docs, native async |

**❌ NOT Allowed:**
- Django (too heavy for microservices)
- Flask (no native async support)

---

### Data Validation & Config
| Library | Version | Use Case |
|---------|---------|----------|
| **Pydantic** | 2.0+ | Request/response validation, data models |
| **pydantic-settings** | 2.0+ | Environment variable management |

**Example:**
```python
from pydantic import BaseModel

class TaskRequest(BaseModel):
    action: str
    data: dict
```

---

### Testing
| Tool | Version | Use Case |
|------|---------|----------|
| **pytest** | Latest | Test runner |
| **httpx** | Latest | Async HTTP client for testing |

**❌ DON'T use `requests`** - It's blocking (not async-compatible)

**Example Test:**
```python
import httpx
import pytest

@pytest.mark.asyncio
async def test_api():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/health")
        assert response.status_code == 200
```

---

### Database (If Your Service Needs One)
| Type | Technology | ORM Options |
|------|-----------|-------------|
| **Relational** | PostgreSQL | SQLAlchemy (async mode) or Tortoise ORM |
| **Cache** | Redis | aioredis |

**Important:** Always use async database drivers!

---

### Deployment
| Stage | Tool | Why |
|-------|------|-----|
| **Containerization** | Docker | Consistent environments |
| **Orchestration** | Kubernetes or Docker Swarm | For production |

---

### Code Quality Tools
| Tool | Purpose |
|------|---------|
| **Ruff** or **Flake8** | Linting (catch code issues) |
| **Black** | Auto-formatting (consistent style) |
| **mypy** | Optional: Static type checking |

**Quick Setup:**
```bash
pip install ruff black pytest
ruff check .
black .
pytest
```

---

## 📦 Standard Dependencies

Every Service should have these in `requirements.txt`:

```txt
fastapi>=0.104.0
uvicorn>=0.23.0
pydantic>=2.0.0
pydantic-settings>=2.0.0
httpx>=0.25.0
pytest>=7.4.0
python-multipart
```

**Add more as needed for your specific Service** (e.g., `pillow` for images, `pandas` for data).

---

## ❓ What If I Need Something Not Listed?

1. **Check if there's an approved alternative** (e.g., use `httpx` instead of `requests`)
2. **Ask your Coordinator** with justification
3. **Document why you need it** in your handoff notes

---

## 🚫 Explicitly Banned

- ❌ `requests` library (use `httpx` instead)
- ❌ Django or Flask (use FastAPI)
- ❌ Synchronous database drivers (use async versions)
- ❌ Unmaintained libraries (check last update date)

