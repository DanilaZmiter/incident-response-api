from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from app.core.config import settings


class DBHelper:
    def __init__(self):
        self.engine = create_async_engine(settings.db.db_url)
        self.session = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False
        )

    @property
    async def get_session(self):
        yield self.session
