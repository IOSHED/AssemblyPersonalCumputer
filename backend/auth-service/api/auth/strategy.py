from fastapi_users.authentication import JWTStrategy

from api import config

SECRET = config.SECRET_AUTH


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=config.LIFETIME_JWT)
