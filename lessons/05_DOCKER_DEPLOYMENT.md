# 🐳 Lesson 5: Docker & Deployment

> **Time:** 10 minutes  
> **Goal:** Package your Service in a Docker container ready for production

---

## What You'll Do

By the end of this lesson, you'll have:
- ✅ Built a Docker image of your Service
- ✅ Tested the container locally
- ✅ Verified it's production-ready
- ✅ Understanding of how deployment works

---

## Why Docker?

### The Problem
```
Your Computer:
- Python 3.11
- Libraries installed
- Works perfectly! ✅

Production Server:
- Python 3.9
- Different libraries
- Nothing works! ❌
```

### The Solution: Docker
```
Docker Container:
- Packages everything together
- Same environment everywhere
- Works on any server! ✅
```

**Think of Docker like a shipping container:**  
Whatever you put inside stays the same, no matter where it goes.

---

## Step 1: Understand the Dockerfile (5 minutes)

Your template includes a pre-configured `Dockerfile`. Let's understand it:

```dockerfile
# Use Python 3.11 as the base
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for Docker caching)
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy your code into the container
COPY . .

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run when container starts
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**You usually don't need to modify this!** It's already configured correctly.

---

## Step 2: Build Your Docker Image (3 minutes)

### Build the Image

```bash
# Make sure you're in your service directory
pwd  # Should show: .../my-first-service

# Build the image
docker build -t my-service:1.0 .

# What happens:
# [1/5] FROM python:3.11-slim
# [2/5] WORKDIR /app
# [3/5] COPY requirements.txt
# [4/5] RUN pip install
# [5/5] COPY . .
# Successfully built abc123def456
```

**Name Format:** `service-name:version`
- Use lowercase with hyphens
- Version helps track changes
- Examples: `pdf-processor:1.0`, `ocr-service:2.1`

### Verify the Image

```bash
# List your Docker images
docker images

# You should see:
# REPOSITORY     TAG    IMAGE ID       CREATED         SIZE
# my-service     1.0    abc123def456   2 minutes ago   180MB
```

---

## Step 3: Run Your Container (2 minutes)

### Basic Run

```bash
# Run the container
docker run -p 8000:8000 my-service:1.0

# You should see:
# INFO:     Started server process
# INFO:     Uvicorn running on http://0.0.0.0:8000
```

**What `-p 8000:8000` means:**
- First 8000: Port on your computer
- Second 8000: Port inside container
- Maps container port to your machine

### Run in Background (Detached Mode)

```bash
# Run in background
docker run -d -p 8000:8000 --name my-service-instance my-service:1.0

# Returns container ID:
# abc123def456789...
```

**Useful flags:**
- `-d`: Run in background (detached)
- `--name`: Give container a friendly name
- `-p`: Map ports

---

## Step 4: Test the Running Container (3 minutes)

### Check Container Status

```bash
# List running containers
docker ps

# You should see:
# CONTAINER ID   IMAGE            STATUS         PORTS
# abc123def456   my-service:1.0   Up 2 minutes   0.0.0.0:8000->8000/tcp
```

### Test the Service

```bash
# Test health endpoint
curl http://localhost:8000/health

# Expected:
# {"status": "active", ...}
```

### View Container Logs

```bash
# See what's happening inside
docker logs my-service-instance

# Follow logs in real-time
docker logs -f my-service-instance

# Press Ctrl+C to stop following
```

### Enter the Container (Debugging)

```bash
# Open a shell inside the container
docker exec -it my-service-instance /bin/bash

# You're now inside! Look around:
ls
pwd
cat src/main.py

# Exit when done
exit
```

---

## Step 5: Pass Environment Variables (2 minutes)

### Using .env File

```bash
# Run with environment file
docker run -d -p 8000:8000 --env-file .env --name my-service my-service:1.0
```

### Using Individual Variables

```bash
docker run -d -p 8000:8000 \
  -e SERVICE_ID=42 \
  -e SERVICE_NAME=my-service \
  -e LOG_LEVEL=DEBUG \
  --name my-service \
  my-service:1.0
```

**Important:** In production, your Coordinator will provide real credentials.

---

## Step 6: Stop and Clean Up (1 minute)

### Stop Container

```bash
# Stop the container
docker stop my-service-instance

# Remove the container
docker rm my-service-instance
```

### Remove Image (if needed)

```bash
# Remove the image
docker rmi my-service:1.0
```

### Clean Up Everything

```bash
# Remove stopped containers
docker container prune

# Remove unused images
docker image prune

# Remove everything unused (careful!)
docker system prune -a
```

---

## ✅ Production Readiness Checklist

Before submitting your Service, verify:

### Docker Build
- [ ] `docker build` completes without errors
- [ ] Image size is reasonable (<500MB for simple services)
- [ ] No secrets baked into the image

### Container Run
- [ ] Container starts without errors
- [ ] Service responds on port 8000
- [ ] All 5 UDC endpoints work in container
- [ ] Logs show expected output (no errors)

### Environment Variables
- [ ] Service reads from environment variables
- [ ] No hardcoded secrets in code
- [ ] .env.example provided for reference

### Testing in Container
- [ ] `curl http://localhost:8000/health` works
- [ ] Custom functionality works same as local
- [ ] Container can be stopped and restarted cleanly

---

## 🐛 Troubleshooting

### "Cannot connect to Docker daemon"
```bash
# Start Docker Desktop
# Or on Linux:
sudo systemctl start docker
```

### "Port 8000 already in use"
```bash
# Stop existing container
docker stop $(docker ps -q --filter "publish=8000")

# Or use different port
docker run -p 8001:8000 my-service:1.0
```

### "No such file or directory" during build
```bash
# Make sure you're in the right directory
ls  # Should see: Dockerfile, src/, requirements.txt

# Check .dockerignore isn't excluding necessary files
cat .dockerignore
```

### Container exits immediately
```bash
# Check logs for errors
docker logs my-service-instance

# Common causes:
# - Python syntax error
# - Missing dependencies
# - Port already in use inside container
```

### Service works locally but not in Docker
```bash
# Common causes:
# 1. Using localhost instead of 0.0.0.0
#    Fix: CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0"]

# 2. Missing dependencies in requirements.txt
#    Fix: pip freeze > requirements.txt

# 3. Environment variables not passed
#    Fix: docker run --env-file .env ...
```

---

## 📋 Docker Command Cheat Sheet

```bash
# BUILD
docker build -t service-name:version .

# RUN
docker run -p 8000:8000 service-name:version
docker run -d -p 8000:8000 --name my-service service-name:version
docker run --env-file .env -p 8000:8000 service-name:version

# MANAGE
docker ps                          # List running containers
docker ps -a                       # List all containers
docker stop <container-id>         # Stop container
docker rm <container-id>           # Remove container
docker logs <container-id>         # View logs
docker logs -f <container-id>      # Follow logs
docker exec -it <container-id> /bin/bash  # Enter container

# IMAGES
docker images                      # List images
docker rmi <image-id>             # Remove image
docker image prune                # Remove unused images

# CLEANUP
docker stop $(docker ps -q)        # Stop all containers
docker container prune            # Remove stopped containers
docker system prune -a            # Remove everything unused
```

---

## 🚀 What Happens in Production?

### Your Journey So Far
```
1. You build locally
2. You test locally
3. You build Docker image
4. You test Docker container
```

### What Happens Next (handled by Coordinator)
```
5. Image pushed to registry (like Docker Hub)
6. Production server pulls your image
7. Container deployed with real credentials
8. Service registers with Registry
9. Service starts receiving real traffic
```

**You don't need to worry about steps 5-9 yet!**

---

## 💡 Best Practices

### 1. Keep Images Small
```dockerfile
# Use slim base images
FROM python:3.11-slim  # ✅ Good (150MB)
# Not
FROM python:3.11       # ❌ Big (900MB)
```

### 2. Layer Caching
```dockerfile
# Copy requirements first (caches if unchanged)
COPY requirements.txt .
RUN pip install -r requirements.txt
# Then copy code (changes more often)
COPY . .
```

### 3. Don't Run as Root (Advanced)
```dockerfile
# Add non-root user
RUN useradd -m appuser
USER appuser
```

### 4. Health Checks
```dockerfile
# Add health check to Dockerfile
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8000/health || exit 1
```

### 5. .dockerignore
Create `.dockerignore` to exclude files:
```
.env
__pycache__
*.pyc
.git
venv/
htmlcov/
.pytest_cache
```

---

## 🎓 What's Next?

Your Service is containerized and ready for deployment! Final step: submission.

**Next Lesson:** `06_SUBMISSION.md`  
You'll learn how to prepare and submit your Service to your Coordinator.

---

## 📚 Additional Resources

- Docker Documentation: [docs.docker.com](https://docs.docker.com/)
- Best Practices: [docs.docker.com/develop/dev-best-practices](https://docs.docker.com/develop/dev-best-practices/)
- Dockerfile Reference: [docs.docker.com/engine/reference/builder](https://docs.docker.com/engine/reference/builder/)

---

**Container ready?** Move to: `06_SUBMISSION.md`

