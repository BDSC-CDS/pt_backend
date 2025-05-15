#!/bin/bash

set -e

echo "######################################"
echo "Helm Version:"
helm version
echo

echo "######################################"
echo "Helm Dependency Update:"
helm dependency update ./pt-backend-chart
helm dependency update ./pt-backend-chart/charts/pt-arx-service-chart
echo

echo "######################################"
echo "Helm Lint:"
helm lint ./pt-backend-chart
echo

echo "######################################"
echo "Helm Template:"
helm template ./pt-backend-chart
echo

echo "######################################"
echo "Installing or upgrading chart..."
helm upgrade --install --namespace "test" --create-namespace "pt-backend-test" ./pt-backend-chart
echo "done"
echo