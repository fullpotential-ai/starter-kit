from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "active", "service": "simple-service"}

@app.get("/capabilities")
async def capabilities():
    return {"features": [], "udc_version": "1.0"}

@app.get("/state")
async def state():
    return {"status": "active"}

@app.post("/message")
async def message(msg: dict):
    return {"received": True}

