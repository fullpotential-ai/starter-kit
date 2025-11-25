# Mission Specification: [Service Name]

> **Purpose:** This document defines what you need to build. Fill this out when you receive an assignment.

---

## 🎯 Objective
*One clear sentence describing what this Service does.*

**Example:** "Build a Service that analyzes uploaded images for text content using OCR."

---

## 📋 Requirements

### Functional Requirements
What your Service must DO:
- [ ] Must do X (be specific)
- [ ] Must handle Y (define inputs/outputs)
- [ ] Must output Z (specify format)

**Example:**
- [ ] Accept image uploads via `/message` endpoint
- [ ] Extract text using OCR library
- [ ] Return extracted text as JSON with confidence scores

### UDC Requirements (Non-Negotiable)
- [ ] Implement `/health` endpoint (returns service status)
- [ ] Implement `/capabilities` endpoint (lists features)
- [ ] Implement `/state` endpoint (current load/status)
- [ ] Implement `/dependencies` endpoint (what you need to run)
- [ ] Implement `/message` endpoint (receives tasks from other Services)

---

## 🏗️ Architecture

### Internal Flow
*Describe how data flows through your Service*

**Example:**
```
1. Receive image via /message
2. Validate image format
3. Process with OCR library
4. Return results with trace_id
```

### External Dependencies
*What other Services or systems does this connect to?*

**Example:**
- Storage Service (to fetch images)
- Database (to store results)

---

## 📦 Deliverables

When you're done, you must provide:
- [ ] Source code repository (GitHub link)
- [ ] `Dockerfile` that builds successfully
- [ ] Test suite with >80% coverage (all passing)
- [ ] `README.md` with setup instructions
- [ ] Filled-out `HANDOFF_TEMPLATE.md`

---

## ✅ Testing Checklist

Before submitting:
- [ ] All UDC endpoints return correct JSON format
- [ ] Unit tests cover core business logic
- [ ] Integration test with mock inputs
- [ ] Docker container runs without errors
- [ ] Manual test: `curl http://localhost:8000/health` works

---

## 📤 Submission

When ready, fill out `HANDOFF_TEMPLATE.md` and submit to your coordinator.

