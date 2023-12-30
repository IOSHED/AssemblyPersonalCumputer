from api.componet.model import Component
from api.utils.repository import SQLAlchemyRepository


class ComponentRepository(SQLAlchemyRepository):
    model = Component
