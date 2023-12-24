from typing import Any

from api.componet.service import ComponentService, TypeComponentService
from api.componet.shemas import ComponentSchemaAdd, TypeComponentSchemaAdd
from api.pc.urls import router
from api.utils.dependencies import UOWDep


@router.post("/component")
async def create_component(component_add: ComponentSchemaAdd, uow: UOWDep) -> Any:
    try:
        id_new_component = await ComponentService.add_component(uow, component_add)
    except Exception as err:
        return {"type_error": "Unknown Error", "error": err}
    return id_new_component


@router.post("/type_component")
async def create_type_component(type_component_add: TypeComponentSchemaAdd, uow: UOWDep) -> Any:
    try:
        id_new_type_component = await TypeComponentService.add_type_component(uow, type_component_add)
    except Exception as err:
        return {"type_error": "Unknown Error", "error": err}
    return id_new_type_component
