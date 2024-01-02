import os

from dotenv import load_dotenv

load_dotenv()

"""Base config"""
MODE = os.environ.get("MODE")
VERSION_API = 1
NAME_SERVICE = "Assembly PC"
PATH_SERVICE = f"/api/v{VERSION_API}/asm-pc"
ORIGINS = [  # All hosts that can access our api
    "http://127.0.0.1:8080",
]

"""Data base"""
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
TEST_POSTGRES_DB = os.environ.get("TEST_POSTGRES_DB")

DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
TEST_DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{TEST_POSTGRES_DB}"

"""Type components"""
DEFAULT_TYPE_COMPONENTS = [
    "CPU",
    "MEMORY",
    "MOTHER_BOARD",
    "GPU",
    "POWER SUPPLIES",
    "CASES",
    "COOLING",
    "SSD",
    "HDD",
]

IS_RECREATE_TYPE_COMPONENTS = True

"""Auth"""
URL_GET_CURRENT_USER = "http://auth_service:8000/api/v1/auth/users/me"
