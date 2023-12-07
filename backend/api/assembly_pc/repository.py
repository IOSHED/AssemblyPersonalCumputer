from api.assembly_pc.model import PC
from api.utils.repository import SQLAlchemyRepository


class AssemblyPCRepository(SQLAlchemyRepository):
    model = PC
