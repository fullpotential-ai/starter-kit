# Mission Specification: Service #[N] - [Service Name]

> **FOR ARCHITECTS:** Use this template to create detailed specs for apprentices.  
> **FOR APPRENTICES:** This document tells you exactly what to build and includes AI prompts to help you.

---

## 🎯 Objective
*One clear sentence describing what this Service does.*

**Example:** "Build a Service that automates apprentice onboarding via email validation and credential generation."

---

## 📋 Requirements

### Functional Requirements
What your Service must DO:
- [ ] Specific requirement 1 (define inputs/outputs)
- [ ] Specific requirement 2 (include constraints)
- [ ] Specific requirement 3 (specify formats)

**Example:**
- [ ] POST `/register` endpoint accepting: email, github_username, discord_id
- [ ] Validate email is not from disposable provider
- [ ] Generate credentials via Bitwarden API (7-day expiry)
- [ ] Send welcome email via Email Service
- [ ] Store registration in SQLite database
- [ ] Rate limit: 10 registrations/hour per IP

### UDC Requirements (Non-Negotiable)
**The template already implements these - keep them working:**
- [ ] `/health` endpoint (returns service status)
- [ ] `/capabilities` endpoint (lists features)
- [ ] `/state` endpoint (current load/status)
- [ ] `/dependencies` endpoint (what you need to run)
- [ ] `/message` endpoint (receives tasks from other Services)

---

## 🤖 Pre-Written AI Prompts

**Apprentice:** Copy these prompts into your chosen AI tool (Cursor, Gemini, Claude, or ChatGPT) exactly as written. They're designed to work with the starter-kit template.

**Tip:** If using Gemini Gems or Claude Projects, upload the starter-kit docs first for better context.

### Prompt 1: Initial Setup

```
Using the starter-kit Python FastAPI template at src/main.py, add:
- POST /register endpoint accepting: email (str), github_username (str), discord_id (str)
- Use Pydantic model for validation
- Email validation: reject disposable email providers (use disposable-email-domains list)
- SQLite database (via SQLAlchemy) to store: id, email, github_username, discord_id, created_at, credentials_sent
- Rate limiting: 10 registrations per hour per IP address (use slowapi)
- Return JSON: {"success": bool, "message": str, "registration_id": int}
```

### Prompt 2: Bitwarden Integration

```
Add Bitwarden Send integration to the /register endpoint:
1. Install bw CLI wrapper (subprocess calls)
2. After successful registration, generate credentials:
   - SERVICE_ID=[from spec]
   - JWT_PUBLIC_KEY=[generate random]
   - REGISTRY_URL=[from config]
3. Use bw send create to create a Send with 7-day expiry
4. Return the Send link in the response
5. Update database with credentials_sent=True
6. Handle bw CLI errors gracefully
```

### Prompt 3: Email Notification

```
Add email notification via SMTP after credential generation:
1. Use EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASS from .env
2. Send welcome email with:
   - Subject: "Welcome to Full Potential AI"
   - Body: Credentials link, Discord invite, starter-kit repo link
3. Use Jinja2 template for email body (create templates/welcome_email.html)
4. Log email sent status to database
5. Handle SMTP errors without failing the registration
```

### Prompt 4: Testing

```
Create comprehensive tests in tests/test_register.py:
1. test_valid_registration() - Happy path
2. test_disposable_email_rejected() - Should return 400
3. test_rate_limiting() - 11th request in hour should fail
4. test_invalid_email_format() - Should return 422
5. test_duplicate_registration() - Should handle gracefully
6. Mock Bitwarden and SMTP calls
Use pytest fixtures for database setup/teardown
```

---

## 🏗️ Architecture

### Data Flow
```
1. POST /register → Validate input (Pydantic)
2. Check rate limit (slowapi)
3. Check email not disposable
4. Check not duplicate registration
5. Save to SQLite database
6. Generate credentials (Bitwarden Send)
7. Send welcome email (SMTP)
8. Return success + credentials link
```

### External Dependencies
- **Bitwarden CLI** - For credential generation
- **SMTP Server** - For email sending
- **Email Service** (optional) - Could delegate to Service #X

### Database Schema
```sql
CREATE TABLE registrations (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    github_username TEXT NOT NULL,
    discord_id TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    credentials_sent BOOLEAN DEFAULT FALSE,
    send_link TEXT
);
```

---

## 📦 Deliverables

When you're done, you must provide:
- [ ] Source code in YOUR public GitHub repo (e.g., `github.com/yourname/service-16-onboarding`)
- [ ] All tests passing: `pytest tests/ -v`
- [ ] >80% code coverage: `pytest --cov=src`
- [ ] `README.md` updated with service-specific instructions
- [ ] `HANDOFF.md` completed (use template from starter-kit)
- [ ] `.env.example` with all required variables (no real values!)

---

## 🧪 Testing Checklist

**Before submitting, verify:**

### Automated Tests
- [ ] `pytest tests/ -v` → All pass
- [ ] `pytest --cov=src` → >80% coverage
- [ ] All 5 UDC endpoints tested

### Manual Tests
```bash
# Test registration
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","github_username":"testuser","discord_id":"123456"}'

# Should return: {"success": true, ...}

# Test UDC endpoints
curl http://localhost:8000/health
curl http://localhost:8000/capabilities
```

### Security Tests
- [ ] No secrets in code: `grep -rn "password\|secret" src/`
- [ ] `.env` gitignored: `git status` should not show `.env`
- [ ] `env.example` has placeholders only

---

## 💡 Success Criteria

**Your Service passes if:**
1. ✅ Valid registration completes in <5 seconds
2. ✅ Disposable emails are rejected
3. ✅ Rate limiting prevents spam
4. ✅ Credentials are generated via Bitwarden
5. ✅ Welcome email is sent
6. ✅ All tests pass
7. ✅ UDC compliant (all 5 endpoints work)
8. ✅ No secrets exposed

---

## 🔧 Configuration

### Environment Variables (in .env)
```bash
# Service Identity
SERVICE_NAME=onboarding-orchestrator
SERVICE_ID=16
REGISTRY_URL=[PROVIDED BY COORDINATOR]
JWT_SECRET=[PROVIDED BY COORDINATOR]

# Bitwarden
BITWARDEN_CLIENT_ID=[PROVIDED BY COORDINATOR]
BITWARDEN_CLIENT_SECRET=[PROVIDED BY COORDINATOR]

# Email
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USER=[PROVIDED BY COORDINATOR]
EMAIL_PASS=[PROVIDED BY COORDINATOR]

# Rate Limiting
RATE_LIMIT_ENABLED=true
```

---

## 📚 Required Libraries

Add to `requirements.txt`:
```
fastapi>=0.104.0
uvicorn>=0.23.0
pydantic>=2.0.0
sqlalchemy>=2.0.0
slowapi>=0.1.9
disposable-email-domains>=0.0.91
jinja2>=3.1.0
python-multipart
pytest
httpx
```

---

## 📤 Submission

When complete:

1. **Push to YOUR repo:**
```bash
git add .
git commit -m "Complete Service #16 - Onboarding Orchestrator"
git push origin main
```

2. **Reply to Coordinator:**
```
Subject: Service #16 Complete - [Your Name]

Repository: https://github.com/yourname/service-16-onboarding

Quick test:
git clone https://github.com/yourname/service-16-onboarding
cd service-16-onboarding
cp env.example .env  # Add test credentials
pip install -r requirements.txt
pytest
python src/main.py

All requirements completed. See HANDOFF.md for details.
```

---

## 🆘 Need Help?

**Common Issues:**

**"Bitwarden CLI not working"**
- Mock it in tests
- Ask AI: "Create a mock for Bitwarden Send API calls"

**"Tests failing"**
- Read error message
- Ask AI: "This test is failing: [paste error]. Fix the code."

**"Not sure how to implement X"**
- Check starter-kit/docs/
- Ask AI with context: "Using FastAPI, how do I [X]?"

**Still stuck?**
Contact your Coordinator with:
- What you're trying to do
- What you've tried
- Error messages
- Repo link

---

**Ready to build? Copy the template and use the AI prompts above!** 🚀
