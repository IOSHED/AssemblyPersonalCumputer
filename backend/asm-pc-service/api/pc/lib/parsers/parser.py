from abc import ABC, abstractmethod
from typing import Any


class Parser(ABC):
    @abstractmethod
    async def parse(self) -> Any:
        ...
