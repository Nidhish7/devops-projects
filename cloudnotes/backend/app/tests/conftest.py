import asyncio
import pytest

from app.db.base import Base
from app.db.session import engine


@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    async def init_models():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    asyncio.run(init_models())
