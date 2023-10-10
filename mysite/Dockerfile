FROM python:3.11-bullseye

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get upgrade -y\
    && pip install -r requirements.txt \
    && python manage.py collectstatic --no-input \
    && wget -O /usr/local/bin/wait-for-it.sh \
    https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x /usr/local/bin/wait-for-it.sh

CMD ["wait-for-it.sh", "db:5432", "--","python", "manage.py" ,"runserver", "0.0.0.0:7000"]
EXPOSE 8000