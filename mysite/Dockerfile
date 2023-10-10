FROM python:3.11-bullseye

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get upgrade -y\
    && pip install -r requirements.txt \
    && python manage.py collectstatic --no-input

CMD ["python", "manage.py" ,"runserver", "0.0.0.0:7000"]
EXPOSE 8000