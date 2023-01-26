# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt requirements.txt

# COPY .bashrc ~/.bashrc

RUN pip install -r requirements.txt

RUN pip install gunicorn

COPY . /code

CMD ["gunicorn"  ,  "-b", "0.0.0.0:8000", "survey.wsgi:application"]