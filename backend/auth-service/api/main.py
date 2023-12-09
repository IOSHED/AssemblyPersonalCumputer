from fastapi import FastAPI
# from starlette.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Assembly PC",
    openapi_url="/api/v1/auth/openapi.json",
    docs_url="/api/v1/auth/docs"
)
