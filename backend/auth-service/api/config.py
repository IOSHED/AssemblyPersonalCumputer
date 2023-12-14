import os

from dotenv import load_dotenv

load_dotenv()


"""Data base"""
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"


"""Secret token"""
SECRET_AUTH = os.environ.get("SECRET_AUTH")
SECRET_VERIFICATION = os.environ.get("SECRET_VERIFICATION")


"""Lifetime"""
COOKIE_MAX_EGE = 3600
LIFETIME_JWT = 3600
LIFETIME_RESET_PASSWORD = 3600
LIFETIME_VERIF_TOKEN = 3600
