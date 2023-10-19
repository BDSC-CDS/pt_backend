FROM registry.itrcs3-app.intranet.chuv/ds-cicd-template-backend-stage1:latest

USER ds

COPY --chown=ds:ds . /ds/ds-deployer
RUN rm -rf /ds/ds-deployer/.git

RUN whoami
RUN ls -lah
RUN npm ci

CMD ["/usr/bin/node", "app.js", "--config", "int"]