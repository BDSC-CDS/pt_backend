#!/bin/bash

set -e

docker build -f dockerfiles/dev.dockerfile -t local/ds-cicd-template-backend-stage1 ..