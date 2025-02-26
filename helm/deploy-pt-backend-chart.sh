#!/bin/bash

set -e

echo "######################################"
echo "Helm Version:"
helm version
echo "\n"

echo "######################################"
echo "Helm Lint:"
helm lint ./pt-backend-chart
echo "\n"

# echo "######################################"
# echo "Helm Template:"
# helm template ./pt-backend-chart
# echo "\n"

echo "######################################"
echo "Installing or upgrading chart..."
helm upgrade --install --namespace "test" --create-namespace "pt-backend-test" ./pt-backend-chart
echo "done"
echo "\n"