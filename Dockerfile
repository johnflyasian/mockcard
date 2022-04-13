FROM bitnami/python:3.9

RUN apt-get update -y

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .
CMD gunicorn -w 1 --threads 4 -b 0.0.0.0:5000 wsgi:flaskapp

