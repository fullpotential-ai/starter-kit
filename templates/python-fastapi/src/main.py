"""
Full Potential AI Service Template
UDC-compliant FastAPI service

This template implements all 5 required UDC endpoints.
Customize the SERVICE_INFO and add your business logic below.
"""
from fastapi import FastAPI, HTTPException
import time
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Full Potential Service",
    version="1.0.0",
    description="UDC-compliant service template"
)

# ============================================================================
# SERVICE CONFIGURATION - CUSTOMIZE THIS
# ============================================================================
SERVICE_INFO = {
    "id": 0,                      # Will be assigned by Registry when you register
    "name": "template-service",   # 👈 CHANGE THIS to your service name
    "version": "1.0.0",           # Your service version
    "status": "active"            # Status: "active", "degraded", or "maintenance"
}

# Track when service started (for uptime calculation)
START_TIME = time.time()


# ============================================================================
# UDC ENDPOINTS - REQUIRED (Do not remove these!)
# ============================================================================

@app.get("/health")
async def health():
    """
    UDC Endpoint 1/5: Health Check
    Called every 30s by the orchestrator to verify service is alive.
    """
    return {
        "status": SERVICE_INFO["status"],
        "service": SERVICE_INFO["name"],
        "uptime": int(time.time() - START_TIME),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


@app.get("/capabilities")
async def capabilities():
    """
    UDC Endpoint 2/5: Capabilities
    Declares what this service can do and what it needs.
    
    👉 CUSTOMIZE: Update 'features' and 'dependencies' lists below
    """
    return {
        "service": SERVICE_INFO["name"],
        "version": SERVICE_INFO["version"],
        "features": [],          # 👈 ADD YOUR FEATURES: ["ocr", "image-analysis"]
        "dependencies": [],      # 👈 ADD DEPENDENCIES: ["storage-service", "database"]
        "udc_version": "1.0"
    }


@app.get("/state")
async def state():
    """
    UDC Endpoint 3/5: State
    Reports current operational status and load.
    """
    return {
        "uptime_seconds": int(time.time() - START_TIME),
        "status": SERVICE_INFO["status"]
    }


@app.get("/dependencies")
async def dependencies():
    """
    UDC Endpoint 4/5: Dependencies
    Lists what other services or systems this service requires.
    
    👉 CUSTOMIZE: List your required and optional dependencies
    """
    return {
        "required": [],   # 👈 Services you MUST have: ["postgresql", "redis"]
        "optional": []    # 👈 Services that are nice to have: ["cache-service"]
    }


@app.post("/message")
async def receive_message(message: dict):
    """
    UDC Endpoint 5/5: Message
    Receives work requests from other services.
    
    👉 CUSTOMIZE: Add your business logic here to handle different message types
    
    Expected message format:
    {
        "type": "command",           # or "query", "event"
        "payload": {                 # Your custom data
            "action": "do_something",
            "data": {...}
        },
        "trace_id": "uuid-string"    # For request tracing
    }
    """
    trace_id = message.get("trace_id", "unknown")
    logger.info(f"[{trace_id}] Received message: {message.get('type')}")
    
    # 👉 ADD YOUR LOGIC HERE
    # Example:
    # payload = message.get("payload", {})
    # action = payload.get("action")
    # if action == "process":
    #     result = process_data(payload)
    #     return {"received": True, "trace_id": trace_id, "result": result}
    
    # Default response (just acknowledges receipt)
    return {
        "received": True,
        "trace_id": trace_id
    }


# ============================================================================
# CUSTOM ENDPOINTS - ADD YOUR BUSINESS LOGIC BELOW
# ============================================================================

# Example custom endpoint (delete or modify as needed)
@app.get("/")
async def root():
    """Welcome endpoint"""
    return {
        "message": f"Welcome to {SERVICE_INFO['name']}",
        "version": SERVICE_INFO["version"],
        "docs": "/docs"
    }

# 👇 ADD YOUR CUSTOM ENDPOINTS HERE
# 
# @app.post("/your-endpoint")
# async def your_function(data: YourPydanticModel):
#     # Your business logic
#     return {"result": "success"}


# ============================================================================
# STARTUP/SHUTDOWN EVENTS (Optional)
# ============================================================================

@app.on_event("startup")
async def startup_event():
    """Called when service starts"""
    logger.info(f"🚀 {SERVICE_INFO['name']} v{SERVICE_INFO['version']} starting...")
    # 👉 ADD STARTUP TASKS: Connect to database, load models, etc.


@app.on_event("shutdown")
async def shutdown_event():
    """Called when service stops"""
    logger.info(f"🛑 {SERVICE_INFO['name']} shutting down...")
    # 👉 ADD CLEANUP TASKS: Close connections, save state, etc.

