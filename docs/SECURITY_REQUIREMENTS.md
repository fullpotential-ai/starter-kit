# 🔒 Security Requirements

> **Purpose:** How to keep Services secure. These are NON-NEGOTIABLE rules.

**⚠️ Security violations can compromise the entire network. Take this seriously.**

---

## 1. Secret Management 🔑

### The Golden Rules
1. **NEVER hardcode secrets in source code**
2. **ALWAYS use environment variables**
3. **ALWAYS add `.env` to `.gitignore`**

### ❌ BAD (Don't Do This)
```python
# DANGER: Secret in code!
DATABASE_URL = "postgresql://admin:MyPassword123@10.0.0.5/db"
API_KEY = "sk-1234567890abcdef"
```

### ✅ GOOD (Do This)
```python
# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    api_key: str
    
    class Config:
        env_file = ".env"

settings = Settings()
```

```bash
# .env (NEVER commit this file!)
DATABASE_URL=postgresql://admin:MyPassword123@10.0.0.5/db
API_KEY=sk-1234567890abcdef
```

### Checklist
- [ ] No passwords/keys in source code
- [ ] `.env` in `.gitignore`
- [ ] `env.example` provided with placeholders only

---

## 2. Authentication & Authorization 🛡️

### JWT Validation (Required)
All inter-Service communication uses JWT tokens.

```python
from fastapi import Header, HTTPException

async def verify_token(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="No token provided")
    
    token = authorization.replace("Bearer ", "")
    # Verify JWT signature here
    return token

@app.post("/protected")
async def protected_endpoint(token: str = Depends(verify_token)):
    return {"message": "You're authenticated!"}
```

### Least Privilege Principle
**Your Service should only access what it needs.**

- If you only need read access, don't request write access
- If you only need one database table, don't connect to the whole database

---

## 3. Input Validation 🚪

### Trust No One
**ALL incoming data is potentially malicious until validated.**

### ✅ Always Use Pydantic Models
```python
from pydantic import BaseModel, validator

class TaskRequest(BaseModel):
    action: str
    image_id: int
    
    @validator('action')
    def validate_action(cls, v):
        allowed = ['analyze', 'process', 'store']
        if v not in allowed:
            raise ValueError(f'action must be one of {allowed}')
        return v

@app.post("/message")
async def receive_message(request: TaskRequest):
    # request is automatically validated
    return {"status": "ok"}
```

### ❌ DON'T Accept Raw Dictionaries
```python
# BAD - No validation
@app.post("/message")
async def receive_message(data: dict):
    action = data["action"]  # Could be anything!
```

---

## 4. Database Security 💾

### Prevent SQL Injection

### ❌ NEVER Do String Concatenation
```python
# DANGER: SQL Injection vulnerability!
user_id = request.user_id
query = f"SELECT * FROM users WHERE id = {user_id}"
```

### ✅ Use ORMs or Parameterized Queries
```python
# SAFE: Using SQLAlchemy ORM
from sqlalchemy import select

result = await session.execute(
    select(User).where(User.id == user_id)
)
```

### Database User Permissions
- Use separate database users for different Services
- Grant only necessary permissions (e.g., SELECT only if read-only)

---

## 5. Network Security 🌐

### HTTPS Only in Production
- All external traffic **must** be encrypted via TLS
- Docker internal network can use HTTP (it's isolated)

### Rate Limiting
Prevent abuse by limiting requests per client.

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/message")
@limiter.limit("10/minute")
async def receive_message(request: Request):
    return {"status": "ok"}
```

### Port Exposure
- **Only expose port 8000** (or your configured port)
- Don't expose database ports, debug ports, etc.

```dockerfile
# Dockerfile
EXPOSE 8000  # Only this port
```

---

## 🔍 Security Checklist (Pre-Submission)

### Secrets & Config
- [ ] No secrets in code (search for "password", "key", "token", "secret")
- [ ] All secrets loaded from environment variables
- [ ] `.env` in `.gitignore`
- [ ] `env.example` has placeholders only (no real values)
- [ ] Checked git history: `git log -p | grep -i "secret"` → Nothing sensitive

### Authentication
- [ ] JWT validation implemented on protected endpoints
- [ ] Unauthorized requests return 401

### Input Validation
- [ ] All endpoints use Pydantic models (not raw `dict`)
- [ ] Validators in place for critical fields
- [ ] File uploads size-limited

### Database
- [ ] Using ORM or parameterized queries (no string concatenation)
- [ ] Database user has minimal required permissions

### Network
- [ ] Only necessary port exposed in Dockerfile
- [ ] Rate limiting implemented (if public-facing)

---

## 🚨 If You Accidentally Commit a Secret

**ACT IMMEDIATELY:**

1. **Rotate the secret** (change the password/key)
2. **Remove from git history:**
   ```bash
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch .env" \
     --prune-empty --tag-name-filter cat -- --all
   ```
3. **Notify your Coordinator**
4. **Add to `.gitignore`** to prevent future accidents

---

## 📚 Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [FastAPI Security Docs](https://fastapi.tiangolo.com/tutorial/security/)
- Pydantic [Validation Docs](https://docs.pydantic.dev/latest/concepts/validators/)

