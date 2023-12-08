from typing import Any

from fastapi import APIRouter

from api.assembly_pc.service import AssemblyPCService
from api.assembly_pc.shemas import PCSchema, PCSchemaAdd
from api.utils.dependencies import UOWDep


router = APIRouter()

# TODO create a good except error


@router.post("/", response_model=PCSchema)
async def assembly_pc(user_data_pc: PCSchemaAdd, uow: UOWDep) -> Any:
    try:
        new_pc = await AssemblyPCService.add_pc(uow, user_data_pc)
    except Exception as err:
        return {"type_error": "Unknown Error", "error": err}
    return new_pc
