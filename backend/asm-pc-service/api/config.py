import os

from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

DATABASE_URL = os.environ.get("DATABASE_URL")

URL_GET_CURRENT_USER = "http://auth_service:8000/api/v1/auth/users/me"

TYPE_COMPONENTS = [
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
