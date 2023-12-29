from typing import Any, List

from fastapi import APIRouter

from api.componet.service import TypeComponentService
from api.componet.shemas import TypeComponentSchema, TypeComponentSchemaChange, TypeComponentSchemaAdd, \
    TypeComponentSchemaDelete
from api.utils.dependencies import UOWDep


router = APIRouter()


@router.post("/all_type_components")
async def create_all_type_components(uow: UOWDep) -> Any:
    try:
        await TypeComponentService.create_type_components(uow)
    except Exception as err:
        return {"type_error": "Unknown Error", "error": err}
    return None


@router.delete("/all_type_components")
async def delete_all_type_components(uow: UOWDep) -> Any:
    try:
        await TypeComponentService.delete_type_components(uow)
    except Exception as err:
        return {"type_error": "Unknown Error", "error": err}
    return None


@router.get("/all_type_components", response_model=List[TypeComponentSchema])
async def get_all_type_components(uow: UOWDep) -> Any:
    try:
        type_components = await TypeComponentService.get_all_type_components(uow)
    except Exception as err:
        return {"type_error": "Unknown Error", "error": err}
    return type_components


@router.get("/type_component", response_model=TypeComponentSchema)
async def get_type_component(uow: UOWDep, type_components_id: int) -> Any:
    try:
        type_component = await TypeComponentService.get_type_component(uow, type_components_id)
    except Exception as err:
        return {"type_error": "Unknown Error", "error": err}
    return type_component


@router.patch("/type_component", response_model=TypeComponentSchema)
async def patch_type_component(
        uow: UOWDep,
        type_components_id: int,
        change_components: TypeComponentSchemaChange,
) -> Any:
    try:
        type_component = await TypeComponentService.patch_type_component(uow, type_components_id, change_components)
    except Exception as err:
        return {"type_error": "Unknown Error", "error": err}
    return type_component


@router.post("/type_component", response_model=TypeComponentSchema)
async def create_type_component(
        uow: UOWDep,
        new_type_components: TypeComponentSchemaAdd,
) -> Any:
    try:
        type_component = await TypeComponentService.add_type_component(uow, new_type_components)
    except Exception as err:
        return {"type_error": "Unknown Error", "error": err}
    return type_component


@router.delete("/type_component")
async def delete_type_component(
        uow: UOWDep,
        type_component_delete: TypeComponentSchemaDelete,
) -> Any:
    try:
        type_component = await TypeComponentService.delete_type_component(uow, type_component_delete)
    except Exception as err:
        return {"type_error": "Unknown Error", "error": err}
    return type_component
