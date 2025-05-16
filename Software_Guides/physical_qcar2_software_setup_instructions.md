# Physical Software Setup for the ACC Competition <!-- omit in toc -->

Welcome to the ACC Quanser Self-Driving Car Student Competition - software setup!
In this document we will describe:

- [System Requirements](#system-requirements)
- [Set Up the Isaac-ROS Container](#set-up-the-isaac-ros-container)
- [How to Run the ROS2 Humble Nodes](#how-to-run-the-ros2-humble-nodes)

## System Requirements

**System Requirements**:

- The QCar 2 will be configured with the necessary system requirements

**Warning**: If you plan on changing any native packages on the QCar 2, consult the Software sections at the bottom of the following page: [QCar 2 QUARC Documentation](https://docs.quanser.com/quarc/documentation/qcar2.html)

**Docker Check**:

Docker should be installed by default on the QCar 2. Please check that it is by running the following command:

```bash
docker run hello-world
```

Make sure your QCar 2 is connected to the internet. If this does not work, please raise an issue on the Github.

To remove this container use the following commands:

```bash
docker ps -a
docker rm <CONTAINER ID of hello-world>
```

**Download and Set Up the ACC Resources**:

1. Download the ACC resources available from Quanser [ACC Resources](https://quanserinc.box.com/s/g2690n3jwbhquwr8uqdz0b45m5wx945z).

   Password: acc2025denver

2. Extract the content of ACC_Resources folder inside the Downloads folder.

3. Run the setup_linux.py to configure your development environment

How your system should look like:

``` bash
/home/$USER/Documents/ACC_Development/ 
                        L Development/
                        L isaac_ros_common/
                        L docker/
                        L dev/
                        L backup/
```

## Set Up the Isaac-ROS Container

For software development we will leverage the isaac_ros docker container. This container can be used for:

- ROS focused solutions (Using either python/C++ to publish/subscribe to the QCar 2 nodes)

The below instructions show you how to set up the **Development Docker Container**.

1. To get started please install [Nvidia-Container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-the-nvidia-container-toolkit)

    **_NOTE:_**  If you're not sure what to install, use the [Debian-based installation for the toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#with-apt-ubuntu-debian). Then [Configure Your Docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#with-apt-ubuntu-debian).

    The dev team had to install `nvidia-container-toolkit-base` package manually since the instructions on the Nvidia website was failing to install this.

2. Navigate to the following directory:

    ```bash
    cd /home/$USER/Documents/ACC_Development/isaac_ros_common
    ```

3. To start the container use the command

    ```bash
    ./scripts/run_dev.sh  /home/$USER/Documents/ACC_Development/Development
    ```

    **_NOTE:_**  You may need to add your local user to the local Docker Group. Please restart your machine once your user has been added.

4. **To open additional terminals attached to the Development docker container**, open a new terminal and run Steps 2 & 3 again.

## How to Run the ROS2 Humble Nodes

Once you are ready to start developing, follow these steps to start the virtual environment:

1. Natively in Ubuntu, open the QLabs application and navigate to the SDCS then the Open Plane.

2. If you do not have a Quanser Virtual Environment Docker container open, follow the above sections to open one.

3. Using the Quanser Virtual Environment Docker container, navigate to the following directory:

    ```bash
    cd /home/qcar2_scripts/python
    ```

4. Run the following Python script to spawn the competition map into QLabs:

    ```bash
    python3 Base_Scenarios_Python/Setup_Competition_Map.py
    ```

Once everything has run to completion, the QLabs world should look like the following:

![QLabs after running Setup_Competition_Map.py](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Guides/Pictures/HowToStart.png)

5. If you do not have a Development Docker (Isaac-ROS) container open, follow the above section to open one. The following commands should be run in the Development container.

6. Compile the QCar2 ros nodes using:

    ```bash
    colcon build
    ```

6. Source the QCar2 packages using:

    ```bash
    . install/setup.bash
    ```

7. Launch the nodes for the QCar using the launch file configured for the virtual QCar:

    ```bash
    ros2 launch qcar2_nodes qcar2_virtual_launch.py
    ```

**IMPORTANT:** For tips and guides on how to develop in this container, visit the [Devlopment Guide](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Guides/Development%20Guide.md).
