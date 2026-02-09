from fastapi import FastAPI
from sqlalchemy import text

from app.db.session import engine
from app.core.config import settings
from app.api.routes import notes
from app.db.session import engine
from app.db.base import Base

app = FastAPI(title=settings.app_name)

app.include_router(notes.router)


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "env": settings.env,
    }
    
@app.get("/health/db")
async def db_health():
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return {"database": "ok"}
    except Exception as e:
        return {"database": "down", "error": str(e)}
