
from typing import List, Union

import pydantic

from api.componet.shemas import ComponentSchema


class PCSchemaAdd(pydantic.BaseModel):
    price: float = pydantic.Field(gt=0, le=9_999_999)
    components: Union[List[ComponentSchema], None] = None


class PCSchema(pydantic.BaseModel):
    id: int = pydantic.Field(gt=0)
    price: float = pydantic.Field(gt=0, le=9_999_999)
    components: List[ComponentSchema]
