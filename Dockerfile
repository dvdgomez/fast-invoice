# syntax=docker/dockerfile:1

FROM python:3.9.12-slim-buster

WORKDIR /invoice_app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "invoice_app.main:app", "--host", "0.0.0.0", "--port", "80"]
