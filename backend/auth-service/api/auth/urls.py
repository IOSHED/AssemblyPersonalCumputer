from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend

from api.auth.manager import get_user_manager
from api.auth.models import User
from api.auth.schemas import UserRead, UserCreate, UserUpdate
from api.auth.strategy import get_jwt_strategy
from api.auth.transport import cookie_transport


router = APIRouter()

# Use lib 'fastapi_users':
# https://fastapi-users.github.io/fastapi-users/12.1/
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

"""
Add routers:
    /jwt/login  <- login user in system
    /jwt/logout <- logout user in system
"""
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    tags=["Auth"],
)

"""
Add routers:
    /register <- register user in system

"""
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    tags=["Auth"],
)

"""
Add routers:
    /request-verify-token <- send token in email users
    /verify               <- user send getting token and become 'is_verified = true'
"""
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    tags=["Auth"],
)

"""
Add routers:
    /forgot-password <- send token in email user
    /reset-password  <- set new password by token
"""
router.include_router(
    fastapi_users.get_reset_password_router(),
    tags=["Auth"],
)

"""
Add routers:
    /users/me   <- get current users or patch current users
    /users/{id} <- delete, patch, get user by id (only for superusers)
"""
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["Users"],
)
