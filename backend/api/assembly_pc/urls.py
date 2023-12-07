from typing import Any

from fastapi import APIRouter

from api.assembly_pc.service import AssemblyPCService
from api.assembly_pc.shemas import PCSchema, PCSchemaAdd
from api.utils.dependencies import UOWDep


router = APIRouter()


@router.post("/", response_model=PCSchema)
async def assembly_pc(user_data_pc: PCSchemaAdd, uow: UOWDep) -> Any:
    new_pc = await AssemblyPCService.add_pc(uow, user_data_pc)
    return new_pc
