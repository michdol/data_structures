FROM python:3.12-slim-bullseye AS build

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        libpython3-dev \
        libpq-dev \
        gcc && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

CMD mkdir /intrv
COPY . /intrv
WORKDIR /intrv

RUN pip install -r /intrv/requirements.txt

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
CMD tail -f /dev/null
