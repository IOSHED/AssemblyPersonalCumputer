from api.assembly_pc.shemas import PCSchemaAdd
from api.utils.unitofwork import IUnitOfWork


class AssemblyPCService:
    @staticmethod
    async def add_pc(uow: IUnitOfWork, pc: PCSchemaAdd) -> int:
        pc_dict = pc.model_dump()
        async with uow:
            pc_id = await uow.assembly_pc.add_one(pc_dict)
            await uow.commit()
            return pc_id
