# from typing import Any

from fastapi import APIRouter

# from api.pc.service import PCService
# from api.pc.shemas import PCSchema, PCSchemaAdd
# from api.utils.dependencies import UOWDep


router = APIRouter()


# @router.post("/", response_model=PCSchema)
# async def assembly_pc(user_data_pc: PCSchemaAdd, uow: UOWDep) -> Any:
#     try:
#         new_pc = await PCService.add_pc(uow, user_data_pc)
#     except Exception as err:
#         return {"type_error": "Unknown Error", "error": err}
#     return new_pc
