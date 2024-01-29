#FROM python:3.11-buster
FROM andrejreznik/python-gdal:stable

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY migrations .
COPY pyproject.toml .
COPY src/ ./src/