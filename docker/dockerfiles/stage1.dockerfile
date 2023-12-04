FROM registry.itrcs3-app.intranet.chuv/ds-ubuntu:latest

RUN apt install libpq-dev

COPY ./requirements.txt /template_backend/requirements.txt
COPY ./docker/secret_exec.sh /template_backend/docker/secret_exec.sh
RUN --mount=type=secret,id=PYPI_USERNAME --mount=type=secret,id=PYPI_PASSWORD \
    /template_backend/docker/secret_exec.sh pip install -r /template_backend/requirements.txt

WORKDIR /template_backend