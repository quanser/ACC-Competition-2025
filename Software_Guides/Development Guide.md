# Development Guide for the Development Container <!-- omit in toc -->

This guide will provide instructions and tips for developing your self-driving algorithm in the Isaac-ROS Development Container.

Developing in a Docker container can be tricky since everytime the container is restarted, all files and actions that took place in the container get reset.

The topics are listed below and will be updated with new information periodically:

- [Structure of the development environment](#structure-of-the-development-environment)
  - [Quanser Virtual Container](#quanser-virtual-container)
  - [Development Container](#development-container)
- [How to create files that persist in the container](#how-to-create-files-that-persist-in-the-container)
- [How to add packages via `apt` that persist](#how-to-add-packages-via-apt-that-persist)
- [How to add Python packages via `pip3` that persist](#how-to-add-python-packages-via-pip3-that-persist)
- [How to stop the RT Model](#how-to-stop-the-rt-model)

## Structure of the development environment

There are 3 components to the development environment that has been constructed for this competition:

1. `Quanser Virtual Environment Container`: A Docker Container intended for running Python scripts that set up the QLabs world.
2. `Development Container`: A Docker Container modified from the `isaac_ros` Nvidia container that contains Quanser's QCar 2 ROS2 nodes.
3. `Quanser Interactive Labs`: An application that gets installed natively in Ubuntu 24.04. This application provides the simulation environment for the QCar 2 and the Quanser Virtual Environment Container connects to this application.

![QLabsDevelopmentVennDiagram](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Guides/Pictures/DevelopmentVennDiagram.png)

To set these 3 components up, you will need to follow the [ACC Software Setup](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Guides/ACC%20Software%20Setup%20Instructions%20.md) document.

### Quanser Virtual Container

This Docker Container comes preinstalled with a Python interpreter that can run the Base Scenarios. The Base Scenarios utilize the [`qvl` library](https://qlabs.quanserdocs.com/en/latest/Objects/index.html) that allows you to spawn "actors" into the QLabs environment. The  allows you to interface with QLabs to spawn in different actors. Using `qvl` you can develop your own custom scenarios to test your algorithm.

Inside the Docker Container are 2 RT Models (Real-Time Model). When you run any of the Base Scenarios, an RT Model is run. The RT Model is what allows you to interface with the virtual QCar 2. It sends and receives information from a digital "hardware board" in QLabs.

```bash
/virtual_plants/rt_models/QCar2
                            L QCar2_Workspace_studio.rt-linux_x86_64
                            L QCar2_Workspace.rt-linux_x86_64
```

The studio RT Model is used if you spawn the QCar 2 at 1/10th scale, as done in the Setup_Competition_Map.py script. The non-studio version is used if you spawn the Virtual QCar 2 in at full scale, as done in the Setup_Base_Scenario_stop_ACC_Competition_2025.py script.

### Development Container

This Docker Container is modified from the Isaac-ROS Nvidia container. It comes preinstalled with ROS2 Humble and contains the nodes that are used to interface with the Virtual QCar2.

The ROS2 Humble nodes interface with the QCar2 via the [C API](https://docs.quanser.com/quarc/documentation/hardware_functions_alphabetical_list_c.html).

## How to create files that persist in the container

When a docker container is exited, all the changes done inside the container will be lost. Starting the Development container (Isaac-ROS) using the command `./scripts/run_dev.sh  /home/$USER/Documents/ACC_Development/Development` links the `/home/$USER/Documents/ACC_Development/Development` directory to the container and all files under this directory will automatically synced with the host. Therefore, your development files will persist even after the container is exited if you place your files in that directory. We recommend you create a `<ros_packages_go_here>` directory as shown below and develop your ROS packages in that directory:

```bash
/home/$USER/Documents/ACC_Development/Development/
                                              L ros2/
                                                  L src/
                                                      L qcar2_interfaces/
                                                      L qcar2_nodes/
                                                      L <ros_packages_go_here>/
```

If you do not plan on using ROS, we recommend you create the `<non_ros_development>` directory shown below outside of the ros2 directory:

```bash
/home/$USER/Documents/ACC_Development/Development/
                                              L ros2/
                                              L <non_ros_development>/
```

## How to add packages via `apt` that persist

Any packages that get installed via `apt` in the command line of the Development Container do not persist once the container is closed. When you are installing packages in teh terminal, make sure to edit the Docker file called **`Dockerfile.quanser`**. This Docker file is used to configure the Development container and can be found in the following folder:

```bash
cd /home/$USER/Documents/ACC_Development/docker
```

At the bottom of the `Dockerfile.quanser` add your Debian packages as shown below:

```bash
# Install Debian packages
RUN apt-get update && apt-get install -y \
    python3-transforms3d \
    python3-pyqtgraph \
    && rm -rf /var/lib/apt/lists/*
```

This example will install pytransform3d and pyqtgraph everytime the container is started. **As you develop in the Development Container**, make sure you record any packages installed via `apt` in the Docker file mentioned above.

**IMPORTANT:** If you ever download the ACC_Resources.zip file and run the `setup_linux.py` file again, this will create a new ACC_Development folder and record a backup of your previous one. Make sure to copy any changes made to `Dockerfile.quanser` over to the new ACC_Development folder.

## How to add Python packages via `pip3` that persist

**NOTE**: We recommend you use the Debian packages if they are available.

Any packages that get installed via `pip3` in the command line of the Development Container do not persist once the container is closed. When you are installing packages in the terminal, make sure to edit the Docker file called **`Dockerfile.quanser`**. This Docker file is used to configure the Development container and can be found in the following folder:

```bash
cd /home/$USER/Documents/ACC_Development/docker
```

At the bottom of the `Dockerfile.quanser` add your Python packages as shown below:

```bash
# Install Python Packages if necessary
RUN pip3 install -U \
    pytransform3d \
    pyqtgraph
```

This example will install pytransform3d and pyqtgraph everytime the container is started. **As you develop in the Development Container**, make sure you record any packages installed via `pip3` in the Docker file mentioned above.

**IMPORTANT:** If you ever download the ACC_Resources.zip file and run the `setup_linux.py` file again, this will create a new ACC_Development folder and record a backup of your previous one. Make sure to copy any changes made to `Dockerfile.quanser` over to the new ACC_Development folder.

## How to stop the RT Model

When the Setup_Competition_Map.py file gets run (or any other base scenario file provided), a real-time application (RT Model) is deployed that communicates with the virtual QCar 2. This RT Model is what the QCar2 ROS nodes communicate with. It is important to gracefully stop this model once you are no longer using your current workspace. Run the following commands to stop the RT Model:

1. Using the Quanser Virtual Environment Docker container, navigate to the following directory:

    ```bash
    cd /home/qcar2_scripts/python
    ```

2. To stop the RT Model run the following command:

    ```bash
    python3 qcar2_stop.py
    ```
