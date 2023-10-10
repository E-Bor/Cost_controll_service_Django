FROM postgres:13.3-alpine

RUN apk update && apk add postgresql-client

COPY dump.sql /docker-entrypoint-initdb.d/dump.sql

ENV POSTGRES_DB mydatabase
ENV POSTGRES_USER user
ENV POSTGRES_PASSWORD user
