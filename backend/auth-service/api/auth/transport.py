from fastapi_users.authentication import CookieTransport

from api import config

# Top article:
# https://habr.com/ru/articles/710578/
cookie_transport = CookieTransport(
    cookie_max_age=config.COOKIE_MAX_EGE,
    cookie_name="bonds",
)
