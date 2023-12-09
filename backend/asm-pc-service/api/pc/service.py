from api.pc import lib
from api.pc.shemas import PCSchemaAdd, ComponentSchemaAdd, TypeComponentSchemaAdd, PCSchema
from api.utils.unitofwork import IUnitOfWork


class PCService:
    @staticmethod
    async def add_pc(uow: IUnitOfWork, pc: PCSchemaAdd) -> PCSchema:
        new_pc = await lib.assembly_pc(pc)
        pc_dict = new_pc.model_dump()
        async with uow:
            pc_id = await uow.pc.add_one(data=pc_dict)
            new_pc = await uow.pc.find_one(id=pc_id)
            await uow.commit()
            return new_pc


class ComponentService:
    @staticmethod
    async def add_component(uow: IUnitOfWork, component: ComponentSchemaAdd) -> int:
        component_dict = component.model_dump()
        async with uow:
            print(component_dict)
            component_id = await uow.component.add_one(data=component_dict)
            await uow.commit()
            return component_id


class TypeComponentService:
    @staticmethod
    async def add_type_component(uow: IUnitOfWork, type_component: TypeComponentSchemaAdd) -> int:
        type_component_dict = type_component.model_dump()
        async with uow:
            type_component_id = await uow.type_component.add_one(data=type_component_dict)
            await uow.commit()
            return type_component_id
