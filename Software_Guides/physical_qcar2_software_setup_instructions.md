# Physical Software Setup for the ACC Competition <!-- omit in toc -->

Welcome to the ACC Quanser Self-Driving Car Student Competition software setup!

In this document we will describe:

- [System Requirements](#system-requirements)
- [Set Up the Isaac-ROS Container](#set-up-the-isaac-ros-container)
- [How to Run the ROS2 Humble Nodes](#how-to-run-the-ros2-humble-nodes)

## System Requirements

**System Requirements**:

- The QCar 2 provided will be configured with the necessary system requirements

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

3. Run the `setup_qcar2.py` file to configure your development environment

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

Note: Isaac ROS is already installed on the QCar 2. You will only need to install the Nvidia Container Toolkit.

1. To get started please install [Nvidia-Container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-the-nvidia-container-toolkit)

    **_NOTE:_**  If you're not sure what to install, use the [Debian-based installation for the toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#with-apt-ubuntu-debian). Then [Configure Your Docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#with-apt-ubuntu-debian).

    The dev team had to install `nvidia-container-toolkit-base` package manually since the instructions on the Nvidia website commands were failing to install this. Please do this if necessary.

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

To ensure safe development, the QCar 2 nodes should not be touched and no packages should be installed on the native Ubuntu. Instead, you will install packages on the Isaac-ROS container and write scripts within the container that will communicate with the ROS nodes running natively. This structure will look like the following:

![Development Structure](https://github.com/quanser/ACC-Competition-2025/tree/stage2/Software_Guides/Pictures/software_architecture_stage2.png)

Use the following steps to run the ROS2 nodes for the first time. Once you have done this once, you won't need to do the steps involving building the nodes again.

1. Source ROS2 Humble:

    ```bash
    source /opt/ros/humble/setup.bash
    ```

2. Transfer the ROS nodes and interfaces into the ros2 directory:

    ```bash
    cp -r -u /home/$USER/Documents/ACC_Development/Development/ros2/src /home/$USER/ros2
    ```

3. Make sure Python 3.8 is being used to build the nodes:

    ```bash
    PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.8/dist-packages
    ```

4. Navigate to the ros2 folder and build the nodes:

    ```bash
    cd /home/$USER/ros2
    colcon build
    ```

5. Source the recently compiled ROS packages:

    ```bash
    source install/setup.bash
    ```

6. Run the nodes using the following command:

    ```bash
    ros2 launch qcar2_nodes qcar2_launch.py
    ```

7. Open an Isaac-ROS container in a NEW terminal using the following commands:

    ```bash
        cd /home/$USER/Documents/ACC_Development/isaac_ros_common
        ./scripts/run_dev.sh  /home/$USER/Documents/ACC_Development/Development
    ```

8. Open RViz2:

    ```bash
    rviz2
    ```

9. Add 'By Topic' relevant topics such as /laserscan.

**IMPORTANT:** For tips and guides on how to develop in this container, visit the [Devlopment Guide](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Guides/Development%20Guide.md).
