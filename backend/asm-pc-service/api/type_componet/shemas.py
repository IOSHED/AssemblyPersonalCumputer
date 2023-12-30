from typing import Optional

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
