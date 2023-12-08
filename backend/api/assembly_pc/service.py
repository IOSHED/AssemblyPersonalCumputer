from api.assembly_pc import lib
from api.assembly_pc.shemas import PCSchemaAdd
from api.utils.unitofwork import IUnitOfWork


class AssemblyPCService:
    @staticmethod
    async def add_pc(uow: IUnitOfWork, pc: PCSchemaAdd) -> int:
        new_pc = await lib.assembly_pc(pc)
        pc_dict = new_pc.model_dump()
        async with uow:
            pc_id = await uow.assembly_pc.add_one(data=pc_dict)
            new_pc = await uow.assembly_pc.find_one(id=pc_id)
            await uow.commit()
            return new_pc
