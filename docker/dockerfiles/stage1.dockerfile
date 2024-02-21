FROM registry.rdeid.unil.ch/pt-ubuntu:latest

USER root

RUN apt update && apt install libpq-dev -y --no-install-recommends

USER pt

COPY ./requirements.txt /pt_backend/requirements.txt
RUN pip install -r /pt_backend/requirements.txt

WORKDIR /pt_backend