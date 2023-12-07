
from typing import Union, Dict

import pydantic


class PCSchemaAdd(pydantic.BaseModel):
    price: int = pydantic.Field(gt=0)
    components: Union[Dict[str, str], None] = None


class PCSchema(pydantic.BaseModel):
    id: int
    price: int = pydantic.Field(gt=0)
    other_components: Dict[str, str]
