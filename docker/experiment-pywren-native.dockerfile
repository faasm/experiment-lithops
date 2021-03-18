ARG EXPERIMENTS_VERSION

FROM faasm/experiment-base-native:${EXPERIMENTS_VERSION}

WORKDIR /code
# TODO fix release version when lithops-cloud/lithops#599 is included in one
# RUN pip3 install git+git://github.com/lithops-cloud/lithops.git@v2.1.0
RUN pip3 install git+https://github.com/lithops-cloud/lithops

RUN git clone https://github.com/faasm/experiment-pywren

