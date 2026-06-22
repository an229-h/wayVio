from fastapi import FastAPI
from routers import auth, devices, locations

app = FastAPI(title="Tracker API")

# Register your new routers here
app.include_router(auth.router)
app.include_router(devices.router)
app.include_router(locations.router)

# Keep your health check endpoint!
@app.get("/api/v1/health")
async def health_check():
    return {"status": "ok"}