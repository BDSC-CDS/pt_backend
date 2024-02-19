FROM registry.rdeid.unil.ch/pt-ubuntu:latest

USER root

RUN apt-get update && \
    apt-get install -y python3 python3-pip unzip default-jre libpq-dev

COPY requirements.txt  /pt/pt-deployer/requirements.txt
RUN pip3 install -r requirements.txt
RUN rm /pt/pt-deployer/requirements.txt

USER pt

ENV SHELL /bin/bash