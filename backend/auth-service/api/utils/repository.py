from abc import ABC, abstractmethod

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def delete_one(self, filter_id: int):
        ...

    @abstractmethod
    async def find_one(self, **filter_by):
        ...


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def delete_one(self, filter_id: int):
        stmt = delete(self.model).filter_by(id=filter_id)
        await self.session.execute(stmt)
        await self.session.commit()

    async def find_one(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        return res
