FROM registry.rdeid.unil.ch/ds-ubuntu:latest

USER root

RUN apt update && apt install libpq-dev -y --no-install-recommends

USER ds

COPY ./requirements.txt /pt_backend/requirements.txt
COPY ./docker/secret_exec.sh /pt_backend/docker/secret_exec.sh
RUN --mount=type=secret,id=PYPI_USERNAME,uid=1000 --mount=type=secret,id=PYPI_PASSWORD,uid=1000 \
    /pt_backend/docker/secret_exec.sh pip install -r /pt_backend/requirements.txt

WORKDIR /pt_backend