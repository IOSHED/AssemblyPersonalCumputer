from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend

from api.auth.manager import get_user_manager
from api.auth.models import User
from api.auth.schemas import UserRead, UserCreate, UserUpdate
from api.auth.strategy import get_jwt_strategy
from api.auth.transport import cookie_transport


router = APIRouter()

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_verify_router(UserRead),
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_reset_password_router(),
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate, requires_verification=True),
    prefix="/users",
    tags=["Users"],
)
