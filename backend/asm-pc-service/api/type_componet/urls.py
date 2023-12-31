from __future__ import annotations

from typing import List, Any, Dict

from fastapi import HTTPException, APIRouter, Depends
from starlette import status

from api.type_componet.service import TypeComponentService
from api.type_componet.shemas import TypeComponentSchemaAdd, TypeComponentSchemaChange, TypeComponentSchemaDelete, \
    TypeComponentSchema
from api.utils.dependencies import UOWDep
from api.utils.users import get_active_user, get_superuser

router = APIRouter()


@router.post("/all_type_components", response_model=List[TypeComponentSchema], status_code=status.HTTP_201_CREATED)
async def create_all_type_components(
        uow: UOWDep,
        _user: Dict[str, Any] = Depends(get_superuser),
) -> List[TypeComponentSchema]:
    """
    Creates all the component types specified in config.py.

    Args:
        uow (UOWDep): The unit of work dependency.
        _user (Dict[str, Any]): Get current superuser.

    Returns:
        List[TypeComponentSchema]: Returns list new creating type components.

    Raises:
        HTTPException: If an internal server error occurs.
    """
    try:
        list_type_components_schema = await TypeComponentService.create_type_components(uow)
        if not list_type_components_schema:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No type components found")
        return list_type_components_schema
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.delete("/all_type_components", status_code=status.HTTP_200_OK)
async def delete_all_type_components(
        uow: UOWDep,
        _user: Dict[str, Any] = Depends(get_superuser),
):
    """
    Deletes all type components.

    Args:
        uow (UOWDep): The unit of work dependency.
        _user (Dict[str, Any]): Get current superuser.

    Returns:
        None

    Raises:
        HTTPException: If an internal server error occurs.
    """
    try:
        await TypeComponentService.delete_type_components(uow)
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.get("/all_type_components", response_model=List[TypeComponentSchema], status_code=status.HTTP_200_OK)
async def get_all_type_components(
        uow: UOWDep,
        _user: Dict[str, Any] = Depends(get_active_user),
) -> List[TypeComponentSchema]:
    """
    Retrieves all type components.

    Args:
        uow (UOWDep): The unit of work dependency.
        _user (Dict[str, Any]): Get current active user.

    Returns:
        List[TypeComponentSchema]: Returns all list of type components.

    Raises:
        HTTPException: If no type components are found or if an internal server error occurs.
    """
    try:
        type_components = await TypeComponentService.get_all_type_components(uow)
        if not type_components:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No type components found")
        return type_components
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.get("/type_component", response_model=TypeComponentSchema, status_code=status.HTTP_200_OK)
async def get_type_component(
        uow: UOWDep,
        type_components_id: int,
        _user: Dict[str, Any] = Depends(get_active_user),
) -> Any:
    """
    Get one type of component by its id.

    Args:
        uow (UOWDep): The unit of work dependency.
        type_components_id (int): id of the component type.
        _user (Dict[str, Any]): Get current active user.

    Returns:
        TypeComponentSchema: Returns of the type component.

    Raises:
        HTTPException: If no type components are found or if an internal server error occurs.
    """
    try:
        type_component = await TypeComponentService.get_type_component(uow, type_components_id)
        if not type_component:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No type component found")
        return type_component
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.patch("/type_component", response_model=TypeComponentSchema, status_code=status.HTTP_200_OK)
async def patch_type_component(
        uow: UOWDep,
        type_components_id: int,
        change_components: TypeComponentSchemaChange,
        _user: Dict[str, Any] = Depends(get_superuser),
) -> Any:
    """
    Changes the data about the component type by its id.

    Args:
        uow (UOWDep): The unit of work dependency.
        type_components_id (int): id of the component type.
        change_components (TypeComponentSchemaChange): fields for which the component type will change.
        _user (Dict[str, Any]): Get current superuser.

    Returns:
        TypeComponentSchema: Returns of the type component.

    Raises:
        HTTPException: If no type components are found or if an internal server error occurs.
    """
    try:
        type_component = await TypeComponentService.patch_type_component(uow, type_components_id, change_components)
        if not type_component:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No type component found")
        return type_component
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.post("/type_component", response_model=TypeComponentSchema, status_code=status.HTTP_201_CREATED)
async def create_type_component(
        uow: UOWDep,
        new_type_components: TypeComponentSchemaAdd,
        _user: Dict[str, Any] = Depends(get_superuser),
) -> Any:
    """
    Creates a new type of component.

    Args:
        uow (UOWDep): The unit of work dependency.
        new_type_components (TypeComponentSchemaAdd): data to add new type component.
        _user (Dict[str, Any]): Get current superuser.

    Returns:
        TypeComponentSchema: Returns of the type component.

    Raises:
        HTTPException: If no type components are found or if an internal server error occurs.
    """
    try:
        type_component = await TypeComponentService.create_type_component(uow, new_type_components)
        if not type_component:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No type component found")
        return type_component
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.delete("/type_component", status_code=status.HTTP_200_OK)
async def delete_type_component(
        uow: UOWDep,
        type_component_delete: TypeComponentSchemaDelete,
        _user: Dict[str, Any] = Depends(get_superuser),
) -> Any:
    """
    Delete type of component by int name or id.

    Args:
        uow (UOWDep): The unit of work dependency.
        type_component_delete (TypeComponentSchemaDelete): data to delete type component.
        _user (Dict[str, Any]): Get current superuser.

    Returns:
        None

    Raises:
        HTTPException: if an internal server error occurs.
    """
    try:
        await TypeComponentService.delete_type_component(uow, type_component_delete)
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
