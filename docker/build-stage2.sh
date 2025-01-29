#!/bin/bash

set -e

docker build --pull -f dockerfiles/stage2.dockerfile -t registry.rdeid.unil.ch/pt-backend:${IMAGE_TAG} ..

docker push registry.rdeid.unil.ch/pt-backend:${IMAGE_TAG}

docker tag registry.rdeid.unil.ch/pt-backend:${IMAGE_TAG} ghcr.io/bdsc-cds/pt-backend:${IMAGE_TAG}
docker push ghcr.io/bdsc-cds/pt-backend:${IMAGE_TAG}

# if IMAGE_TAG matches master-[0-9]*, push to tag latest
if [[ ${IMAGE_TAG} =~ ^master-[0-9]+$ ]]; then
  docker tag registry.rdeid.unil.ch/pt-backend:${IMAGE_TAG} registry.rdeid.unil.ch/pt-backend:latest
  docker push registry.rdeid.unil.ch/pt-backend:latest
  
  docker tag registry.rdeid.unil.ch/pt-backend:${IMAGE_TAG} ghcr.io/bdsc-cds/pt-backend:latest
  docker push ghcr.io/bdsc-cds/pt-backend:latest
fi
