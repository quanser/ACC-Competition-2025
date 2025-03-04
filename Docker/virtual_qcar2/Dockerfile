FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    locales \
    && rm -rf /var/lib/apt/lists/* \
	&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG=en_US.utf8
LABEL org.opencontainers.image.authors="tech@quanser.com"

# Install the essential
RUN apt-get update && apt-get install -y \
    build-essential \
    gnupg \
    udev \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Put the usb.ids file on the image since quanser-sdk installer needs it
COPY ./misc/usb.ids /usr/share/misc/usb.ids

# Setup the proper configuration for apt to get quanser-sdk
# Here we're getting the prerelease version
RUN wget --no-cache https://repo.quanser.com/keys/Quanser.pub
RUN wget --no-cache https://repo.quanser.com/debian/prerelease/config/99-quanser -O /etc/apt/preferences.d/99-quanser
RUN wget --no-cache https://repo.quanser.com/debian/prerelease/config/quanser.sources -O /etc/apt/sources.list.d/quanser.sources
RUN gpg --dearmor --homedir /root --output /usr/share/keyrings/Quanser.gpg Quanser.pub
RUN rm Quanser.pub

# Install quanser-sdk and quarc-runtime
RUN apt-get update && apt-get install -y \
    quanser-sdk \
    quarc-runtime \
    && rm -rf /var/lib/apt/lists/*

# Clean up some directorie in the pre-release quanser-sdk
RUN rm -r /home/dmadill /home/ubuntu

# Install Python modules that QVL needs
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-pygit2 \
    python3-numpy \
    python3-opencv \
    python3-pyqtgraph \
    python3-transforms3d \
    && rm -rf /var/lib/apt/lists/*

# Put a modified version of QLabs resources installer on image and
# Run the QLabs resources installer, but
#   - specify the installation location
#   - skip the python dependency
RUN --mount=type=bind,source=./qvl/install.py,target=install.py \
    python3 install.py --install_dir /QLabs_Resources/ --ignore_dependencies --skip_envvar_setup

# Patch QVL to be able to start rt-model for x86-64
COPY ./qvl/real_time.py /QLabs_Resources/libraries/python/qvl/real_time.py

# Python scripts to start and stop virtual qcar2
COPY ./python/ /home/qcar2_scripts/python/

# Put the QCar2_Workspace spawn model on the image
COPY ./misc/*.rt-linux_x86_64 /virtual_plants/rt_models/QCar2/

# Set the environment variables that would be set by QVL
ENV QAL_DIR=/QLabs_Resources/
ENV PYTHONPATH=/QLabs_Resources/libraries/python/
ENV RTMODELS_DIR=/virtual_plants/rt_models/

CMD ["bash"]

# start image by:
# sudo docker run --rm -it --network host --name virtual-qcar2 quanser/acc2025-virtual-qcar2 bash