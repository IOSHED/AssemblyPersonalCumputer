from typing import Dict

from sqlalchemy import Integer, JSON
from sqlalchemy.orm import mapped_column, Mapped

from api.assembly_pc.shemas import PCSchema
from api.db.db import Base


class PC(Base):
    __tablename__ = "pc"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[int] = mapped_column(Integer)
    components: Mapped[Dict[str, str]] = mapped_column(JSON)

    def to_read_model(self) -> PCSchema:
        return PCSchema(
            id=self.id,
            price=self.price,
            components=self.components
        )
