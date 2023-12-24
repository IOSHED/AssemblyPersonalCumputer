from typing import Any

from fastapi import APIRouter

from api.pc.service import PCService
from api.pc.shemas import PCSchema, PCSchemaAdd
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
