from api.componet.shemas import TypeComponentSchemaAdd, ComponentSchemaAdd
from api.utils.unitofwork import IUnitOfWork


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
