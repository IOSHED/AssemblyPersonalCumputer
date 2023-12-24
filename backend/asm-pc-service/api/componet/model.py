from typing import Dict, Any

from sqlalchemy import Float, ForeignKey, String, JSON
from sqlalchemy.orm import Mapped, mapped_column

from api.db.db import Base
from api.componet.shemas import TypeComponentSchema, ComponentSchema


class Component(Base):
    __tablename__ = "component"

    id: Mapped[int] = mapped_column(primary_key=True)

    price: Mapped[float] = mapped_column(Float)
    user_rating_other_site: Mapped[float] = mapped_column(Float, default=0)
    user_rating: Mapped[float] = mapped_column(Float, default=0)
    type_component: Mapped[str] = mapped_column(ForeignKey("type_component.name"))

    name: Mapped[str] = mapped_column(String(255))
    specifications: Mapped[Dict[str, Any]] = mapped_column(JSON)

    def __repr__(self) -> str:
        return f"Component(id={self.id!r}, price={self.price!r}, name={self.name!r})"

    def to_read_model(self) -> ComponentSchema:
        return ComponentSchema(
            id=self.id,
            price=self.price,
            user_rating_other_site=self.user_rating_other_site,
            user_rating=self.user_rating,
            type_component=self.type_component,
            name=self.name,
            specifications=self.specifications,
        )


class TypeComponent(Base):
    __tablename__ = "type_component"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)

    def __repr__(self) -> str:
        return f"TypeComponent(name={self.name!r})"

    def to_read_model(self) -> TypeComponentSchema:
        return TypeComponentSchema(
            id=self.id,
            name=self.name,
        )
