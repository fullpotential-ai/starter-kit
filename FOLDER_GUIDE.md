# 📂 Folder Navigation Guide

> **Quick Reference:** Where to find everything in this starter kit

---

## 🎯 I Want To...

| Goal | Go Here | Time |
|------|---------|------|
| **Get started (first time)** | [`START_HERE.md`](START_HERE.md) | 5 min |
| **Learn core concepts** | [`lessons/01_CORE_CONCEPTS.md`](lessons/01_CORE_CONCEPTS.md) | 10 min |
| **Set up my environment** | [`lessons/02_SETUP_ENVIRONMENT.md`](lessons/02_SETUP_ENVIRONMENT.md) | 15 min |
| **Build my Service** | [`lessons/03_BUILD_YOUR_SERVICE.md`](lessons/03_BUILD_YOUR_SERVICE.md) | 1-2 hrs |
| **Test my Service** | [`lessons/04_TESTING.md`](lessons/04_TESTING.md) | 15 min |
| **Deploy with Docker** | [`lessons/05_DOCKER_DEPLOYMENT.md`](lessons/05_DOCKER_DEPLOYMENT.md) | 10 min |
| **Submit my work** | [`lessons/06_SUBMISSION.md`](lessons/06_SUBMISSION.md) | 10 min |
| **See a quick example** | [`examples/service-simple/`](examples/service-simple/) | 5 min |
| **Copy the template** | [`templates/python-fastapi/`](templates/python-fastapi/) | 2 min |
| **Get a cheat sheet** | [`docs/QUICK_REFERENCE.md`](docs/QUICK_REFERENCE.md) | 5 min |

---

## 📁 Folder Structure Explained

```
starter-kit/
│
├── 🚀 START_HERE.md              👈 BEGIN HERE!
│   └─→ Your complete onboarding guide
│
├── 📚 lessons/                   👈 Step-by-step tutorials
│   ├── 01_CORE_CONCEPTS.md       (What are Services/UDC?)
│   ├── 02_SETUP_ENVIRONMENT.md   (Get tools ready)
│   ├── 03_BUILD_YOUR_SERVICE.md  (Write code)
│   ├── 04_TESTING.md             (Verify it works)
│   ├── 05_DOCKER_DEPLOYMENT.md   (Package in container)
│   └── 06_SUBMISSION.md          (Submit to Coordinator)
│
├── 📖 docs/                      👈 Reference documentation
│   ├── UDC_COMPLIANCE.md         (The 5 required endpoints)
│   ├── SERVICE_STANDARDS.md      (Code quality rules)
│   ├── TECH_STACK.md            (Approved technologies)
│   ├── SECURITY_REQUIREMENTS.md  (Security rules)
│   ├── SERVICE_INTEGRATION.md    (How Services communicate)
│   ├── GETTING_STARTED.md        (Hands-on tutorial)
│   └── QUICK_REFERENCE.md        (One-page cheat sheet)
│
├── 🔧 templates/                 👈 Copy this to start building
│   └── python-fastapi/
│       ├── src/main.py           (Entry point - customize this)
│       ├── src/config.py         (Environment settings)
│       ├── tests/test_udc.py     (Pre-written tests)
│       ├── Dockerfile            (Ready to deploy)
│       ├── requirements.txt      (Dependencies)
│       └── README.md             (Template documentation)
│
├── 💡 examples/                  👈 Working examples
│   └── service-simple/
│       ├── src/main.py           (~20 lines, fully UDC compliant)
│       └── README.md             (How to run it)
│
├── 📋 MISSION_TEMPLATE.md        👈 Fill when assigned
├── 📋 HANDOFF_TEMPLATE.md        👈 Fill when submitting
├── 🔒 SECURITY.md                👈 Read before first commit!
├── 📄 README.md                  👈 Overview & philosophy
├── 📂 FOLDER_GUIDE.md            👈 YOU ARE HERE
└── 📄 STARTER_KIT_OVERVIEW.md    👈 Complete kit description
```

---

## 🎓 Learning Paths

### Path 1: Absolute Beginner (Total: ~3-4 hours)

```
Day 1 (30 minutes):
1. START_HERE.md (5 min)
2. lessons/01_CORE_CONCEPTS.md (10 min)
3. docs/UDC_COMPLIANCE.md (10 min)
4. examples/service-simple/ (5 min) - run it!

Day 2 (15 minutes):
5. lessons/02_SETUP_ENVIRONMENT.md (15 min) - hands-on

Day 3 (2-3 hours):
6. lessons/03_BUILD_YOUR_SERVICE.md (2-3 hrs) - build it!

Day 4 (30 minutes):
7. lessons/04_TESTING.md (15 min)
8. lessons/05_DOCKER_DEPLOYMENT.md (10 min)
9. lessons/06_SUBMISSION.md (5 min)
```

### Path 2: Experienced Developer (Total: ~1 hour)

```
Quick Start (30 minutes):
1. START_HERE.md - skim overview (2 min)
2. docs/QUICK_REFERENCE.md - cheat sheet (3 min)
3. docs/UDC_COMPLIANCE.md - 5 endpoints (5 min)
4. Copy templates/python-fastapi/ (2 min)
5. Customize & build (18 min)

Testing & Deploy (30 minutes):
6. pytest + manual testing (15 min)
7. Docker build & test (10 min)
8. Fill HANDOFF_TEMPLATE.md (5 min)
```

### Path 3: Just Need a Reminder

```
One File (5 minutes):
→ docs/QUICK_REFERENCE.md
  (One-page cheat sheet with all commands & patterns)
```

---

## 📚 Documentation by Topic

### Understanding the System
- **What are Services?** → `lessons/01_CORE_CONCEPTS.md`
- **What is UDC?** → `docs/UDC_COMPLIANCE.md`
- **How do Services communicate?** → `docs/SERVICE_INTEGRATION.md`
- **Overall architecture?** → `README.md` Philosophy section

### Building Code
- **Quick template guide** → `templates/python-fastapi/README.md`
- **Code standards** → `docs/SERVICE_STANDARDS.md`
- **What libraries to use** → `docs/TECH_STACK.md`
- **Security rules** → `docs/SECURITY_REQUIREMENTS.md`

### Testing & Deployment
- **How to test** → `lessons/04_TESTING.md`
- **Docker basics** → `lessons/05_DOCKER_DEPLOYMENT.md`
- **Submission process** → `lessons/06_SUBMISSION.md`

### Quick Reference
- **All commands & code** → `docs/QUICK_REFERENCE.md`
- **Hands-on tutorial** → `docs/GETTING_STARTED.md`

---

## 🔍 Finding Specific Information

### "How do I...?"

| Question | Answer Location |
|----------|-----------------|
| "...implement /health endpoint?" | `docs/UDC_COMPLIANCE.md` → Section "1. Health Check" |
| "...handle messages?" | `lessons/03_BUILD_YOUR_SERVICE.md` → Step 4 |
| "...call another Service?" | `docs/SERVICE_INTEGRATION.md` → "Calling Another Service" |
| "...use Pydantic?" | `lessons/03_BUILD_YOUR_SERVICE.md` → Step 6 |
| "...run tests?" | `lessons/04_TESTING.md` → Step 1 |
| "...build Docker?" | `lessons/05_DOCKER_DEPLOYMENT.md` → Step 2 |
| "...name my variables?" | `docs/SERVICE_STANDARDS.md` → Naming Conventions |
| "...keep secrets safe?" | `docs/SECURITY_REQUIREMENTS.md` → Secret Management |

### "What is...?"

| Term | Explanation Location |
|------|---------------------|
| Service / Droplet | `lessons/01_CORE_CONCEPTS.md` |
| UDC | `lessons/01_CORE_CONCEPTS.md` + `docs/UDC_COMPLIANCE.md` |
| Registry | `lessons/01_CORE_CONCEPTS.md` → Architecture |
| trace_id | `docs/SERVICE_INTEGRATION.md` → Trace IDs |
| Heartbeat | `docs/UDC_COMPLIANCE.md` → Heartbeat Protocol |

### "Where do I...?"

| Task | Location |
|------|----------|
| Start learning | `START_HERE.md` |
| Copy template | `templates/python-fastapi/` |
| See working example | `examples/service-simple/` |
| Find cheat sheet | `docs/QUICK_REFERENCE.md` |
| Get assignment format | `MISSION_TEMPLATE.md` |
| Prepare submission | `HANDOFF_TEMPLATE.md` + `lessons/06_SUBMISSION.md` |

---

## 🎯 Files by Purpose

### For Learning
- `START_HERE.md` - Complete onboarding
- `lessons/` folder - Step-by-step tutorials
- `examples/service-simple/` - Minimal working example

### For Reference
- `docs/UDC_COMPLIANCE.md` - Endpoint specifications
- `docs/QUICK_REFERENCE.md` - One-page cheat sheet
- `docs/SERVICE_STANDARDS.md` - Code quality rules
- `docs/TECH_STACK.md` - Approved tools
- `docs/SECURITY_REQUIREMENTS.md` - Security rules
- `docs/SERVICE_INTEGRATION.md` - Multi-service patterns

### For Building
- `templates/python-fastapi/` - Production template
- `templates/python-fastapi/src/main.py` - Entry point (customize here)
- `templates/python-fastapi/tests/` - Pre-written tests

### For Process
- `MISSION_TEMPLATE.md` - Assignment format (fill when assigned)
- `HANDOFF_TEMPLATE.md` - Submission format (fill when done)
- `SECURITY.md` - Public repo policy (read before committing!)

### For Context
- `README.md` - Overview & philosophy
- `STARTER_KIT_OVERVIEW.md` - Complete kit description
- `FOLDER_GUIDE.md` - This file!

---

## 💡 Pro Tips

### Tip 1: Bookmark These
- `START_HERE.md` - Your map
- `docs/QUICK_REFERENCE.md` - Your cheat sheet
- `docs/UDC_COMPLIANCE.md` - Your bible

### Tip 2: Follow the Numbers
Files in `lessons/` are numbered 01-06 for a reason. Follow them in order!

### Tip 3: Use Search
Need to find something? Use your editor's search:
```
# VS Code: Cmd/Ctrl + Shift + F
# Search across all files in starter-kit
```

### Tip 4: Keep START_HERE Open
While learning, keep `START_HERE.md` open in one tab as your navigation hub.

### Tip 5: Print the Checklists
Print the checklists from `HANDOFF_TEMPLATE.md` and check them off as you go.

---

## 🆘 Still Can't Find Something?

### Search Pattern
1. Check `START_HERE.md` for pointers
2. Check this `FOLDER_GUIDE.md` for location
3. Check `docs/QUICK_REFERENCE.md` for quick answers
4. Use full-text search across all files
5. Ask your Coordinator

### Common "Can't Find" Issues

**"Where's the example Service?"**  
→ `examples/service-simple/src/main.py`

**"Where's the template I copy?"**  
→ `templates/python-fastapi/` (copy entire folder)

**"Where are the 5 endpoints explained?"**  
→ `docs/UDC_COMPLIANCE.md`

**"Where's the one-page cheat sheet?"**  
→ `docs/QUICK_REFERENCE.md`

**"Where's the step-by-step tutorial?"**  
→ Start with `lessons/01_CORE_CONCEPTS.md` or `docs/GETTING_STARTED.md`

---

## 🎓 Which File Should I Read Next?

### If you're at... → Read this next:

| Current Location | Next Step |
|------------------|-----------|
| Just arrived | `START_HERE.md` |
| START_HERE.md | `lessons/01_CORE_CONCEPTS.md` |
| 01_CORE_CONCEPTS.md | `docs/UDC_COMPLIANCE.md` |
| UDC_COMPLIANCE.md | `lessons/02_SETUP_ENVIRONMENT.md` |
| 02_SETUP_ENVIRONMENT.md | `lessons/03_BUILD_YOUR_SERVICE.md` |
| 03_BUILD_YOUR_SERVICE.md | `lessons/04_TESTING.md` |
| 04_TESTING.md | `lessons/05_DOCKER_DEPLOYMENT.md` |
| 05_DOCKER_DEPLOYMENT.md | `lessons/06_SUBMISSION.md` |
| 06_SUBMISSION.md | 🎉 You're done! Submit your Service |

---

## 📊 File Statistics

- **Total Lessons:** 6 step-by-step guides
- **Total Docs:** 7 reference documents
- **Templates:** 1 production-ready (Python/FastAPI)
- **Examples:** 1 minimal working Service
- **Total Reading Time:** ~2 hours (at your own pace)
- **Total Build Time:** 2-4 hours (depending on complexity)

---

**Lost? Start here:** [`START_HERE.md`](START_HERE.md)  
**Need quick answer? Check:** [`docs/QUICK_REFERENCE.md`](docs/QUICK_REFERENCE.md)  
**Ready to build? Copy:** [`templates/python-fastapi/`](templates/python-fastapi/)

---

**Happy building! 🚀**

