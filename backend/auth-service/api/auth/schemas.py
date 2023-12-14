from typing import Optional

from fastapi_users import schemas
from pydantic import EmailStr


class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    username: str
    is_active: bool = True

    # These fields are always initially 'false', even if the query is set to 'true'
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True

    # These fields are always initially 'false', even if the query is set to 'true'
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None

    # These fields are always initially 'false', even if the query is set to 'true'
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = None
