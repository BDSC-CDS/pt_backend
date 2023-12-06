#!/bin/bash

set -e

# kubectl apply --force -f ./all.yaml
# kubectl rollout restart -f ./all.yaml || true

mkdir -p ./chart/files
rm -rf ./chart/files/*
cp -r ../configs/$env/* ./chart/files/

helm version
helm template --namespace ci --values ./chart/files/values.yaml --set-string "aesPassphrase=$CONFIG_AES_PASSPHRASE" --set-string "image=registry.itrcs3-app.intranet.chuv/ds-cicd-template-backend:${IMAGE_TAG}" ./chart

echo ""
echo "deploying..."
helm upgrade --install --create-namespace --namespace ci --values ./chart/files/values.yaml --set-string "aesPassphrase=$CONFIG_AES_PASSPHRASE" --set-string "version=$IMAGE_TAG" --set-string "image=registry.itrcs3-app.intranet.chuv/ds-cicd-template-backend:${IMAGE_TAG}" "${RELEASE_NAME}" ./chart
echo "done"