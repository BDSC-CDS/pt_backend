FROM registry.rdeid.unil.ch/pt-backend-stage1:latest

USER pt

COPY --chown=pt:pt . /pt_backend
USER root
RUN ls -lah /pt_backend && rm -rf /pt_backend/.git
USER pt

RUN pip install -r /pt_backend/requirements.txt

CMD ["python3", "-m", "src.cmd.start"]