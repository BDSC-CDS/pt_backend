kubectl apply --force -f ./all.yaml
kubectl rollout restart -f ./all.yaml || true