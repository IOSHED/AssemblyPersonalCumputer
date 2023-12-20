# Auth service
This service provides APIs for authentication, 
user authorization, as well as viewing and editing users.

## Administration Menu

You can access the API of this service using 
the [path](http://localhost:8080/api/v1/auth): `api/v1/auth`.  
[Documentation](http://localhost:8080/api/v1/auth/docs) is provided by the [`Swagger`](https://swagger.io/) tool along 
the path `/api/v1/auth/docs`.


## Table of contents

- Requirements
- Installation
- Configuration
- Maintainers


## Requirements

This module requires the following modules:

- [FastAPI](https://fastapi.tiangolo.com/ru/)
- [SqlAlchemy](https://docs.sqlalchemy.org/en/20/)
- [pydantic](https://docs.pydantic.dev/latest/)
- [fastapi-users[sqlalchemy]](https://fastapi-users.github.io/fastapi-users/12.1/)

More dependencies can be found in the file: `requirements.txt`


## Installation

Install the service's code base:
```commandline
git clone https://github.com/IOSHED/AssemblyPersonalCumputer/tree/main/backend/auth-service
```


## Configuration

To configure the service, use the file: `api/config.py`

1) Create the file `.env`. For example:
    ```dotenv
    MODE=DEBUG# DEV, DEBUG, PROD
    POSTGRES_USER=...
    POSTGRES_PASSWORD=...
    POSTGRES_DB=...
    POSTGRES_HOST=...
    POSTGRES_PORT=...
    TEST_POSTGRES_DB=...
    SECRET_AUTH=...
    SECRET_VERIFICATION=...
    ```

2) Add the service to `docker-compose` by creating a `postgres` database for it:
   ```yaml
   auth_service:
    build: ./auth-service
    command: uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
    volumes:
      - ./auth-service/:/api/
    ports:
      - 8002:8000
    env_file:
      - ./auth-service/.env
    depends_on:
      - auth_db
   
   auth_db:
    image: postgres:12.1-alpine
    volumes:
      - postgres_data_auth:/var/lib/postgresql/data/
    env_file:
      - ./auth-service/.env
   ```

3) Build and run containers:
   ```commandline
   docker-compose build
   docker-compose run
   ```
   
4) Apply migrations to the database:
   ```commandline
   docker-compose exec alembic migrations heade
   ```
   
5) Go to the documentation on the path [Documentation](http://localhost:8080/api/v1/auth/docs): `/api/v1/auth/docs`.


## Maintainers

- Ivenin Valentin - [github](https://github.com/IOSHED)
