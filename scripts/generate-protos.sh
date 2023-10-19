#!/bin/bash

# Main procedure.
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
cd "$DIR"

PATH="$PATH:$PWD/scripts/tools/linux/bin"

echo $PATH

function generate_api_files() {
    # Protobuf and openapiv2 instantiations.
    echo
    echo "==> Handling proto files:"

    mkdir -p internal/api/v1/templatebackend
    mkdir -p api/openapiv2/v1-tags

    for file in api/proto/v1/*.proto; do
        if [[ -f $file ]]; then
            echo "---> generating grpc files..."
            echo $(basename $file)
            echo $file
            #python3 -m grpc_tools.protoc --proto_path=. --proto_path=api/proto/third_party --python_out=internal --grpc_python_out=internal $file
            # protoc --proto_path=api/proto/v1/ --proto_path=api/proto/third_party --go_out=plugins=grpc:internal/api/v1/templatebackend $(basename $file)


            # echo "---> generating grpc gateway files..."
            # protoc --proto_path=api/proto/v1 --proto_path=api/proto/third_party --grpc-gateway_out=logtostderr=true:internal/api/v1/templatebackend $(basename $file)

            #echo "---> generating grpc validation files..."
            #protoc --proto_path=api/proto/v1 --proto_path=api/proto/third_party --govalidators_out=internal/api/v1/templatebackend  `basename $file`

            echo "---> generating openapiv2 files..."
            protoc --proto_path=api/proto/v1 --proto_path=api/proto/third_party --openapiv2_out=disable_default_errors=true,simple_operation_ids=true,logtostderr=true:api/openapiv2/v1-tags $(basename $file)
        fi
    done

    echo "---> generating merged openapiv2 API definition file 'apis.openapiv2.json' ..."
    protoc --proto_path=api/proto/v1 --proto_path=api/proto/third_party --openapiv2_out=logtostderr=true,allow_merge=true,merge_file_name=apis:api/openapiv2/v1-tags api/proto/v1/*.proto
}

function generate_server() {
    # Protobuf and openapiv2 instantiations.
    echo
    echo "==> Handling openapi file:"

    echo "---> generating flask server ..."
    java -jar ./scripts/tools/openapi-generator-cli.jar generate \
       -i api/openapiv2/v1-tags/apis.swagger.json \
       -g python-flask \
       -o internal/api/server_template \
       -t internal/api/generator-template/python-flask

}

generate_api_files
generate_server
