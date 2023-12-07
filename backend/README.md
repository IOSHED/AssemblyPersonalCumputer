# BACKEND

## Starting backend in local

```commandline
cd backend
python -m venv venv
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8080
```
