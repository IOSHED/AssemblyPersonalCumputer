from __future__ import annotations

from typing import List

from api import config
from api.type_componet.shemas import TypeComponentSchemaAdd, TypeComponentSchema, TypeComponentSchemaDelete, \
    TypeComponentSchemaChange
from api.utils.dependencies import UOWDep


class TypeComponentService:
    @staticmethod
    async def create_type_component(uow: UOWDep, type_component: TypeComponentSchemaAdd) -> TypeComponentSchema:
        """
        Adds a new type component to the database.

        Args:
            uow (UOWDep): The unit of work dependency.
            type_component (TypeComponentSchemaAdd): The type component to add.

        Returns:
            TypeComponentSchema: The newly added type component.
        """
        type_component_dict = type_component.model_dump()
        async with uow:
            type_component_id = await uow.type_component.add_one(data=type_component_dict)
            new_type_component = await uow.type_component.find_one(id=type_component_id)

            await uow.commit()
            return new_type_component

    @staticmethod
    async def create_type_components(uow: UOWDep) -> List[TypeComponentSchema]:
        """
        Creates multiple type components and adds them to the database.

        Args:
            uow (UOWDep): The unit of work dependency.

        Returns:
            List[TypeComponentSchema]: The list of newly created type components.
        """
        async with uow:
            new_components = []
            for name in config.TYPE_COMPONENTS:
                new_type_component = TypeComponentSchemaAdd(name=name).model_dump()
                new_id = await uow.type_component.add_one(data=new_type_component)
                new_component = await uow.type_component.find_one(id=new_id)
                new_components.append(new_component)

            await uow.commit()
            return new_components

    @staticmethod
    async def delete_type_components(uow: UOWDep):
        """
        Deletes all type components from the database.

        Args:
            uow (UOWDep): The unit of work dependency.
        """
        async with uow:
            await uow.type_component.delete_all()
            await uow.commit()

    @staticmethod
    async def delete_type_component(uow: UOWDep, type_component_delete: TypeComponentSchemaDelete):
        """
        Deletes a specific type component from the database.

        Args:
            uow (UOWDep): The unit of work dependency.
            type_component_delete (TypeComponentSchemaDelete): The type component to delete.
        """
        async with uow:
            await uow.type_component.delete_one(filter_by=type_component_delete.model_dump())
            await uow.commit()

    @staticmethod
    async def patch_type_component(
            uow: UOWDep,
            type_components_id: int,
            change_component: TypeComponentSchemaChange
    ) -> TypeComponentSchema:
        """
        Updates a specific type component in the database.

        Args:
            uow (UOWDep): The unit of work dependency.
            type_components_id (int): The ID of the type component to update.
            change_component (TypeComponentSchemaChange): The updated type component data.

        Returns:
            TypeComponentSchema: The updated type component.
        """
        async with uow:
            type_component_id = await uow.type_component.edit_one(
                unit_id=type_components_id,
                data=change_component.model_dump()
            )
            new_type_component = await uow.type_component.find_one(id=type_component_id)
            await uow.commit()
            return new_type_component

    @staticmethod
    async def get_type_component(uow: UOWDep, type_components_id: int) -> TypeComponentSchema:
        """
        Retrieves a specific type component from the database.

        Args:
            uow (UOWDep): The unit of work dependency.
            type_components_id (int): The ID of the type component to retrieve.

        Returns:
            TypeComponentSchema: The retrieved type component.
        """
        async with uow:
            type_component = await uow.type_component.find_one(id=type_components_id)
            return type_component

    @staticmethod
    async def get_all_type_components(uow: UOWDep) -> List[TypeComponentSchema]:
        """
        Retrieves all type components from the database.

        Args:
            uow (UOWDep): The unit of work dependency.

        Returns:
            List[TypeComponentSchema]: The list of retrieved type components.
        """
        async with uow:
            list_type_components = await uow.type_component.find_all()
            return list_type_components
