
from typing_extensions import Annotated

from fastapi import Depends

from api.utils.unitofwork import IUnitOfWork, UnitOfWork

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
