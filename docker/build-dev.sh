#!/bin/bash

set -e

docker build -f dockerfiles/dev.dockerfile -t local/pt-backend-stage1 ..