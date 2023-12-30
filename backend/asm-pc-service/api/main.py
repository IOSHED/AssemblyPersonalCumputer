from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api.pc.urls import router as router_assembly_pc
from api.componet.urls import router as router_component
from api.type_componet.urls import router as router_type_component
from api.db.db import Base

_base = Base

app = FastAPI(
    title="Assembly PC",
    openapi_url="/api/v1/asm-pc/openapi.json",
    docs_url="/api/v1/asm-pc/docs"
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

# All hosts that can access our api
origins = [
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)
