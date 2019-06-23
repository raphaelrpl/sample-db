FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y \
        sudo \
        software-properties-common && \
    add-apt-repository -y ppa:nextgis/ppa && \
    apt-get update && \
    apt-get install -y \
        libgdal-dev gdal-bin \
        python3-pip python3-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install GDAL==2.4

COPY . /devel

WORKDIR /devel

RUN gdalinfo --version && \
    pip3 install -r requirements.txt

