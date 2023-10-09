FROM postgres:13.3-alpine

RUN apk update && apk add postgresql-client

WORKDIR /usr/src/app

ENV POSTGRES_DB mydatabase
ENV POSTGRES_USER user
ENV POSTGRES_PASSWORD user