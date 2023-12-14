from fastapi_users.authentication import JWTStrategy

from api import config

SECRET = config.SECRET_AUTH


# Top article
# https://habr.com/ru/companies/doubletapp/articles/764424/
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=config.LIFETIME_JWT)
