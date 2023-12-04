FROM registry.itrcs3-app.intranet.chuv/ds-ubuntu:latest

USER root

RUN apt update && apt install libpq-dev -y --no-install-recommends

RUN curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | tee /usr/share/keyrings/helm.gpg > /dev/null && \
    apt install apt-transport-https --yes && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | tee /etc/apt/sources.list.d/helm-stable-debian.list && \
    apt update  && \
    apt install helm

USER ds

COPY ./requirements.txt /template_backend/requirements.txt
COPY ./docker/secret_exec.sh /template_backend/docker/secret_exec.sh
RUN --mount=type=secret,id=PYPI_USERNAME,uid=1000 --mount=type=secret,id=PYPI_PASSWORD,uid=1000 \
    /template_backend/docker/secret_exec.sh pip install -r /template_backend/requirements.txt

WORKDIR /template_backend