from api.componet.model import Component, TypeComponent
from api.utils.repository import SQLAlchemyRepository


class ComponentRepository(SQLAlchemyRepository):
    model = Component


class TypeComponentRepository(SQLAlchemyRepository):
    model = TypeComponent
