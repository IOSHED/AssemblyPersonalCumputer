
from typing import Union, Dict

import pydantic


class PCSchemaAdd(pydantic.BaseModel):
    price: int = pydantic.Field(gt=0)
    components: Union[Dict[str, str], None] = None


class PCSchema(pydantic.BaseModel):
    id: int = pydantic.Field(gt=0)
    price: int = pydantic.Field(gt=0)
    components: Dict[str, str]
