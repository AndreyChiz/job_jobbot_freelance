import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import dbsettings
from models import UsersOrm, Base



class Database:

    def __init__(self, ):
        self.engine = create_async_engine(
            dbsettings.database_url_asyncpg
        )
        self.session_factory = async_sessionmaker(self.engine)

    async def create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def insert_data(self, data: list):
        async with self.session_factory() as session:
            # user = UsersOrm(user_id=123, user_name='Феликс', user_keywords='бот, aiogram, доделать', user_notify=True)
            # user1 = UsersOrm(user_id=345, user_name='Халк', user_keywords='django, api', user_notify=False)
            session.add_all(data)
            await session.commit()


async def check():
    db = Database()
    await db.create_tables()
    await db.insert_data()


if __name__ == '__main__':
    asyncio.run(check())
