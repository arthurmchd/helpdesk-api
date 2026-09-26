from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config import settings

engine = create_async_engine(settings.database_url, echo=settings.sql_echo)

# expire_on_commit=False: depois do commit os objetos continuam utilizáveis.
# Com o padrão (True), ler um atributo após o commit dispararia uma query
# implícita, e em código async isso gera erro (MissingGreenlet).
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_session() -> AsyncIterator[AsyncSession]:
    """Dependência do FastAPI: uma sessão de banco por requisição."""
    async with SessionLocal() as session:
        yield session
