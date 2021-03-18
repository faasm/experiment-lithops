#!/bin/bash

set -e

THIS_DIR=$(dirname $(readlink -f $0))
PROJ_ROOT=${THIS_DIR}/..
BASE_DIR=${PROJ_ROOT}/../experiment-base
DOCKER_DIR=${PROJ_ROOT}/docker

pushd ${PROJ_ROOT} >> /dev/null

# IMAGE_NAME="experiment-pywren-native"
# VERSION="$(sed -n '2,2p' ${BASE_DIR}/.env | cut -d"=" -f 2)"
# 
# docker run -it --rm \
#     -v /var/run/docker.sock:/var/run/docker.sock \
#     -v /usr/bin/docker:/usr/bin/docker \
#     -v /home/csegarra/.docker:/usr/mpirun/.docker \
#     faasm/${IMAGE_NAME}:${VERSION} \
#     bash

# Check pip3 installed
if [[ ! -d "./venv" ]]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip3 install -r ./requirements.txt

popd >> /dev/null

