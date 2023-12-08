from api.pc.model import PC
from api.utils.repository import SQLAlchemyRepository


class PCRepository(SQLAlchemyRepository):
    model = PC
