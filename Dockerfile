FROM ubuntu:14.04

# Install opencv and matplotlib.
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y unzip wget build-essential \
        cmake git pkg-config libswscale-dev \
        python3-dev python3-tk \
        libtbb2 libtbb-dev libjpeg-dev \
        libpng-dev libtiff-dev libjasper-dev \
        bpython python3-pip libfreetype6-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt

RUN pip3 install --upgrade pip
RUN pip3 install opencv-python
RUN apt update && apt install -y libsm6 libxext6

ADD split-video-frames.py /split-video-frames.py
