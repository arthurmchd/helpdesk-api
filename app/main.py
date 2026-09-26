from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import engine


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield
    # Fecha as conexões do pool quando o servidor desliga.
    await engine.dispose()


app = FastAPI(title="Helpdesk API", version="0.1.0", lifespan=lifespan)


@app.get("/health", tags=["health"])
async def health() -> dict[str, str]:
    return {"status": "ok"}
