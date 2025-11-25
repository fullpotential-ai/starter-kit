# 🎯 START HERE - Apprentice Onboarding

> **Welcome to the Full Potential AI Starter Kit!**  
> This guide will take you from zero to your first deployed Service.

---

## 📋 What You're About To Do

You're going to build a **Service** (an autonomous backend process) that joins the Full Potential AI network. Think of it like creating a specialized worker that can communicate with other workers through a standard protocol.

**Time Commitment:**
- **First-time setup:** 15 minutes
- **Build your Service:** 2-3 hours (depending on complexity)
- **Testing & submission:** 30 minutes

---

## 🎓 Step-by-Step Learning Path

Follow these lessons in order. Each builds on the previous one.

### Phase 1: Understanding (30 minutes)

#### 📖 Lesson 1: Core Concepts (10 min)
**File:** `lessons/01_CORE_CONCEPTS.md`

What you'll learn:
- What is a Service (Droplet)?
- What is UDC (Universal Droplet Contract)?
- How Services work together

**Action:** Read this first to understand the big picture.

---

#### 📖 Lesson 2: The 5 Required Endpoints (15 min)
**File:** `docs/UDC_COMPLIANCE.md`

What you'll learn:
- The 5 endpoints every Service must have
- What each endpoint does and why
- How to test them

**Action:** This is your "bible" - bookmark it for reference.

---

#### 💡 Lesson 3: See a Working Example (5 min)
**Folder:** `examples/service-simple/`

What you'll learn:
- How simple a UDC Service can be (~20 lines)
- What a working Service looks like

**Action:** 
```bash
cd examples/service-simple
pip install -r requirements.txt
uvicorn src.main:app --reload
# Visit http://localhost:8000/docs
```

---

### Phase 2: Building (2-3 hours)

#### 🔧 Lesson 4: Set Up Your Development Environment (15 min)
**File:** `lessons/02_SETUP_ENVIRONMENT.md`

What you'll learn:
- How to copy the template
- How to configure your environment
- How to run tests

**Action:** Follow the step-by-step setup guide.

---

#### 🏗️ Lesson 5: Customize Your Service (30 min - 2 hours)
**File:** `lessons/03_BUILD_YOUR_SERVICE.md`

What you'll learn:
- How to modify the template for your needs
- Where to add your business logic
- How to handle messages from other Services

**Action:** This is where you implement your assigned mission.

---

#### 📏 Lesson 6: Code Quality & Standards (20 min)
**File:** `docs/SERVICE_STANDARDS.md`

What you'll learn:
- Python coding standards we follow
- How to structure your code
- Common mistakes to avoid

**Action:** Review this while coding, use as a checklist.

---

#### 🔒 Lesson 7: Security Requirements (15 min)
**File:** `docs/SECURITY_REQUIREMENTS.md`

What you'll learn:
- What NEVER to put in code
- How to handle secrets safely
- Security checklist before submission

**Action:** **CRITICAL** - Read before your first commit!

---

### Phase 3: Integration (30 minutes)

#### 🔗 Lesson 8: Service Integration (Optional for first build)
**File:** `docs/SERVICE_INTEGRATION.md`

What you'll learn:
- How to call other Services
- Authentication with JWT
- Service discovery through Registry

**Action:** Read if your Service needs to talk to other Services.

---

### Phase 4: Testing & Submission (30 minutes)

#### ✅ Lesson 9: Testing Your Service (15 min)
**File:** `lessons/04_TESTING.md`

What you'll learn:
- How to run automated tests
- How to manually test each endpoint
- How to verify UDC compliance

**Action:** Run all tests before submission.

---

#### 📦 Lesson 10: Docker & Deployment (10 min)
**File:** `lessons/05_DOCKER_DEPLOYMENT.md`

What you'll learn:
- How to build a Docker image
- How to test the container
- How to verify it's production-ready

**Action:** Build and test your container locally.

---

#### 📤 Lesson 11: Submission (5 min)
**File:** `lessons/06_SUBMISSION.md`

What you'll learn:
- How to fill out the handoff template
- What to include in your submission
- How to submit to your Coordinator

**Action:** Complete HANDOFF_TEMPLATE.md and submit.

---

## 🎯 Quick Navigation by Role

### "I'm brand new to this"
1. Read `lessons/01_CORE_CONCEPTS.md`
2. Run `examples/service-simple/`
3. Follow `docs/GETTING_STARTED.md`
4. Proceed through lessons 4-11

### "I have FastAPI experience"
1. Skim `docs/UDC_COMPLIANCE.md` (5 endpoints)
2. Skim `docs/QUICK_REFERENCE.md` (cheat sheet)
3. Copy `templates/python-fastapi/`
4. Jump to lessons 5-11

### "I just need a quick reminder"
- **Quick Reference:** `docs/QUICK_REFERENCE.md`
- **All in one page:** Cheat sheet for experienced devs

---

## 📁 Folder Structure Overview

```
starter-kit/
│
├── 🚀 START_HERE.md          ← YOU ARE HERE
│
├── 📚 lessons/               ← Step-by-step learning path
│   ├── 01_CORE_CONCEPTS.md
│   ├── 02_SETUP_ENVIRONMENT.md
│   ├── 03_BUILD_YOUR_SERVICE.md
│   ├── 04_TESTING.md
│   ├── 05_DOCKER_DEPLOYMENT.md
│   └── 06_SUBMISSION.md
│
├── 📖 docs/                  ← Reference documentation
│   ├── UDC_COMPLIANCE.md     (The "Bible" - 5 endpoints)
│   ├── SERVICE_STANDARDS.md  (Code quality rules)
│   ├── TECH_STACK.md        (Approved technologies)
│   ├── SECURITY_REQUIREMENTS.md (Security rules)
│   ├── SERVICE_INTEGRATION.md (Multi-service patterns)
│   ├── GETTING_STARTED.md    (Hands-on tutorial)
│   └── QUICK_REFERENCE.md    (One-page cheat sheet)
│
├── 🔧 templates/             ← Copy this to start building
│   └── python-fastapi/       (Production-ready template)
│
├── 💡 examples/              ← Working examples
│   └── service-simple/       (Minimal 20-line Service)
│
├── 📋 MISSION_TEMPLATE.md    ← Fill this out when assigned
├── 📋 HANDOFF_TEMPLATE.md    ← Fill this out when done
├── 🔒 SECURITY.md            ← Public repo security policy
└── 📄 README.md              ← Overview & philosophy
```

---

## 🎯 Your Mission Assignment

When you receive an assignment from your Coordinator, they'll give you:

1. **Mission Specification** - What to build
2. **Service ID** - Your unique number
3. **Credentials** - For Registry and JWT (never commit these!)

**Your workflow:**
1. Copy `MISSION_TEMPLATE.md` to your service repo
2. Fill it out with your assignment details
3. Build your Service following the lessons
4. Test thoroughly
5. Fill out `HANDOFF_TEMPLATE.md`
6. Submit to Coordinator

---

## 🛠️ Tools You'll Need

### Required
- **Python 3.11+** - [Download](https://www.python.org/downloads/)
- **pip** - Comes with Python
- **Git** - [Download](https://git-scm.com/)
- **Code editor** - VS Code, PyCharm, or your favorite
- **Docker** - [Download](https://www.docker.com/get-started)

### Helpful
- **Postman or curl** - For testing APIs
- **Terminal** - Command line access

---

## 🆘 Getting Help

### During Learning Phase
| Question | Where to Look |
|----------|---------------|
| "What's a Droplet?" | `lessons/01_CORE_CONCEPTS.md` |
| "How do I set up?" | `lessons/02_SETUP_ENVIRONMENT.md` |
| "Where do I add my code?" | `lessons/03_BUILD_YOUR_SERVICE.md` |
| "How do I test?" | `lessons/04_TESTING.md` |

### During Development
| Question | Where to Look |
|----------|---------------|
| "What libraries can I use?" | `docs/TECH_STACK.md` |
| "How do I structure code?" | `docs/SERVICE_STANDARDS.md` |
| "How do I keep secrets safe?" | `docs/SECURITY_REQUIREMENTS.md` |
| "How do I call other Services?" | `docs/SERVICE_INTEGRATION.md` |

### Quick Answers
- **One-page cheat sheet:** `docs/QUICK_REFERENCE.md`
- **All 5 endpoints explained:** `docs/UDC_COMPLIANCE.md`

### Still Stuck?
Contact your Coordinator with:
- What you're trying to do
- What you've tried
- What error you're getting

---

## ✅ Success Checklist

Before you begin, make sure you have:
- [ ] Python 3.11+ installed (`python --version`)
- [ ] pip working (`pip --version`)
- [ ] Docker installed (`docker --version`)
- [ ] Code editor ready
- [ ] Access to this starter-kit repository

Before you submit, verify:
- [ ] All 5 UDC endpoints implemented
- [ ] `pytest` passes all tests
- [ ] Docker builds successfully
- [ ] No secrets in code (checked git history)
- [ ] `HANDOFF_TEMPLATE.md` filled out
- [ ] README updated with service-specific info

---

## 🚀 Ready to Start?

### Absolute Beginner Path
```bash
# Step 1: Read core concepts (10 min)
open lessons/01_CORE_CONCEPTS.md

# Step 2: See it working (5 min)
cd examples/service-simple
pip install -r requirements.txt
uvicorn src.main:app --reload

# Step 3: Follow setup guide (15 min)
# Read lessons/02_SETUP_ENVIRONMENT.md and follow along

# Step 4: Build your service (2-3 hours)
# Read lessons/03_BUILD_YOUR_SERVICE.md and implement
```

### Experienced Developer Path
```bash
# Step 1: Quick overview (5 min)
open docs/QUICK_REFERENCE.md

# Step 2: Copy template (2 min)
cp -r templates/python-fastapi ../my-service
cd ../my-service

# Step 3: Build (1-2 hours)
# Customize src/main.py with your logic

# Step 4: Test & submit (30 min)
pytest
docker build -t my-service .
# Fill out HANDOFF_TEMPLATE.md
```

---

## 🎉 What Success Looks Like

After completing this path, you will have:
- ✅ A working, UDC-compliant Service
- ✅ All tests passing
- ✅ Docker container running your Service
- ✅ Understanding of how Services communicate
- ✅ A completed handoff ready for production deployment

**Let's build something amazing! 🚀**

---

## 📚 Additional Resources

- **Full Overview:** `STARTER_KIT_OVERVIEW.md` (detailed description of entire kit)
- **Interactive Tutorial:** `docs/GETTING_STARTED.md` (hands-on walkthrough)
- **Security Policy:** `SECURITY.md` (what never to commit)

---

**Next Step:** Open `lessons/01_CORE_CONCEPTS.md` and start learning! 🎓

