from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
import asyncpg

from app.core.config import settings

from app.api.routers.producers import router as producers_router
from app.api.routers.farms import router as farms_router
from app.api.routers.farm_crops import router as farm_crops_router
from app.api.routers.dashboard import router as dashboard_router

app = FastAPI(title="Brain AG - Backend", version="0.3.0")

if settings.cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

Instrumentator().instrument(app).expose(app, endpoint="/metrics")

@app.get("/health", tags=["health"])
async def health():
    dsn = settings.database_url.replace("postgresql+psycopg", "postgresql", 1)
    try:
        conn = await asyncpg.connect(dsn)
        await conn.execute("SELECT 1;")
        await conn.close()
        return {"status": "ok", "db": "up", "env": settings.app_env}
    except Exception as e:
        return {"status": "degraded", "db": "down", "error": str(e)[:300]}

app.include_router(producers_router, prefix="/producers", tags=["producers"])
app.include_router(farms_router, prefix="/farms", tags=["farms"])
app.include_router(farm_crops_router, prefix="/farm-crops", tags=["farm-crops"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["dashboard"])
