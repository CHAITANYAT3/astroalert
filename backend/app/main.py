import os
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from app.ws.orbit_stream import orbit_streamer
from app.api.routes import router as api_router
from app.database import engine, Base

app = FastAPI(title="AstroAlert API")

# ✅ Create DB tables on startup
Base.metadata.create_all(bind=engine)

# ✅ Secure CORS configuration
origins = [os.getenv("ALLOWED_ORIGINS", "https://astroalert.netlify.app")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Health check route for testing
@app.get("/")
def health_check():
    return {"status": "astroalert-api is running"}

# ✅ Include REST API routes
app.include_router(api_router, prefix="/api")

# ✅ WebSocket endpoint
@app.websocket("/ws/orbits")
async def websocket_endpoint(websocket: WebSocket):
    await orbit_streamer(websocket)
