from abc import ABC, abstractmethod
from typing import List, Any

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        ...

    @abstractmethod
    async def find_all(self):
        ...

    @abstractmethod
    async def edit_one(self, unit_id: int, data: dict) -> int:
        ...

    @abstractmethod
    async def find_one(self, **filter_by):
        ...

    @abstractmethod
    async def delete_all(self):
        ...

    @abstractmethod
    async def delete_one(self, **filter_by):
        ...


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def edit_one(self, unit_id: int, data: dict) -> int:
        stmt = update(self.model).values(**data).filter_by(id=unit_id).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def find_all(self) -> List[Any]:
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def find_one(self, **filter_by) -> Any:
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = res.scalar_one().to_read_model()
        return res

    async def delete_all(self):
        stmt = delete(self.model)
        await self.session.execute(stmt)

    async def delete_one(self, **filter_by):
        stmt = delete(self.model).filter_by(**filter_by)
        await self.session.execute(stmt)
