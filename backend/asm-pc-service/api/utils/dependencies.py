from typing import Dict

from typing_extensions import Annotated

from fastapi import Depends
from api.utils.unitofwork import IUnitOfWork, UnitOfWork
from api.utils.users import get_superuser, get_verified_user, get_active_user

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]

SuperUser = Annotated[Dict[str, any], Depends(get_superuser)]
VerifiedUser = Annotated[Dict[str, any], Depends(get_verified_user)]
ActiveUser = Annotated[Dict[str, any], Depends(get_active_user)]
