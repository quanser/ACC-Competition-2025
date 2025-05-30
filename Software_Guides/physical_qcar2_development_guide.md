# Physical Development Guide <!-- omit in toc -->

This document will show the architecture of the software on the physical QCar 2 and describe the intended development structure for the QCar 2.

- [Stage 2 Software Architecture](#stage-2-software-architecture)
- [How to Transfer the Virtual Isaac-ROS Container to the Physical System](#how-to-transfer-the-virtual-isaac-ros-container-to-the-physical-system)
- [Best Practices for a Python only Setup](#best-practices-for-a-python-only-setup)
- [How to add packages via `apt` that persist in the Isaac-ROS container](#how-to-add-packages-via-apt-that-persist-in-the-isaac-ros-container)
- [How to add Python packages via `pip3` that persist in the Isaac-ROS container](#how-to-add-python-packages-via-pip3-that-persist-in-the-isaac-ros-container)

## Stage 2 Software Architecture

The physical QCar 2 system will have a slightly different software architecture than stage 1 of the competition. The QCar 2 nodes will be run in the native Ubuntu OS, while any development will be done in the Isaac-ROS container. You are not intended to modify the base ROS2 nodes and instead will only modify packages and scripts within the Isaac-ROS container. This will ensure a safe development environment for all participants.

![Development Structure](https://github.com/quanser/ACC-Competition-2025/blob/stage2/Software_Guides/Pictures/software_architecture_stage2.png)

It is important that teams understand that changing packagaes in the native Ubuntu OS can damage the QCar 2 software irrepairably. Before updating any packages, please make sure they do not affect the packages in Software Section of the following document: [QCar2 QUARC Documentation](https://docs.quanser.com/quarc/documentation/qcar2.html).

## How to Transfer the Virtual Isaac-ROS Container to the Physical System

In Stage 1, ROS packages were created in `/home/$USER/Documents/ACC_Development/Development`. For Stage 2 please transfer these files to the `/home/$USER/Documents/ACC_Development/dev` folder. These will be pulled into the Isaac-ROS container every time it is spun up with the following command: `./scripts/run_dev.sh  /home/$USER/Documents/ACC_Development/dev`.

Any Debian or Python packages you installed on the Isaac-ROS container through `Dockerfile.quanser` in Stage 1 must be transferred over to the `Dockerfile.quanser-qcar2`.

## Best Practices for a Python only Setup

We understand that some of our participants are choosing to stick to a Python only setup. It is important that these users understand that damaging the native Python installation can lead to a bricked QCar 2 that can only be fixed by sending it back to Quanser. To avoid this, always check the following software list for conflicts before installing packages: [QCar2 QUARC Documentation](https://docs.quanser.com/quarc/documentation/qcar2.html).

We also recommend that you work inside a virtual environment. Please use the following to create a `venv` for Python:

1. Install the debian version of venv:

    ```bash
    sudo apt install python3.8-venv
    ```

2. Create the virtual environment and give it access to the system packages so that the Quanser Python API can be used:

    ```bash
    python3.8 -m venv --system-site-packages .
    ```

The command `deactivate` will exit the virtual environment when you are inside of it and to reactivate the environment, `source /path_to_venv/bin/activate`.

It is important to keep track of the Python packages that you have installed so that you can recreate the venv if you break things.

## How to add packages via `apt` that persist in the Isaac-ROS container

Any packages that get installed via `apt` in the command line of the Isaac-ROS Container do not persist once the container is closed. When you are installing packages in the terminal, make sure to edit the Docker file called **`Dockerfile.quanser-qcar2`**. This Docker file is used to configure the Isaac-ROS container and can be found in the following folder:

```bash
cd /home/$USER/Documents/ACC_Development/docker/isaac_ros
```

At the bottom of the `Dockerfile.quanser-qcar2` add your Debian packages as shown below:

```bash
# Install Debian packages
RUN apt-get update && apt-get install -y \
    python3-pyqtgraph \
    && rm -rf /var/lib/apt/lists/*
```

This example will install pytransform3d and pyqtgraph everytime the container is started. **As you develop in the Development Container**, make sure you record any packages installed via `apt` in the Docker file mentioned above.

**IMPORTANT:** If you ever download the ACC_Resources.zip file and run the `setup_qcar2.py` file again, this will create a new ACC_Development folder and record a backup of your previous one. Make sure to copy any changes made to `Dockerfile.quanser-qcar2` over to the new ACC_Development folder.

## How to add Python packages via `pip3` that persist in the Isaac-ROS container

**NOTE**: We recommend you use the Debian packages if they are available.

Any packages that get installed via `pip3` in the command line of the Isaac-ROS Container do not persist once the container is closed. When you are installing packages in the terminal, make sure to edit the Docker file called **`Dockerfile.quanser-qcar2`**. This Docker file is used to configure the Isaac-ROS container and can be found in the following folder:

```bash
cd /home/$USER/Documents/ACC_Development/docker/isaac_ros
```

At the bottom of the `Dockerfile.quanser-qcar2` add your Python packages as shown below:

```bash
# Install Python Packages if necessary
RUN pip3 install -U \
    pytransform3d \
    pyqtgraph
```

This example will install pytransform3d and pyqtgraph everytime the container is started. **As you develop in the Isaac-ROS Container**, make sure you record any packages installed via `pip3` in the Docker file mentioned above.

**IMPORTANT:** If you ever download the ACC_Resources.zip file and run the `setup_qcar2.py` file again, this will create a new ACC_Development folder and record a backup of your previous one. Make sure to copy any changes made to `Dockerfile.quanser-qcar2` over to the new ACC_Development folder.
