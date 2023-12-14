from fastapi_users.authentication import CookieTransport

from api import config

cookie_transport = CookieTransport(
    cookie_max_age=config.COOKIE_MAX_EGE,
    cookie_name="bonds",
)
