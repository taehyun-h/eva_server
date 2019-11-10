#!/bin/bash

function auto-generate-all() {
    pushd $AUTOGENERATEDIR/data

    # remove all files
    find . ! -name '__init__.py' -type f -exec trash {} +

    # re-generate grpc files
    python3 -m grpc_tools.protoc --proto_path=$PROTODIR/data \
        --python_out=. --grpc_python_out=. \
         $(find $PROTODIR/data -name "*.proto")

    popd

    pushd $AUTOGENERATEDIR/service

    # remove all files
    find . ! -name '__init__.py' -type f -exec trash {} +

    # re-generate grpc files
    python3 -m grpc_tools.protoc --proto_path=$PROTODIR/service \
        --python_out=. --grpc_python_out=. \
         $(find $PROTODIR/service -name "*.proto")

    popd
}

function update-proto() {
    pushd $PROTODIR

    git pull

    popd

    auto-generate-all
}

BASEDIR="$(cd "$(dirname "$0")"; pwd)"
PROTODIR="$BASEDIR/../eva_proto"
AUTOGENERATEDIR="$BASEDIR/../eva/protocol/grpc_auto_generated"

case "$1" in
    auto-generate-all)
        auto-generate-all
        ;;
    update-proto)
        update-proto
        ;;
    *)
        echo "invalid"
        ;;
esac
