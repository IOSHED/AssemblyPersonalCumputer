from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api import config
from api.auth.urls import router as router_auth
from api.db.db import Base

# Import for alembic migrations
_Base = Base

# Init app
app = FastAPI(
    title=config.NAME_SERVICE,
    openapi_url=f"{config.PATH_SERVICE}/openapi.json",
    docs_url=f"{config.PATH_SERVICE}/docs"
)

# All include routers
app.include_router(
    router_auth,
    prefix=config.PATH_SERVICE,
)

# All use middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)
