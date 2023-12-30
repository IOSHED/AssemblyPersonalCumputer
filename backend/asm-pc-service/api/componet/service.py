from __future__ import annotations

from api.componet.shemas import ComponentSchemaAdd
from api.utils.dependencies import UOWDep


class ComponentService:
    @staticmethod
    async def add_component(uow: UOWDep, component: ComponentSchemaAdd) -> int:
        component_dict = component.model_dump()
        async with uow:
            print(component_dict)
            component_id = await uow.component.add_one(data=component_dict)
            await uow.commit()
            return component_id
