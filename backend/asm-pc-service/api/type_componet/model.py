from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from api.db.db import Base
from api.type_componet.shemas import TypeComponentSchema


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
