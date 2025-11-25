# ⚡ AGGRESSIVE TIMELINE - Mission to Production

> **Goal:** Mission posted → Service LIVE in **3-6 hours**

---

## 🎯 **YOUR EXECUTION TIMELINE**

### **Hour 0:00-0:30 - Mission Claimed & Setup** ⏱️ **30 minutes MAX**

**What you do:**
```bash
# Minute 0-5: Clone and copy
git clone https://github.com/fullpotential-ai/starter-kit.git
cp -r starter-kit/templates/python-fastapi ../service-16-yourname
cd ../service-16-yourname
git init

# Minute 5-10: Environment setup
cp env.example .env
# Paste credentials from Bitwarden Send into .env
pip install -r requirements.txt

# Minute 10-15: Verify template works
pytest  # Should pass all tests
uvicorn src.main:app --reload  # Start service

# Minute 15-20: Test endpoints
curl http://localhost:8000/health  # Verify working
curl http://localhost:8000/capabilities

# Minute 20-30: Read mission
# Open MISSION_SPEC.md
# Read requirements
# Understand pre-written prompts
```

**✅ Checkpoint:** Template running, mission understood
**⏱️ Time spent:** 30 minutes

---

### **Hour 0:30-2:00 - AI Builds the Service** ⏱️ **60-90 minutes**

**What you do (mostly copy/paste):**

#### **0:30-0:45 (15 min) - Prompt 1: Initial Setup**
```
1. Open Gemini/Cursor/Claude
2. Copy Prompt 1 from MISSION_SPEC.md
3. Paste into AI
4. Copy generated code to src/main.py
5. Run: pytest
6. Fix any errors with AI
```

#### **0:45-1:00 (15 min) - Prompt 2: Core Integration**
```
1. Copy Prompt 2 from spec
2. Paste into AI
3. Copy generated code
4. Run: pytest
5. Verify with curl
```

#### **1:00-1:15 (15 min) - Prompt 3: Additional Features**
```
1. Copy Prompt 3 from spec
2. Paste into AI
3. Copy generated code
4. Run: pytest
5. Test manually
```

#### **1:15-1:30 (15 min) - Prompt 4: Test Generation**
```
1. Copy Prompt 4 from spec
2. AI generates tests
3. Copy to tests/ folder
4. Run: pytest --cov=src
5. Should see >80% coverage
```

#### **1:30-2:00 (30 min) - Polish & Final Tests**
```
1. Ask AI: "Review this code for issues"
2. Fix any problems
3. Run full test suite
4. Test all endpoints manually
5. Check logs for errors
```

**✅ Checkpoint:** Service working, all tests passing
**⏱️ Time spent:** 60-90 minutes (AI does most work)

---

### **Hour 2:00-2:30 - Verification & Submission** ⏱️ **30 minutes MAX**

#### **2:00-2:10 (10 min) - Generate Documentation**
```
Ask AI:
"Generate HANDOFF.md for this service. Include:
- Implementation summary
- Key features used
- Technologies (FastAPI, SQLAlchemy, etc.)
- How to test
- Known limitations"

Copy output to HANDOFF.md
Review for accuracy
```

#### **2:10-2:20 (10 min) - Security Check**
```bash
# Check for secrets
grep -rn "password\|secret\|key\|token" src/ --include="*.py"
# Should only find variable NAMES, not values

# Verify .env not in repo
git status | grep .env
# Should show nothing (gitignored)

# Verify env.example has placeholders
cat env.example | grep -i secret
# Should show "your-secret-here" not real values
```

#### **2:20-2:30 (10 min) - Submit**
```bash
# Final commit
git add .
git commit -m "Complete Service #16 - [Feature Name]"

# Create GitHub repo
# Go to github.com/new
# Create public repo: service-16-yourname

# Push
git remote add origin https://github.com/yourusername/service-16-yourname.git
git push -u origin main

# Reply to Coordinator
"✅ Service #16 complete
Repository: https://github.com/yourusername/service-16-yourname
All tests passing. Ready for review."
```

**✅ Checkpoint:** Submitted to Coordinator
**⏱️ Total time spent:** 2-3 hours

---

## 🔍 **VERIFICATION PHASE (Not You - Verifier Does This)**

### **Hour 2:30-3:00 - Verifier Review** ⏱️ **20-30 minutes**

**What verifier does:**
```bash
# Clone and test (10 min)
git clone https://github.com/apprentice/service-16-yourname
cd service-16-yourname
pip install -r requirements.txt
pytest -v

# Manual endpoint testing (5 min)
python src/main.py &
curl http://localhost:8000/health
curl http://localhost:8000/capabilities
curl -X POST http://localhost:8000/message -d '{"test":"data"}'

# AI code review (5 min)
# Paste code into Claude: "Review this for security and quality issues"

# Security check (5 min)
grep -rn "password\|secret" src/
git log -p | grep -i secret

# Decision (2 min)
# PASS / NEEDS REVISION / FAIL
```

**✅ Checkpoint:** PASS decision
**⏱️ Elapsed:** Hour 3 from start

---

## 🚀 **DEPLOYMENT PHASE (Coordinator Does This)**

### **Hour 3:00-3:30 - Deploy to Production** ⏱️ **20-30 minutes**

**What coordinator does:**
```bash
# Clone approved repo (2 min)
git clone https://github.com/apprentice/service-16-yourname
cd service-16-yourname

# Deploy to production server (15 min)
rsync -avz . root@198.54.123.234:/opt/fpai/services/service-16/
ssh root@198.54.123.234
cd /opt/fpai/services/service-16/

# Set up systemd service (5 min)
cp service.example.service /etc/systemd/system/service-16.service
systemctl daemon-reload
systemctl start service-16
systemctl enable service-16

# Verify it's running (5 min)
systemctl status service-16
curl http://localhost:8000/health
# Check Registry shows service registered
```

**✅ Checkpoint:** Service LIVE in production
**⏱️ Total elapsed:** 3-4 hours from mission post

---

## 📊 **COMPLETE TIMELINE BREAKDOWN**

| Phase | Who | Work Time | Elapsed |
|-------|-----|-----------|---------|
| **Setup** | You | 30 min | Hour 0-0.5 |
| **Build with AI** | You | 60-90 min | Hour 0.5-2 |
| **Submit** | You | 30 min | Hour 2-2.5 |
| **Verify** | Verifier | 20 min | Hour 2.5-3 |
| **Deploy** | Coordinator | 20 min | Hour 3-3.5 |
| **TOTAL** | - | **~3 hours work** | **3-4 hours elapsed** |

---

## ⚡ **SPEED TARGETS**

### **Your Personal Goals:**

**Aggressive (AI Expert):**
- Setup: 20 minutes
- Build: 60 minutes
- Submit: 20 minutes
- **TOTAL: 1 hour 40 minutes**

**Target (Normal):**
- Setup: 30 minutes
- Build: 90 minutes
- Submit: 30 minutes
- **TOTAL: 2 hours 30 minutes**

**Acceptable (First Time):**
- Setup: 45 minutes
- Build: 120 minutes
- Submit: 45 minutes
- **TOTAL: 3 hours 30 minutes**

### **End-to-End Targets:**

| Scenario | Timeline | Requirements |
|----------|----------|--------------|
| **Speed Run** | **3 hours** | Everyone online, no issues, AI expert |
| **Target** | **4-5 hours** | Normal conditions, some async delay |
| **Same Day** | **6-8 hours** | Verifier/deploy queue, but same day |
| **Max** | **24 hours** | Overnight review, next morning deploy |

---

## 🎯 **OPTIMIZATION TIPS**

### **To Hit 3-Hour Target:**

1. **Pre-read MISSION_SPEC** before claiming (understand requirements first)
2. **Use Gemini** for speed (unlimited, fast responses)
3. **Copy prompts exactly** (don't improvise - spec prompts are optimized)
4. **Test after every prompt** (catch issues immediately)
5. **Use multiple AIs** (Gemini generates → Claude reviews)
6. **Don't overthink** (if tests pass, it's good enough)
7. **Ask AI to generate docs** (HANDOFF.md, README updates)

### **Time Wasters to Avoid:**

- ❌ **Reading all docs first** (reference as needed instead)
- ❌ **Manual coding** (AI does this faster - use the prompts!)
- ❌ **Perfectionism** (>80% coverage is enough)
- ❌ **Debugging alone** (ask AI for help immediately)
- ❌ **Writing docs manually** (AI generates these)

---

## 📈 **REALISTIC EXPECTATIONS**

### **First Mission:**
- Expect: **3-4 hours** (learning the flow)
- Some confusion is normal
- Ask questions early

### **Second Mission:**
- Expect: **2-3 hours** (flow is familiar)
- Faster with experience
- Know which AI to use when

### **Third+ Mission:**
- Expect: **1.5-2 hours** (you're efficient now)
- Can hit speed run targets
- Help other apprentices

---

## 🏆 **LEADERBOARD CONCEPT**

**Track your personal bests:**
```
Mission #1: 3h 45m (First time)
Mission #2: 2h 30m (Getting faster)
Mission #3: 1h 50m (Speed run!)
```

**Share your time with Coordinator - fast apprentices get priority on next missions!**

---

## ⏱️ **HOUR-BY-HOUR CHECKLIST**

**Print this and check off as you go:**

### **Hour 1:**
- [ ] Mission claimed (min 0)
- [ ] Template copied (min 5)
- [ ] Dependencies installed (min 10)
- [ ] Template verified working (min 15)
- [ ] Mission spec read (min 30)
- [ ] Prompt 1 executed (min 45)
- [ ] Tests passing (min 60)

### **Hour 2:**
- [ ] Prompt 2 executed (min 75)
- [ ] Prompt 3 executed (min 90)
- [ ] Prompt 4 (tests) executed (min 105)
- [ ] All tests passing >80% coverage (min 120)

### **Hour 3:**
- [ ] HANDOFF.md generated (min 130)
- [ ] Security check passed (min 140)
- [ ] Pushed to GitHub (min 150)
- [ ] Submitted to Coordinator (min 160)

**If you're past these times, you're behind pace. Ask for help!**

---

## 🚨 **IF YOU'RE STUCK (Emergency Timeouts)**

**Rule:** If stuck on one thing for >15 minutes, GET HELP

**Stuck on setup?** (Hour 0-0.5)
- Ask in Discord: "Setup issue: [describe]"
- Expected response: <5 minutes

**Stuck on AI prompt?** (Hour 0.5-2)
- Try different AI (Gemini → Claude)
- Ask AI: "This isn't working: [error]. Fix it."
- If still stuck after 2 tries → Ask Coordinator

**Tests failing?** (Any time)
- Copy error to AI: "Fix this test failure: [error]"
- If AI can't fix after 2 tries → Ask Coordinator

**NEVER spend >30 minutes stuck on one issue!**

---

## 🎉 **SUCCESS METRICS**

**You're doing great if:**
- ✅ Submitted in <3 hours (speed run)
- ✅ Submitted in <4 hours (target)
- ✅ All tests passing
- ✅ No security issues
- ✅ Verifier approves first try

**You need more practice if:**
- ⚠️ Took >5 hours (but still acceptable)
- ⚠️ Multiple revision requests
- ⚠️ Security issues found

**Get help immediately if:**
- 🚨 Taking >6 hours
- 🚨 Completely stuck
- 🚨 Tests won't pass after AI help

---

**Remember: With AI doing the heavy lifting, 2-3 hours is totally achievable. Use the prompts, test frequently, submit fast!** 🚀

