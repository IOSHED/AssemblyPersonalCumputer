from abc import ABC, abstractmethod
from typing import Type

from api.pc.repository import PCRepository, ComponentRepository, TypeComponentRepository
from api.db.db import async_session_maker


class IUnitOfWork(ABC):
    # Set tree repositories
    pc: Type[PCRepository]
    component: Type[ComponentRepository]
    type_component: Type[TypeComponentRepository]

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        # Set tree repositories
        self.pc = PCRepository(self.session)
        self.component = ComponentRepository(self.session)
        self.type_repository = ComponentRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
