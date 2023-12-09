# BACKEND

## Starting backend in local

```commandline
cd backend
python -m venv venv
pip install -r requirements.txt
alembic upgrade head 
uvicorn main:app --reload --host 127.0.0.1 --port 8080
```

## Migrations alembic

Create:
```commandline
alembic revision --autogenerate -m "name migration"
```

Up:
```commandline
alembic upgrade head 
```
