from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from app.ws.orbit_stream import orbit_streamer
from app.api.routes import router as api_router
from app.database import engine, Base

app = FastAPI(title="AstroAlert API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api")

@app.websocket("/ws/orbits")
async def websocket_endpoint(websocket: WebSocket):
    await orbit_streamer(websocket)

@app.get("/")
async def root():
    return {"message": "Welcome to AstroAlert API"}
