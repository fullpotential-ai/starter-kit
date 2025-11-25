# 🔧 Lesson 2: Set Up Your Development Environment

> **Time:** 15 minutes  
> **Goal:** Get your computer ready to build Services and create your first project

---

## What You'll Do

By the end of this lesson, you'll have:
- ✅ All required tools installed
- ✅ The template copied to your project folder
- ✅ Your development environment configured
- ✅ A working Service running locally

---

## 📋 Prerequisites Check

Before starting, verify you have these installed:

```bash
# Check Python version (need 3.11+)
python --version
# or
python3 --version

# Check pip
pip --version

# Check Docker
docker --version

# Check Git
git --version
```

### Don't Have These?

| Tool | Download Link | Why You Need It |
|------|--------------|-----------------|
| **Python 3.11+** | [python.org/downloads](https://www.python.org/downloads/) | Your Services run on Python |
| **pip** | Comes with Python | Installs Python packages |
| **Docker** | [docker.com/get-started](https://www.docker.com/get-started) | Containers for deployment |
| **Git** | [git-scm.com](https://git-scm.com/) | Version control |

---

## 🚀 Step-by-Step Setup

### Step 1: Choose Your Project Location

Decide where you want to build your Service:

```bash
# Example: Create a workspace folder
mkdir ~/fullpotential-services
cd ~/fullpotential-services
```

---

### Step 2: Copy the Template

From the `starter-kit` folder, copy the template to your new project:

```bash
# If you're in the starter-kit folder:
cp -r templates/python-fastapi ../my-first-service
cd ../my-first-service

# Or if you're elsewhere, use full path:
cp -r /path/to/starter-kit/templates/python-fastapi ./my-first-service
cd my-first-service
```

**What you just did:**  
Copied a production-ready template with all 5 UDC endpoints already implemented!

---

### Step 3: Set Up Python Environment (Recommended)

Create an isolated Python environment for this project:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# You should see (venv) in your terminal prompt
```

**Why?**  
Keeps your project dependencies separate from other Python projects.

---

### Step 4: Install Dependencies

```bash
# Make sure you're in your service folder
pwd  # Should show: .../my-first-service

# Install all required packages
pip install -r requirements.txt

# This installs: FastAPI, Pydantic, pytest, etc.
```

**Wait for installation to complete...** (1-2 minutes)

---

### Step 5: Configure Environment Variables

```bash
# Copy the environment template
cp env.example .env

# Open .env in your editor
nano .env
# or
code .env  # if you have VS Code
```

**Edit the `.env` file:**

```bash
# Change these values
SERVICE_NAME=my-first-service      # ← Your service name
SERVICE_ID=0                       # ← Will be assigned by Coordinator
REGISTRY_URL=https://registry.example.com  # ← Will be provided
JWT_SECRET=your-secret-here        # ← Will be provided
LOG_LEVEL=INFO                     # ← Keep as INFO for now
```

**For local development:**  
The placeholder values are fine for now. When you're ready to deploy, your Coordinator will provide real values.

---

### Step 6: Verify Installation

Test that everything is set up correctly:

```bash
# Run the tests
pytest

# You should see:
# tests/test_udc.py::test_health PASSED
# tests/test_udc.py::test_capabilities PASSED
# tests/test_udc.py::test_state PASSED
# tests/test_udc.py::test_message PASSED
```

✅ **If all tests pass, your environment is ready!**

---

### Step 7: Start Your Service

```bash
# Start the development server
uvicorn src.main:app --reload

# You should see:
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     Started reloader process
```

**The `--reload` flag means:** The server automatically restarts when you change code.

---

### Step 8: Test Your Service is Working

**Open a new terminal** (keep the server running in the first one) and test:

```bash
# Test the health endpoint
curl http://localhost:8000/health

# Expected response:
# {
#   "status": "active",
#   "service": "template-service",
#   "uptime": 5,
#   "timestamp": "2023-10-27T10:00:00Z"
# }
```

✅ **If you see JSON, congratulations! Your Service is running!**

---

### Step 9: View Interactive Docs

FastAPI automatically creates API documentation for you.

**Open your browser and visit:**
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

**Try it out:**
1. Click on `/health` endpoint
2. Click "Try it out"
3. Click "Execute"
4. See the response!

---

## 📁 Your Project Structure

After setup, your folder should look like this:

```
my-first-service/
├── venv/                  ← Python virtual environment (gitignored)
├── src/
│   ├── main.py           ← Your service code (start here!)
│   ├── config.py         ← Configuration management
│   └── udc/              ← UDC protocol implementations
├── tests/
│   ├── __init__.py
│   └── test_udc.py       ← Pre-written tests
├── .env                  ← Your secrets (gitignored - NEVER commit!)
├── env.example           ← Template for .env
├── .gitignore           ← What Git should ignore
├── Dockerfile            ← For Docker deployment
├── requirements.txt      ← Python dependencies
└── README.md            ← Template documentation
```

---

## 🎯 Quick Command Reference

```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install/update dependencies
pip install -r requirements.txt

# Run development server
uvicorn src.main:app --reload

# Run tests
pytest

# Run tests with coverage
pytest --cov=src

# Build Docker image
docker build -t my-service .

# Stop the server
# Press CTRL+C in the terminal running uvicorn
```

---

## ✅ Setup Checklist

Before moving to the next lesson, verify:

- [ ] Python 3.11+ installed and working
- [ ] Virtual environment created and activated
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created from `env.example`
- [ ] Tests pass (`pytest`)
- [ ] Service runs (`uvicorn src.main:app --reload`)
- [ ] Can access http://localhost:8000/health
- [ ] Interactive docs work at http://localhost:8000/docs

---

## 🐛 Troubleshooting

### "python: command not found"
```bash
# Try python3 instead
python3 --version

# Or install Python from python.org
```

### "Permission denied" when installing packages
```bash
# Use virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Or install with --user flag
pip install --user -r requirements.txt
```

### "Port 8000 already in use"
```bash
# Find and kill the process
lsof -ti:8000 | xargs kill -9

# Or use a different port
uvicorn src.main:app --reload --port 8001
```

### Tests are failing
```bash
# Make sure service is NOT running when you test
# Tests start their own test server

# Kill any running uvicorn:
pkill -f uvicorn

# Then run tests again:
pytest -v
```

### "Module not found" errors
```bash
# Make sure you're in the right directory
pwd  # Should show your project folder

# Make sure dependencies are installed
pip install -r requirements.txt

# Make sure virtual environment is activated
# You should see (venv) in your prompt
```

### Docker commands not working
```bash
# Make sure Docker Desktop is running
docker ps

# If Docker isn't running, start Docker Desktop
```

---

## 💡 Development Tips

### Use an IDE or Editor

**Recommended editors:**
- **VS Code** - Free, great Python support
- **PyCharm** - Powerful Python IDE
- **Sublime Text** - Lightweight
- **Vim/Neovim** - For terminal lovers

### Install Python Extensions

For VS Code:
1. Open Extensions (Ctrl+Shift+X)
2. Install "Python" by Microsoft
3. Install "Pylance" for better IntelliSense

### Enable Auto-Save

Your development server auto-reloads when you save files. Enable auto-save in your editor for a smooth workflow.

### Keep Two Terminals Open

**Terminal 1:** Running server (`uvicorn src.main:app --reload`)  
**Terminal 2:** For testing (`curl`, `pytest`, etc.)

---

## 🎓 What's Next?

Your environment is ready! Now it's time to understand the code and customize it for your needs.

**Next Lesson:** `03_BUILD_YOUR_SERVICE.md`  
You'll learn how to modify the template and add your business logic.

---

## 📝 Notes for Your Future Self

```bash
# Save these commands somewhere handy

# Start working on your service:
cd ~/fullpotential-services/my-first-service
source venv/bin/activate
uvicorn src.main:app --reload

# Test your changes:
pytest -v

# Build for production:
docker build -t my-service:1.0 .
docker run -p 8000:8000 my-service:1.0
```

---

**Environment ready!** Move to the next lesson: `03_BUILD_YOUR_SERVICE.md`

