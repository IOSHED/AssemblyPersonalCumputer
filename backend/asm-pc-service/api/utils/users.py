from typing import Dict, Any, Union

import requests
from fastapi import Request, HTTPException
from starlette import status

from api import config


def __get_current_user(request: Request) -> Union[Dict[str, Any], Exception]:
    jwt_token = request.cookies.get("bonds")
    response = requests.get(config.URL_GET_CURRENT_USER, cookies={'bonds': jwt_token})
    user_info = response.json()
    if 'detail' in user_info:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return user_info


def get_active_user(request: Request) -> Union[Dict[str, Any], Exception]:
    current_user = __get_current_user(request)
    if current_user["is_active"]:
        return current_user
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")


def get_verified_user(request: Request) -> Union[Dict[str, Any], Exception]:
    current_user = __get_current_user(request)
    if current_user["is_active"] and current_user["is_verified"]:
        return current_user
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email not verified")


def get_superuser(request: Request) -> Union[Dict[str, Any], Exception]:
    current_user = __get_current_user(request)
    if current_user["is_superuser"]:
        return current_user
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Current user is not admin")
