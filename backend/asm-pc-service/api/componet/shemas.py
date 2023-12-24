from typing import Union, Dict, Any, Optional

import pydantic


class TypeComponentSchemaAdd(pydantic.BaseModel):
    name: str = pydantic.Field(max_length=255)


class TypeComponentSchemaChange(pydantic.BaseModel):
    name: Optional[str] = pydantic.Field(max_length=255)


class TypeComponentSchemaDelete(pydantic.BaseModel):
    id: Optional[int] = pydantic.Field(gt=0)
    name: Optional[str] = pydantic.Field(max_length=255)


class TypeComponentSchema(pydantic.BaseModel):
    id: int = pydantic.Field(gt=0)
    name: str = pydantic.Field(max_length=255)

    class Config:
        from_attributes = True


class ComponentSchemaAdd(pydantic.BaseModel):
    price: float = pydantic.Field(gt=0, le=9_999_999)
    user_rating_other_site: Union[float, None] = pydantic.Field(gt=0, le=10)
    user_rating: float = 0

    name: str = pydantic.Field(max_length=255)
    type_component: str = pydantic.Field(max_length=255)
    specifications: Dict[str, Any]


class ComponentSchema(pydantic.BaseModel):
    id: int = pydantic.Field(gt=0)
    price: float = pydantic.Field(gt=0, le=9_999_999)
    user_rating_other_site: float = pydantic.Field(gt=0, le=10)
    user_rating: float = pydantic.Field(gt=0, le=10)

    name: str = pydantic.Field(max_length=255)
    type_component: str = pydantic.Field(max_length=255)
    specifications: Dict[str, Any]
