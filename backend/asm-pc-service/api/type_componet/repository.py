from api.type_componet.model import TypeComponent
from api.utils.repository import SQLAlchemyRepository


class TypeComponentRepository(SQLAlchemyRepository):
    model = TypeComponent
