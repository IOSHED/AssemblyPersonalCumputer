FROM python:3.8-slim

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt
COPY ./migrations /api/migrations
COPY ./alembic.ini /api/alembic.ini

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /api/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /api/
