#!/bin/bash

set -e

docker build --pull -f dockerfiles/stage2.dockerfile -t registry.rdeid.unil.ch/pt-backend:${IMAGE_TAG} ..
docker tag registry.rdeid.unil.ch/pt-backend:${IMAGE_TAG} registry.rdeid.unil.ch/pt-backend:latest
docker push registry.rdeid.unil.ch/pt-backend:${IMAGE_TAG}
docker push registry.rdeid.unil.ch/pt-backend:latest