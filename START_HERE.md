# 🎯 START HERE - Apprentice Onboarding

> **Welcome to the Full Potential AI Starter Kit!**  
> This is your **template repository** - you'll copy from here to build your Service.

---

## ⏱️ **MISSION TO PRODUCTION: 3-5 HOURS**

**Your work:** 2-3 hours | **Waiting:** 1-2 hours | **LIVE:** Same day

| Hour | Phase | Who | What |
|------|-------|-----|------|
| 0-0.5 | Setup | **YOU** | Copy template, install deps ✅ |
| 0.5-2 | Build | **YOU** | AI generates code from prompts ✅ |
| 2-2.5 | Submit | **YOU** | Tests, security, push to GitHub ✅ |
| 2.5-3 | Review | Verifier | Code review & testing ⏳ |
| 3-3.5 | Deploy | Coordinator | Push to production ⏳ |
| **3.5** | **LIVE** | - | **Service running!** 🚀 |

**See [`AGGRESSIVE_TIMELINE.md`](AGGRESSIVE_TIMELINE.md) for hour-by-hour breakdown**

---

## ⚡ FAST PATH (10 Minutes)

**Just want to start building right away?**

```bash
# 1. Copy the template to YOUR new repo
cp -r templates/python-fastapi ../service-16-yourname
cd ../service-16-yourname
git init

# 2. Set up environment
cp env.example .env
pip install -r requirements.txt

# 3. Verify it works
pytest
uvicorn src.main:app --reload

# 4. Test the endpoints
curl http://localhost:8000/health
```

✅ **You now have a working UDC-compliant service!** Read your `MISSION_SPEC.md` and start customizing.

---

## 🤖 USING AI IN THE ASSEMBLY LINE

**You're not coding alone - you're working with AI!**

### Choose Your AI Tools (Pick What You Have)

**Option 1: Cursor (Recommended)**
- All-in-one code editor with AI
- Works with Claude, GPT-4, or other models
- Free tier available, Pro recommended ($20/month)
- **Best for:** Integrated coding + AI in one tool

**Option 2: Gemini (Free Alternative)**
- **Gemini 2.0 Flash** (free) - Fast, good for code generation
- **Gemini with Gems** - Like Claude Projects (upload context files)
- Upload starter-kit docs to a Gem for context
- **Best for:** Free access, unlimited usage

**Option 3: Claude (Premium)**
- Claude 3.5 Sonnet - Excellent code understanding
- Projects feature - Upload entire codebase
- $20/month subscription
- **Best for:** Complex reasoning, code review

**Option 4: ChatGPT**
- GPT-4 or GPT-4o - Strong general coding
- Free tier (GPT-3.5) or $20/month (GPT-4)
- **Best for:** Familiar interface, good documentation

**Mix & Match Strategy (Recommended):**
- **Build:** Use Gemini or Cursor (fast, cheap/free)
- **Review:** Use free Claude or ChatGPT to verify code quality
- **Debug:** Ask different AI if stuck (fresh perspective)

### How to Use AI

**For each mission:**
1. **Read your `MISSION_SPEC.md`** - It includes pre-written prompts
2. **Copy prompts into your chosen AI** - Use the exact prompts provided
3. **AI generates code** - Based on UDC template + requirements
4. **You verify & test** - Run tests, check endpoints
5. **Iterate** - Ask AI to fix issues, add features
6. **Use AI for handoff** - Generate `HANDOFF.md` sections

**Example workflow:**
```
You: [Paste Prompt 1 from MISSION_SPEC.md]
Gemini/Claude/GPT: [Generates code for endpoint]
You: pytest tests/  # Verify it works
You: "Add error handling for invalid input"
AI: [Updates code]
You: pytest tests/  # Verify again
```

**Pro Tip with Gemini Gems:**
1. Create a Gem called "Full Potential AI Service Builder"
2. Upload: `starter-kit/docs/UDC_COMPLIANCE.md`, `SERVICE_STANDARDS.md`, your `MISSION_SPEC.md`
3. Now Gemini has all context for better answers

**Multi-AI Verification Strategy:**
```
Build Phase: Use Gemini (fast, free, unlimited)
  ↓
Code Review: Ask free Claude "Review this code for issues"
  ↓
Alternative Check: Ask ChatGPT "Does this follow best practices?"
  ↓
Final Verify: Run pytest (automated truth)
```

**Why multiple AIs?** Each has different strengths. Gemini might miss something Claude catches, or vice versa. Free tier of each is usually enough for review.

**Key: The spec includes prompts. Don't start from scratch!**

---

## 📋 COMPLETE BUILD FLOW

### Where You Are in the Process

```
┌─────────────────────────────────────────────┐
│ 1. Architect creates spec                  │ ← Already done
│    (James + AI makes MISSION_SPEC.md)      │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 2. Coordinator posts mission                │ ← Already done
│    (You claimed it!)                        │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 3. YOU BUILD (with AI)                      │ ← YOU ARE HERE
│    - Copy template from starter-kit         │
│    - Read MISSION_SPEC.md                   │
│    - Use AI with provided prompts           │
│    - Test locally                           │
│    - Fill HANDOFF.md                        │
│    - Push to YOUR public GitHub repo        │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 4. Verifier reviews your work               │ ← They do this
│    - Tests your code                        │
│    - Checks UDC compliance                  │
│    - PASS / NEEDS REVISION / FAIL           │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 5. If PASS → Production deployment          │ ← Coordinator does
│    - Deployed to production server          │
│    - Joins the Full Potential AI network    │
│    - You get paid!                          │
└─────────────────────────────────────────────┘
```

---

## 🏗️ YOUR BUILDING PROCESS (Step-by-Step)

### Step 1: Set Up Your Workspace (5 min)

```bash
# Clone this starter-kit (read-only reference)
git clone https://github.com/fullpotential-ai/starter-kit.git

# Copy template to YOUR new repo
cp -r starter-kit/templates/python-fastapi ../service-16-yourname
cd ../service-16-yourname

# Initialize YOUR git repo (this is what you'll submit)
git init
git add .
git commit -m "Initial commit from starter-kit template"

# Create YOUR GitHub repo and push
# (Create repo at github.com/yourusername/service-16-yourname)
git remote add origin https://github.com/yourusername/service-16-yourname.git
git push -u origin main
```

**Important:** 
- ✅ You build in YOUR repo (`service-16-yourname`)
- ✅ You submit YOUR repo URL
- ❌ You NEVER commit to `starter-kit` (it's just a template)

---

### Step 2: Read Foundation Docs (10 min)

**Before coding, understand the rules:**

1. **Read:** `starter-kit/docs/UDC_COMPLIANCE.md`
   - The 5 required endpoints
   - What they must return
   - Why they matter

2. **Read:** `starter-kit/docs/SERVICE_STANDARDS.md`
   - Code quality expectations
   - Naming conventions
   - Testing requirements

3. **Read:** Your `MISSION_SPEC.md` (provided by Coordinator)
   - Your specific requirements
   - Pre-written AI prompts
   - Success criteria

---

### Step 3: Build Using AI (1-3 hours)

**The template already has all 5 UDC endpoints working!**

Your job is to **add your business logic** to the `/message` endpoint (or new endpoints).

#### Using the Pre-Written Prompts

Your `MISSION_SPEC.md` includes prompts like this:

```markdown
### Prompt 1: Initial Setup
```
Using the starter-kit Python FastAPI template, add:
- POST /register endpoint accepting: email, github_username, discord_id
- Email validation (reject disposable emails)
- SQLite database for tracking registrations
```
```

**Just copy that entire prompt into Cursor/Claude and let it generate!**

#### Typical AI Session

```
You: [Paste Prompt 1 from spec]

AI: [Generates code for new endpoint]

You: Save to src/main.py, then:
     pytest tests/ -v

You: "Add rate limiting: 10 requests per hour per IP"

AI: [Updates code with rate limiting]

You: pytest tests/ -v  # Verify it works

You: "Write tests for the new /register endpoint"

AI: [Generates test_register.py]

You: pytest tests/ -v  # All tests pass!
```

**Key principles:**
- Start with spec prompts (don't improvise)
- Test after every change
- Ask AI to fix test failures
- Keep UDC endpoints working (don't delete them!)

---

### Step 4: Test Locally (15 min)

```bash
# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v --cov=src

# Should see: All tests pass, >80% coverage

# Run the service
python src/main.py

# Test in another terminal:
curl http://localhost:8000/health
curl http://localhost:8000/capabilities
curl -X POST http://localhost:8000/message \
  -H "Content-Type: application/json" \
  -d '{"type":"test", "payload":{}, "trace_id":"local-test"}'
```

**Checklist before moving on:**
- [ ] All tests pass (`pytest`)
- [ ] >80% code coverage
- [ ] All 5 UDC endpoints respond
- [ ] Your custom logic works
- [ ] No errors in logs

---

### Step 5: Fill Out HANDOFF.md (10 min)

```bash
# Copy the template
cp ../starter-kit/HANDOFF_TEMPLATE.md HANDOFF.md

# Use AI to help fill it out
```

**In Cursor/Claude:**
```
Prompt: "I've completed a service that does [describe]. 
Review my code in src/main.py and help me fill out 
the HANDOFF.md template. Include:
- Implementation summary
- Key features
- Technologies used
- Known limitations
- How to test"
```

AI will generate draft content. **You must review and verify it!**

---

### Step 6: Security Check (5 min)

**CRITICAL - Run these before submitting:**

```bash
# 1. Check for secrets
grep -rn "password\|secret\|key\|token" src/ --include="*.py"
# Should only find variable NAMES, not values

# 2. Check .env is gitignored
cat .gitignore | grep .env
# Should show: .env

# 3. Verify .env not in repo
git status
# Should NOT show .env

# 4. Check credentials are in .env.example only
cat .env.example
# Should have placeholders like "your-secret-here"
```

**If you find a secret in code:** 
1. Move it to `.env`
2. Load from environment
3. Check git history: `git log -p | grep -i "secret"`
4. If in history, contact Coordinator immediately!

---

### Step 7: Submit (2 min)

```bash
# Final commit
git add .
git commit -m "Complete Service #16 - [Feature Name]"
git push origin main
```

**Reply to your Coordinator with:**
```
Subject: Service #16 Complete - [Your Name]

Repository: https://github.com/yourusername/service-16-yourname

Quick test:
git clone https://github.com/yourusername/service-16-yourname
cd service-16-yourname
pip install -r requirements.txt
pytest
python src/main.py

All requirements from MISSION_SPEC.md completed.
See HANDOFF.md for details.
```

---

## 🛠️ Tools You Need

**Required:**
- Python 3.11+ - [Download](https://www.python.org/downloads/)
- Git - [Download](https://git-scm.com/)
- **AI Assistant** - Choose one (or mix):
  - **Gemini** (free) - [gemini.google.com](https://gemini.google.com)
  - **Cursor** ($20/mo or free tier) - [cursor.sh](https://cursor.sh)
  - **Claude** ($20/mo) - [claude.ai](https://claude.ai)
  - **ChatGPT** (free or $20/mo) - [chat.openai.com](https://chat.openai.com)
- Code editor (VS Code, PyCharm, or Cursor)
- GitHub account (free)

**Recommended Combo (Free):**
- **Gemini** for code generation (fast, unlimited)
- **Free Claude** for code review (limited but powerful)
- **VS Code** as editor

**Recommended Combo (Premium):**
- **Cursor** for integrated AI + coding
- **Claude** for complex problem-solving

**Optional but helpful:**
- Docker (for local container testing)
- Postman (for API testing)

---

## 📚 Reference Docs (In starter-kit)

**While building, reference these:**

| Doc | When to Read |
|-----|-------------|
| `docs/UDC_COMPLIANCE.md` | Before starting (required) |
| `docs/SERVICE_STANDARDS.md` | While coding |
| `docs/TECH_STACK.md` | When choosing libraries |
| `docs/SECURITY_REQUIREMENTS.md` | Before committing |
| `docs/SERVICE_INTEGRATION.md` | If calling other Services |
| `docs/QUICK_REFERENCE.md` | Anytime (cheat sheet) |

**Extended lessons available:**
- `lessons/01_CORE_CONCEPTS.md` - Deep dive on Services/UDC
- `lessons/02_SETUP_ENVIRONMENT.md` - Detailed setup
- `lessons/03_BUILD_YOUR_SERVICE.md` - Building patterns
- `lessons/04_TESTING.md` - Testing strategies
- `lessons/05_DOCKER_DEPLOYMENT.md` - Docker guide
- `lessons/06_SUBMISSION.md` - Submission details

**Read these if you want deeper understanding, but not required to complete your mission.**

---

## ❓ Common Questions

### "Do I code everything from scratch?"
**No!** The template has all UDC endpoints working. You just add your business logic.

### "Can I use AI to write all the code?"
**Yes!** That's the point. Use the prompts in your MISSION_SPEC.md.

### "What if the tests fail?"
Ask AI: "The test test_register is failing with error [paste error]. Fix the code."

### "Can I add my own endpoints?"
**Yes!** Add any endpoints you need. Just keep the 5 UDC endpoints working.

### "What if I get stuck?"
1. Try asking AI to help debug
2. Check the relevant doc in `starter-kit/docs/`
3. Read the extended lesson if available
4. Contact your Coordinator

### "Do I need to understand everything?"
**No.** Understand the 5 UDC endpoints and your specific mission. The rest you can learn over time.

---

## ✅ Submission Checklist

Before submitting, verify:

**Code Quality:**
- [ ] All tests pass (`pytest`)
- [ ] Coverage >80% (`pytest --cov`)
- [ ] All 5 UDC endpoints respond correctly
- [ ] Your business logic works as specified
- [ ] Code has type hints and docstrings

**Security:**
- [ ] NO secrets in code (checked with grep)
- [ ] `.env` file gitignored (checked with git status)
- [ ] `env.example` has placeholders only
- [ ] No secrets in git history

**Documentation:**
- [ ] `HANDOFF.md` filled out completely
- [ ] `README.md` updated with your service details
- [ ] Comments explain complex logic

**Submission:**
- [ ] Pushed to PUBLIC GitHub repo
- [ ] Repo URL sent to Coordinator
- [ ] Can be cloned and tested by anyone

---

## 🎉 After Submission

### What Happens Next?

**Verification (1-3 days):**
- Verifier clones your repo
- Runs tests
- Checks UDC compliance
- Reviews code quality
- Decision: PASS / NEEDS REVISION / FAIL

**If PASS:**
- ✅ Deployed to production server
- ✅ Service joins Full Potential AI network
- ✅ You get paid ($40 or as specified)
- ✅ Available for next mission!

**If NEEDS REVISION:**
- Verifier provides specific feedback
- You fix issues
- Re-submit
- *This is normal! Learn and improve.*

---

## 🚀 You Got This!

**Remember:**
1. The template already works (UDC endpoints done)
2. Use AI with the provided prompts (don't start from scratch)
3. Test frequently (catch issues early)
4. Submit YOUR repo (not starter-kit)
5. Ask for help when stuck (Coordinator is there)

**Your mission is achievable. Thousands of lines of boilerplate are already written. You just add the special sauce for your specific Service.**

**Let's build! 🎯**

---

## 📞 Need Help?

**Contact your Coordinator with:**
- Clear description of issue
- What you've tried
- Error messages (if any)
- Link to your repo

**Response time:** Usually within 24 hours

---

**Next:** Copy the template and read your `MISSION_SPEC.md`! 🚀
