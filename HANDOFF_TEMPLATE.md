# 📤 Service Handoff Checklist

> **Purpose:** Fill this out before submitting your completed Service. This ensures quality and compliance.

---

## ✅ Pre-Submission Checklist

### Repository Quality
- [ ] Repository is clean (no `__pycache__/`, no `.env` files committed)
- [ ] `README.md` has clear setup instructions specific to THIS service
- [ ] All code follows naming conventions (snake_case, PascalCase)
- [ ] Docstrings exist for all public functions

### Build & Deploy
- [ ] `Dockerfile` builds without errors: `docker build -t my-service .`
- [ ] Container runs successfully: `docker run -p 8000:8000 my-service`
- [ ] Service responds on port 8000

### Testing
- [ ] All tests pass: `pytest`
- [ ] Test coverage >80%: `pytest --cov`
- [ ] Manual test successful: `curl http://localhost:8000/health`

---

## 🔌 UDC Compliance Verification

Test each endpoint manually:

- [ ] **`GET /health`** → Returns `{"status": "active", "uptime": ..., "timestamp": ...}`
- [ ] **`GET /capabilities`** → Lists features and dependencies
- [ ] **`GET /state`** → Shows current status and uptime
- [ ] **`GET /dependencies`** → Lists required/optional services
- [ ] **`POST /message`** → Accepts tasks and returns `{"received": true, "trace_id": "..."}`

---

## 🔒 Security Verification

**CRITICAL:** Check these before submitting!

- [ ] NO secrets in source code (search for "password", "key", "secret")
- [ ] Checked git history: `git log -p | grep -i "secret"` returns nothing sensitive
- [ ] `env.example` or `.env.example` provided with placeholder values only
- [ ] All sensitive config loaded from environment variables
- [ ] Input validation using Pydantic models (not raw dict)
- [ ] `.gitignore` includes `.env`, `__pycache__/`, `*.pyc`

---

## 📝 Implementation Summary

### Service Name
*What's the official name of this Service?*

### Purpose
*One sentence: What does this Service do?*

### Key Features
*List 3-5 main capabilities*

Example:
- OCR text extraction from images
- Supports PNG, JPG, PDF formats
- Returns confidence scores per word

### Technologies Used
*What libraries/frameworks did you use?*

Example:
- FastAPI 0.104
- Tesseract OCR
- Pillow for image processing

### Trade-offs & Decisions
*Any important architectural decisions or limitations?*

Example:
- Limited to images <10MB due to memory constraints
- Synchronous processing (no queue) for simplicity

---

## 🧪 How to Test This Service

### Quick Test (30 seconds)
```bash
# Build
docker build -t my-service .

# Run
docker run -p 8000:8000 my-service

# Test health
curl http://localhost:8000/health
```

### Full Test (with sample data)
```bash
# Run test suite
pytest -v

# Test with sample input (customize this section)
curl -X POST http://localhost:8000/message \
  -H "Content-Type: application/json" \
  -d '{"type": "task", "payload": {"action": "test"}, "trace_id": "test-123"}'
```

**Expected Result:**
*Describe what successful output looks like*

---

## 📬 Submission

**Repository URL:** [Insert GitHub/GitLab link]

**Submitted by:** [Your Name]

**Date:** [YYYY-MM-DD]

**Coordinator:** [Coordinator Name]

---

## 🐛 Known Issues (Optional)

*List any known bugs or limitations*

Example:
- None at this time
- Performance degrades with images >5MB (acceptable per requirements)

