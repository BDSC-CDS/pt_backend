FROM registry.rdeid.unil.ch/pt-backend-stage1:latest

USER ds

COPY --chown=ds:ds . /pt_backend
USER root
RUN ls -lah /pt_backend && rm -rf /pt_backend/.git
USER ds

RUN --mount=type=secret,id=PYPI_USERNAME,uid=1000 --mount=type=secret,id=PYPI_PASSWORD,uid=1000 \
    /pt_backend/docker/secret_exec.sh pip install -r /pt_backend/requirements.txt

CMD ["python3", "-m", "src.cmd.start"]