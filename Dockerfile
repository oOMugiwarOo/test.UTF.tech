FROM python:3.12-alpine3.19

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt ./app/

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app