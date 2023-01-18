# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# For Mysql
# RUN apt-get update
# RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y
# RUN apt-get install mariadb-server -y

# RUN apt-get update
# RUN apt-get install python3-dev libpq-dev  -y

COPY requirements.txt requirements.txt

COPY .bashrc ~/.bashrc

RUN pip install -r requirements.txt

COPY . /code