docker build --pull -f dockerfiles/stage2.dockerfile -t registry.itrcs3-app.intranet.chuv/ds-cicd-template-backend:${IMAGE_TAG} --secret id=PYPI_USERNAME,env=PYPI_USERNAME --secret id=PYPI_PASSWORD,env=PYPI_PASSWORD ..
docker tag registry.itrcs3-app.intranet.chuv/ds-cicd-template-backend:${IMAGE_TAG} registry.itrcs3-app.intranet.chuv/ds-cicd-template-backend:latest
docker push registry.itrcs3-app.intranet.chuv/ds-cicd-template-backend:${IMAGE_TAG}
docker push registry.itrcs3-app.intranet.chuv/ds-cicd-template-backend:latest