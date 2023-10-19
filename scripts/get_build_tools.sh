#!/bin/bash

# Main procedure.
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
cd "$DIR"

mkdir -p scripts/tools/linux/bin

echo "--- getting protoc ---"
PB_REL="https://github.com/protocolbuffers/protobuf/releases"
curl -LO $PB_REL/download/v3.15.8/protoc-3.15.8-linux-x86_64.zip
unzip -o protoc-3.15.8-linux-x86_64.zip -d protoc-3.15.8-linux-x86_64
cp protoc-3.15.8-linux-x86_64/bin/protoc scripts/tools/linux/bin
rm -r protoc-3.15.8-linux-x86_64*

echo "--- getting protoc-gen-openapiv2 ---"
curl -L -o scripts/tools/linux/bin/protoc-gen-openapiv2 https://github.com/grpc-ecosystem/grpc-gateway/releases/download/v2.18.0/protoc-gen-openapiv2-v2.18.0-linux-x86_64
chmod u+x scripts/tools/linux/bin/protoc-gen-openapiv2

# echo "--- getting swagger-codegen ---"
# curl -L -o scripts/tools/swagger-codegen-cli.jar https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.43/swagger-codegen-cli-3.0.43.jar

echo "--- getting openapi generator ---"
curl -L -o scripts/tools/openapi-generator-cli.jar https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.0.0/openapi-generator-cli-7.0.0.jar
