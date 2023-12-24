from api import pkg
from api.pc.shemas import PCSchemaAdd, PCSchema
from api.utils.unitofwork import IUnitOfWork


class PCService:
    @staticmethod
    async def add_pc(uow: IUnitOfWork, pc: PCSchemaAdd) -> PCSchema:
        new_pc = await pkg.assembly_pc(pc)
        pc_dict = new_pc.model_dump()
        async with uow:
            pc_id = await uow.pc.add_one(data=pc_dict)
            new_pc = await uow.pc.find_one(id=pc_id)
            await uow.commit()
            return new_pc
