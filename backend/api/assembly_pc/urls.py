from typing import Any

from fastapi import APIRouter

from api.assembly_pc.service import AssemblyPCService
from api.assembly_pc.shemas import PCSchema, PCSchemaAdd
from api.utils.dependencies import UOWDep


router = APIRouter()

# response_model=PCSchema


@router.post("/")
async def assembly_pc(user_data_pc: PCSchemaAdd, uow: UOWDep) -> Any:
    try:
        new_pc = await AssemblyPCService.add_pc(uow, user_data_pc)
    except Exception as err:
        return {"type_error": "Unknown Error", "error": err}
    return new_pc
