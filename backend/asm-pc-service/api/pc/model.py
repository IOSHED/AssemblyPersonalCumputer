from typing import List

from sqlalchemy import ForeignKey, Column, Table, Float
from sqlalchemy.orm import mapped_column, Mapped, relationship

from api.pc.shemas import PCSchema
from api.componet.model import Component
from api.db.db import Base


association_table_pc_component = Table(
    "association_table_pc_component",
    Base.metadata,
    Column("pc_id", ForeignKey("pc.id")),
    Column("component_id", ForeignKey("component.id")),
)


class PC(Base):
    __tablename__ = "pc"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float] = mapped_column(Float)
    components: Mapped[List["Component"]] = relationship(secondary=association_table_pc_component)

    def __repr__(self) -> str:
        return f"PC(id={self.id!r}, price={self.price!r})"

    def to_read_model(self) -> PCSchema:
        components = [component.to_read_model() for component in self.components]
        return PCSchema(
            id=self.id,
            price=self.price,
            components=components
        )
