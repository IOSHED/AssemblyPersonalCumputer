import os

from dotenv import load_dotenv

load_dotenv()

"""Base config"""
MODE = os.environ.get("MODE")
VERSION_API = 1
NAME_SERVICE = "Auth"
PATH_SERVICE = f"/api/v{VERSION_API}/auth"
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

"""Secret token"""
SECRET_AUTH = os.environ.get("SECRET_AUTH")
SECRET_VERIFICATION = os.environ.get("SECRET_VERIFICATION")

"""Lifetime"""
COOKIE_MAX_EGE = 3600
LIFETIME_JWT = 3600
LIFETIME_RESET_PASSWORD = 3600
LIFETIME_VERIF_TOKEN = 3600
