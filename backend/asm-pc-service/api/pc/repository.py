from api.pc.model import PC, Component, TypeComponent
from api.utils.repository import SQLAlchemyRepository


class PCRepository(SQLAlchemyRepository):
    model = PC


class ComponentRepository(SQLAlchemyRepository):
    model = Component


class TypeComponentRepository(SQLAlchemyRepository):
    model = TypeComponent

