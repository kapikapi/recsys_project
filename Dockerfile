# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get update \ 
    && apt-get install -y g++ \
    && apt-get install -y gcc \
    && pip install -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
