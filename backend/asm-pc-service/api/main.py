from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api import config
from api.pc.urls import router as router_assembly_pc
from api.componet.urls import router as router_component
from api.type_componet.urls import router as router_type_component
from api.db.db import Base

_base = Base

app = FastAPI(
    title=config.NAME_SERVICE,
    openapi_url=f"{config.PATH_SERVICE}/openapi.json",
    docs_url=f"{config.PATH_SERVICE}/docs"
)


app.include_router(
    router_assembly_pc,
    prefix="/api/v1/asm-pc",
    tags=["Assembly PC"],
)

app.include_router(
    router_component,
    prefix="/api/v1/asm-pc",
    tags=["Components"],
)

app.include_router(
    router_type_component,
    prefix="/api/v1/asm-pc",
    tags=["Type Components"],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)
