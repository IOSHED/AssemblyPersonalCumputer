import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

SECRET_AUTH = os.environ.get("SECRET_AUTH")
SECRET_VERIFICATION = os.environ.get("SECRET_VERIFICATION")

COOKIE_MAX_EGE = 3600
LIFETIME_JWT = 3600
LIFETIME_RESET_PASSWORD = 3600
LIFETIME_VERIF_TOKEN = 3600
