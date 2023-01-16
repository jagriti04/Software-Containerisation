FROM python:latest

RUN python -m venv venv
RUN /usr/local/bin/python - m pip install --upgrade pip

ADD requirement.txt /tmp/

RUN pip install -r /tmp/requirement.txt

RUN mkdir -p /Rest-API/

COPY . /Rest-API/

WORKDIR /Rest-API/

RUN ["python", "manage.py"]