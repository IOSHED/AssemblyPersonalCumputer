from typing import Any

from fastapi import APIRouter

from api.pc.service import PCService, ComponentService, TypeComponentService
from api.pc.shemas import PCSchema, PCSchemaAdd, ComponentSchemaAdd, TypeComponentSchemaAdd
from api.utils.dependencies import UOWDep


router = APIRouter()

# TODO create a good except error
# TODO allow use create_component and create_type_component only the admin


@router.post("/", response_model=PCSchema)
async def assembly_pc(user_data_pc: PCSchemaAdd, uow: UOWDep) -> Any:
    try:
        new_pc = await PCService.add_pc(uow, user_data_pc)
    except Exception as err:
        return {"type_error": "Unknown Error", "error": err}
    return new_pc


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
