import uuid
from typing import Optional, Union, Dict, Any

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin, InvalidPasswordException
from starlette.responses import Response

from api import config
from api.auth.models import User, get_user_db
from api.auth.schemas import UserCreate


SECRET = config.SECRET_VERIFICATION


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET
    reset_password_token_lifetime_seconds = config.LIFETIME_RESET_PASSWORD
    verification_token_lifetime_seconds = config.LIFETIME_VERIF_TOKEN

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_update(self, user: User, update_dict: Dict[str, Any], request: Optional[Request] = None):
        print(f"User {user.id} has been updated with {update_dict}.")

    async def on_after_login(self, user: User, request: Optional[Request] = None, response: Optional[Response] = None):
        print(f"User {user.id} logged in.")

    async def on_after_verify(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has been verified")

    async def on_after_forgot_password(self, user: User, token: str, request: Optional[Request] = None):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_reset_password(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has reset their password.")

    async def on_after_request_verify(self, user: User, token: str, request: Optional[Request] = None):
        print(f"Verification requested for user {user.id}. Verification token: {token}")

    async def on_before_delete(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} is going to be deleted")

    async def on_after_delete(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} is successfully deleted")

    async def validate_password(self, password: str, user: Union[UserCreate, User]) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters"
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason="Password should not contain e-mail"
            )


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
