# BACKEND

## Starting backend

Command for start:
```commandline
docker-compose up
```

Port nginx: 
```json
8080
```

Command for up migrations: 
```commandline
docker-compose exec NAME_SERVICE alembic upgrade head
```

| name service   | path api             | path docs                 |
|----------------|----------------------|---------------------------|
| auth_service   | ```/api/v1/auth```   | ```/api/v1/auth/docs```   |
| asm_pc_service | ```/api/v1/asm-pc``` | ```/api/v1/asm-pc/docs``` |

## Migrations alembic

Create:
```commandline
alembic revision --autogenerate -m "name migration"
```

Up:
```commandline
alembic upgrade head 
```

## TODO

- add OAuth in auth-service
- create python lib for packed services
- add grafana
- add ElasticSearcher
- add RabbitMQ for cooperation services
- loop refactoring
