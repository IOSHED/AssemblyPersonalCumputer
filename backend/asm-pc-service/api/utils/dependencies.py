import requests
from typing_extensions import Annotated

from fastapi import Depends

from api import config
from api.utils.unitofwork import IUnitOfWork, UnitOfWork

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
current_user = requests.post(config.URL_GET_CURRENT_USER).json()
