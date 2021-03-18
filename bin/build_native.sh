#!/bin/bash

set -e

THIS_DIR=$(dirname $(readlink -f $0))
PROJ_ROOT=${THIS_DIR}/..
BASE_DIR=${PROJ_ROOT}/../experiment-base

pushd ${PROJ_ROOT} >> /dev/null

# Update azure config
python3 ./bin/azure_config.py

# Install dependencies
if [[ ! -d "./venv" ]]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip3 install -U pip
pip3 install -r ./requirements.txt

popd >> /dev/null

