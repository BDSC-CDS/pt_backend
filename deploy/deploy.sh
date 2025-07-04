#!/bin/bash

set -e

mkdir -p ./chart/files
rm -rf ./chart/files/*
cp -r ../configs/$env/* ./chart/files/

helm version
CONFIG_AES_PASSPHRASE_VAR_NAME="CONFIG_AES_PASSPHRASE_$env"
helm template --namespace "$env" --values ./chart/files/values.yaml --set-string "aesPassphrase=${!CONFIG_AES_PASSPHRASE_VAR_NAME}" --set-string "version=$version" --set-string "image=registry.rdeid.unil.ch/pt-backend:${IMAGE_TAG}" ./chart

echo ""
echo "deploying..."
helm upgrade --install --create-namespace --namespace "$env" --values ./chart/files/values.yaml --set-string "aesPassphrase=${!CONFIG_AES_PASSPHRASE_VAR_NAME}" --set-string "version=$version" --set-string "image=registry.rdeid.unil.ch/pt-backend:${IMAGE_TAG}" "${RELEASE_NAME}" ./chart
echo "done"