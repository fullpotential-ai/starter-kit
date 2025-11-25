# 🔌 UDC Compliance Guide

> **The Bible:** This document defines the Universal Droplet Contract. Every Service MUST implement these endpoints.

---

## ⚠️ What is a 'Droplet'?

**A "Droplet" is NOT a server or VPS. It's an abstraction - a Service that speaks the UDC protocol.**

### Simple Analogy
Think of it like this:
- **HTTP** is the protocol for web browsers to talk to web servers
- **UDC** is the protocol for Services to talk to each other

When we say "Service #16 is UDC-compliant," we mean:
✅ It implements 5 required HTTP endpoints
✅ It can register with the central Registry
✅ Other Services can discover and talk to it

**Your job:** Make your Service speak UDC by implementing these 5 endpoints.

---

## 5 Required Endpoints

**Every Service MUST implement these 5 endpoints.** No exceptions.

> 💡 **Tip:** The template already has these implemented. Just customize the responses with your Service's specific info.

### 1. Health Check
**GET** `/health`

**Purpose:** "Are you alive and working?"

The orchestrator pings this every 30 seconds. If you don't respond, you're marked as "down".

**Response Format:**
```json
{
  "status": "active",           // Must be "active" or "degraded"
  "service": "service-name",    // Your service's name
  "uptime": 12345,              // Seconds since service started
  "timestamp": "2023-10-27T10:00:00Z"  // Current UTC time
}
```

**Test it:**
```bash
curl http://localhost:8000/health
```

### 2. Capabilities
**GET** `/capabilities`

**Purpose:** "What can you do?"

Other Services call this to discover your features before sending you tasks.

**Response Format:**
```json
{
  "service": "service-name",              // Your service's name
  "version": "1.0.0",                     // Your service's version
  "features": ["image-processing", "ocr"], // List of things you can do
  "dependencies": ["storage-service"],     // Other Services you need
  "udc_version": "1.0"                    // Always "1.0" for now
}
```

**Example:**
If you're building an OCR service:
```json
{
  "service": "ocr-service",
  "version": "1.0.0",
  "features": ["text-extraction", "multi-language-support"],
  "dependencies": ["storage-service"],
  "udc_version": "1.0"
}
```

**Test it:**
```bash
curl http://localhost:8000/capabilities
```

### 3. State
**GET** `/state`

**Purpose:** "How are you doing right now?"

Returns real-time operational status and load.

**Response Format:**
```json
{
  "uptime_seconds": 12345,    // How long you've been running
  "status": "active",         // "active", "degraded", or "busy"
  "current_load": 0.5         // Optional: 0.0 to 1.0 (0% to 100%)
}
```

**Test it:**
```bash
curl http://localhost:8000/state
```

---

### 4. Dependencies
**GET** `/dependencies`

**Purpose:** "What do you need to run?"

Lists other Services or systems your Service requires.

**Response Format:**
```json
{
  "required": ["database", "storage-service"],  // Can't work without these
  "optional": ["cache-service"]                 // Nice to have, but not required
}
```

**Example:**
If your Service needs a database and optionally uses caching:
```json
{
  "required": ["postgresql"],
  "optional": ["redis-cache"]
}
```

**Test it:**
```bash
curl http://localhost:8000/dependencies
```

---

### 5. Message (The Work Endpoint)
**POST** `/message`

**Purpose:** "Here's a task for you to do."

This is where other Services send work to your Service.

**Request Format:**
```json
{
  "type": "command",              // Type of message (command, query, etc.)
  "payload": {                    // Your custom data goes here
    "action": "analyze",
    "image_id": "12345"
  },
  "trace_id": "uuid-string"       // For tracking this request across Services
}
```

**Response Format:**
```json
{
  "received": true,               // Acknowledge you got the message
  "trace_id": "uuid-string",      // Echo back the trace_id
  "result": {}                    // Optional: immediate results
}
```

**Example Implementation Pattern:**
```python
@app.post("/message")
async def receive_message(message: dict):
    trace_id = message.get("trace_id")
    payload = message.get("payload", {})
    
    # Do your work here
    result = process_task(payload)
    
    return {
        "received": True,
        "trace_id": trace_id,
        "result": result
    }
```

**Test it:**
```bash
curl -X POST http://localhost:8000/message \
  -H "Content-Type: application/json" \
  -d '{"type":"test", "payload":{}, "trace_id":"test-123"}'
```

---

## 🔐 Authentication Requirements

**All Service-to-Service communication is secured via JWT (JSON Web Tokens).**

### How It Works
1. Your Service receives a JWT token from the Coordinator when it registers
2. When calling other Services, include: `Authorization: Bearer <token>`
3. When receiving calls, validate the JWT signature

### Getting Your Credentials
Your Coordinator will provide:
- **Service ID:** Your unique number in the network
- **JWT Secret:** For signing/verifying tokens
- **Registry URL:** Where to register

**Never hardcode these!** Always load from environment variables.

```bash
# env.example
SERVICE_ID=42
JWT_SECRET=[PROVIDED BY COORDINATOR]
REGISTRY_URL=[PROVIDED BY COORDINATOR]
```

---

## 🔄 Registration Flow

**What happens when your Service starts:**

```
1. Your Service boots up
   ↓
2. Reads credentials from environment variables
   ↓
3. Contacts Registry at [PROVIDED BY COORDINATOR]
   ↓
4. Sends: "Hi, I'm Service #42, here are my capabilities"
   ↓
5. Registry responds: "Welcome! You're registered."
   ↓
6. Your Service sends heartbeat every 30 seconds
```

### Heartbeat Protocol
**Every 30 seconds**, your Service must ping the Registry to say "I'm still alive."

If you miss 3 heartbeats (90 seconds), the Registry marks you as "down" and stops routing traffic to you.

---

## ✅ Compliance Checklist

Before submitting your Service, verify:

### Endpoints
- [ ] `/health` returns JSON with status, uptime, timestamp
- [ ] `/capabilities` lists your features and dependencies
- [ ] `/state` shows current operational status
- [ ] `/dependencies` lists required and optional services
- [ ] `/message` accepts tasks and returns trace_id

### Response Quality
- [ ] All responses are valid JSON
- [ ] Field names match the schema exactly (case-sensitive)
- [ ] Timestamps are in ISO 8601 format with 'Z' suffix
- [ ] trace_id is echoed back in `/message` responses

### Error Handling
- [ ] Returns 404 for unknown endpoints
- [ ] Returns 422 for invalid input
- [ ] Returns 500 for internal errors (with generic message)
- [ ] Never exposes internal error details to clients

### Testing
- [ ] All 5 endpoints tested with `curl` or `httpx`
- [ ] Tests included in `tests/` folder
- [ ] `pytest` runs successfully

---

## 🧪 Quick Compliance Test

Run this to test all 5 endpoints at once:

```bash
# Health
curl http://localhost:8000/health

# Capabilities
curl http://localhost:8000/capabilities

# State
curl http://localhost:8000/state

# Dependencies
curl http://localhost:8000/dependencies

# Message
curl -X POST http://localhost:8000/message \
  -H "Content-Type: application/json" \
  -d '{"type":"test", "payload":{}, "trace_id":"test-123"}'
```

**✅ All 5 should return valid JSON with no errors.**

