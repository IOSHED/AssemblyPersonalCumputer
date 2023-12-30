

from typing import Optional
import pydantic


class TypeComponentSchemaAdd(pydantic.BaseModel):
    """
    Schema for adding a type component.

    Attributes:
        name (str): The name of the type component to be added. It should be a string with a maximum length of 255 characters.
    """
    name: str = pydantic.Field(max_length=255)


class TypeComponentSchemaChange(pydantic.BaseModel):
    """
    Schema for changing a type component.

    Attributes:
        name (str, optional): The new name for the type component. It should be a string with a maximum length of 255 characters.
    """
    name: Optional[str] = pydantic.Field(max_length=255)


class TypeComponentSchemaDelete(pydantic.BaseModel):
    """
    Schema for deleting a type component.

    Attributes:
        id (int, optional): The ID of the type component to be deleted. It should be an integer greater than 0.
        name (str, optional): The name of the type component to be deleted. It should be a string with a maximum length of 255 characters.
    """
    id: Optional[int] = pydantic.Field(gt=0)
    name: Optional[str] = pydantic.Field(max_length=255)


class TypeComponentSchema(pydantic.BaseModel):
    """
    Schema for type component.

    Attributes:
        id (int): The ID of the type component. It should be an integer greater than 0.
        name (str): The name of the type component. It should be a string with a maximum length of 255 characters.
    """
    id: int = pydantic.Field(gt=0)
    name: str = pydantic.Field(max_length=255)

    class Config:
        """
        Configuration for TypeComponentSchema.

        Configures the behavior of TypeComponentSchema, such as enabling attribute-based instantiation.
        """
        from_attributes = True
