# 🧬 Full Potential AI Starter Kit

> **Welcome, Apprentice!** You're about to build autonomous Services that form the Full Potential AI intelligence network.

---

## 🚀 **[START HERE →](START_HERE.md)** 

**New to this?** Click the link above for your complete step-by-step guide!  
**Can't find something?** Check the **[Folder Guide →](FOLDER_GUIDE.md)**

---

## 🎯 What You'll Build

You'll create a **Service** (also called a "Droplet") - an autonomous backend process that:
- Performs specific work (AI inference, data processing, storage, etc.)
- Communicates with other Services via a standard protocol
- Self-registers and maintains its own health
- Runs independently in a container

Think of it like building a specialized cell in a living organism. Each cell has a specific job, but they all work together through a common language.

---

## 📚 Key Concepts (Read This First!)

### Services vs. Tiles vs. UDC

| Concept | What It Is | Example |
|---------|-----------|---------|
| **Service (Droplet)** | Backend process that does work | Image analysis service, database connector |
| **Tile** | Frontend component that displays data | Dashboard widget, visualization panel |
| **UDC (Universal Droplet Contract)** | The "language" Services speak | 5 required HTTP endpoints every Service must have |

### What is UDC?
Just like HTTP is the protocol for web pages, **UDC is the protocol for Services to talk to each other**. 

Every Service must implement 5 endpoints:
1. `/health` - "Are you alive?"
2. `/capabilities` - "What can you do?"
3. `/state` - "How are you doing?"
4. `/dependencies` - "What do you need?"
5. `/message` - "Here's a task for you"

---

## 🚀 Quick Start (3 Steps)

### Step 1: Copy the Template
```bash
# Copy the production template to your new service folder
cp -r templates/python-fastapi ../my-awesome-service
cd ../my-awesome-service
```

### Step 2: Customize Your Service
```bash
# Set up environment
cp env.example .env
# Edit .env with values provided by your coordinator

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Test & Verify
```bash
# Run tests to verify UDC compliance
pytest

# Start your service
uvicorn src.main:app --reload

# Test it's working
curl http://localhost:8000/health
```

**✅ If you see a JSON response, you're ready to add your custom logic!**

---

## 📂 Repository Structure

```
starter-kit/
│
├── 📖 docs/                    ← START HERE: Read these in order
│   ├── GETTING_STARTED.md      (0) 👈 BRAND NEW? START HERE!
│   ├── UDC_COMPLIANCE.md       (1) The "Bible" - 5 required endpoints
│   ├── SERVICE_STANDARDS.md    (2) How to write clean Python code
│   ├── TECH_STACK.md          (3) What tools you can use
│   ├── SECURITY_REQUIREMENTS.md(4) How to keep secrets safe
│   └── SERVICE_INTEGRATION.md  (5) How Services talk to each other
│
├── 🔧 templates/
│   └── python-fastapi/         ← COPY THIS to start your service
│       ├── src/               (Your code goes here)
│       ├── tests/             (Pre-written UDC tests)
│       ├── Dockerfile         (Ready to deploy)
│       └── README.md          (Template-specific instructions)
│
├── 💡 examples/
│   └── service-simple/         ← See a minimal working example
│
├── MISSION_TEMPLATE.md         ← Use this when you get an assignment
├── HANDOFF_TEMPLATE.md         ← Use this when you submit your work
└── SECURITY.md                 ← CRITICAL: What NOT to commit
```

---

## 🎓 Your First Mission (15 Minutes)

**Follow this learning path:**

```
Step 1: Understand the Basics (5 min)
  📖 Read docs/UDC_COMPLIANCE.md
  → Learn what the 5 endpoints do

Step 2: See It In Action (3 min)
  💡 Explore examples/service-simple/
  → Run a minimal working Service

Step 3: Build Your Service (5 min)
  🔧 Copy templates/python-fastapi/
  → Customize SERVICE_INFO
  → Add your business logic

Step 4: Verify Compliance (2 min)
  ✅ Run pytest
  → All tests should pass
```

**After these 4 steps, you'll have a working, UDC-compliant Service!**

---

## 🆘 Need Help?

- **🆕 "I'm completely new!"** → Start with `docs/GETTING_STARTED.md`
- **"What's a Droplet?"** → Read `docs/UDC_COMPLIANCE.md` - Section "What is a Droplet?"
- **"How do I structure my code?"** → Check `docs/SERVICE_STANDARDS.md`
- **"What libraries can I use?"** → See `docs/TECH_STACK.md`
- **"How do Services find each other?"** → Read `docs/SERVICE_INTEGRATION.md`
- **"I accidentally committed a secret!"** → See `SECURITY.md` immediately

---

## 🌟 Philosophy

> "You're not just writing code; you're building intelligence cells that work together as an organism."

Each Service is independent but connected. When you build a UDC-compliant Service, it automatically becomes part of a larger intelligence network. Your Service can discover others, send messages, and coordinate work - all through the standard UDC protocol.

**Think distributed. Think autonomous. Think organism.**

---

## 📊 What You Get

| Component | What's Inside | Why It Matters |
|-----------|---------------|----------------|
| **📖 Documentation** | 7 comprehensive guides | Learn UDC, standards, security, integration |
| **🔧 Template** | Production-ready FastAPI code | Start building in <5 minutes |
| **💡 Example** | Minimal working Service | Understand the basics quickly |
| **✅ Tests** | Pre-written compliance tests | Verify your Service works correctly |
| **🐳 Docker** | Ready-to-deploy Dockerfile | Deploy anywhere with confidence |
| **📋 Templates** | Mission & Handoff forms | Standardized workflow |
| **🔒 Security** | Clear policies & examples | Keep secrets safe |

---

## 🏆 Success Path

```
┌─────────────────────────────────────────────────────┐
│  Day 1: Learn                                       │
│  → Read GETTING_STARTED.md                          │
│  → Run service-simple example                       │
│  ✅ Understand UDC protocol                         │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│  Day 1-2: Build                                     │
│  → Copy python-fastapi template                     │
│  → Add your business logic                          │
│  → Run pytest to verify                             │
│  ✅ Working UDC-compliant Service                   │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│  Day 2-3: Deploy                                    │
│  → Docker build & test                              │
│  → Fill out HANDOFF_TEMPLATE.md                     │
│  → Submit to Coordinator                            │
│  ✅ Service running in production                   │
└─────────────────────────────────────────────────────┘
```

---
