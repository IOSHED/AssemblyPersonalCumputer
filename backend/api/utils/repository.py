from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self):
        ...

    @abstractmethod
    async def find_all(self):
        ...
