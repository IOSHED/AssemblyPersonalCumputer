from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api.auth.urls import router as router_auth
from api.db.db import Base

_Base = Base


app = FastAPI(
    title="Auth",
    openapi_url="/api/v1/auth/openapi.json",
    docs_url="/api/v1/auth/docs"
)

app.include_router(
    router_auth,
    prefix="/api/v1/auth",
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
