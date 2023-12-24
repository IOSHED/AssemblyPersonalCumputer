from __future__ import annotations

from api import config
from api.componet.shemas import TypeComponentSchemaAdd, ComponentSchemaAdd, TypeComponentSchemaChange, \
    TypeComponentSchemaDelete


class ComponentService:
    @staticmethod
    async def add_component(uow, component: ComponentSchemaAdd) -> int:
        component_dict = component.model_dump()
        async with uow:
            print(component_dict)
            component_id = await uow.component.add_one(data=component_dict)
            await uow.commit()
            return component_id


class TypeComponentService:
    @staticmethod
    async def add_type_component(uow, type_component: TypeComponentSchemaAdd) -> int:
        type_component_dict = type_component.model_dump()
        async with uow:
            type_component_id = await uow.type_component.add_one(data=type_component_dict)
            await uow.commit()
            return type_component_id

    @staticmethod
    def create_type_components(uow):
        async with uow:
            for name in config.TYPE_COMPONENTS:
                new_type_component = TypeComponentSchemaAdd(name=name).model_dump()
                await uow.type_component.add_one(data=new_type_component)
            await uow.commit()

    @staticmethod
    def delete_type_components(uow):
        async with uow:
            await uow.type_component.delete_all()
            await uow.commit()

    @staticmethod
    def delete_type_component(uow, type_component_delete: TypeComponentSchemaDelete):
        async with uow:
            await uow.type_component.delete_one(filter_by=type_component_delete.model_dump())
            await uow.commit()

    @staticmethod
    def patch_type_component(uow, type_components_id: int, change_components: TypeComponentSchemaChange):
        async with uow:
            await uow.type_component.edit_one(unit_id=type_components_id, data=change_components.model_dump())
            await uow.commit()

    @staticmethod
    def get_type_component(uow, type_components_id):
        async with uow:
            await uow.type_component.find_one(id=type_components_id)
            await uow.commit()

    @staticmethod
    def get_all_type_components(uow):
        async with uow:
            await uow.type_component.find_all()
            await uow.commit()
