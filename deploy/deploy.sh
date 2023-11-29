# kubectl apply --force -f ./all.yaml
# kubectl rollout restart -f ./all.yaml || true

cp -r ../config/$env/* ./chart/files/
helm install --create-namespace --namespace ci --values ./chart/files/values.yaml --set-string aesPassphrase=$CONFIG_AES_PASSPHRASE --set-string image=registry.itrcs3-app.intranet.chuv/ds-cicd-template-backend:${IMAGE_TAG}