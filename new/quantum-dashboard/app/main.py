from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import os
from contextlib import asynccontextmanager

from app.database import connect_to_mongo, close_mongo_connection
from app.utils.redis_client import redis_client
from app.routers import auth, capsules, quantum, users, chat, websocket, sse  # <-- import sse router
from app.config import settings

# Rate limiting
limiter = Limiter(key_func=get_remote_address)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    await redis_client.connect()
    yield
    # Shutdown
    await close_mongo_connection()
    await redis_client.disconnect()

# Create FastAPI app
app = FastAPI(
    title="Quantum Dashboard API with Real-time Chat",
    description="Enhanced backend API with user interaction and real-time chat functionality",
    version="2.0.0",
    lifespan=lifespan
)

# Add middleware
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for demo/testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware, 
    allowed_hosts=settings.ALLOWED_HOSTS
)

# Add rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Include routers
app.include_router(auth.router)
app.include_router(capsules.router)
app.include_router(quantum.router)
app.include_router(users.router)
app.include_router(chat.router)
app.include_router(websocket.router)
app.include_router(sse.router)  # <-- add sse router


@app.get("/")
@limiter.limit("100/minute")
async def root(request: Request):
    return {
        "message": "Enhanced Quantum Dashboard API",
        "version": "2.0.0",
        "status": "operational",
        "features": ["real-time chat", "capsule sharing", "user connections"],
        "quantum_state": "entangled"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "quantum_coherence": "stable",
        "temporal_integrity": "maintained",
        "chat_system": "active",
        "redis_connection": "established"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )