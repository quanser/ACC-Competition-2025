# Physical QCar 2 Software Setup for the ACC Competition <!-- omit in toc -->

Welcome to the ACC Quanser Self-Driving Car Student Competition software setup!

**IMPORTANT NOTE: The password for the QCar 2 is `nvidia`**

In this document we will describe:

- [System Requirements](#system-requirements)
- [Set Up the Isaac-ROS (Development) Container](#set-up-the-isaac-ros-development-container)
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

Make sure your QCar 2 is connected to the internet. You should see a `Hello from Docker` somewhere in the output. If this does not work, please raise an issue on the Github.

To remove this container use the following commands:

```bash
docker ps -a
docker rm <CONTAINER ID of hello-world>
```

**Download and Set Up the ACC Resources**:

1. Download the ACC resources available from Quanser [ACC Resources](https://quanserinc.box.com/s/g2690n3jwbhquwr8uqdz0b45m5wx945z).

   Password: acc2025denver

2. Extract the content of ACC_Resources folder inside the Downloads folder.

3. Navigate into the ACC_Resouces folde and run the `setup_qcar2.py` Python script:

```bash
cd /home/$USER/Downloads/ACC_Resources
python setup_qcar2.py
```

If this is your FIRST TIME RUNNING THIS SCRIPT, restart your system using `sudo reboot now`, then run the script again.

Once you run this, your system should look like this:

``` bash
/home/$USER/Documents/ACC_Development/ 
                        L Development/
                        L isaac_ros_common/
                        L docker/
                        L dev/
                        L backup/
```

## Set Up the Isaac-ROS (Development) Container

For software development we will leverage the isaac_ros docker container. This container can be used for:

- ROS focused solutions (Using either python/C++ to publish/subscribe to the QCar 2 nodes)

Note: Isaac ROS is already installed on the QCar 2. You will only need to install the Nvidia Container Toolkit.

1. To get started please install [Nvidia-Container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-the-nvidia-container-toolkit)

    **_NOTE:_**  Make sure you install the [Debian-based installation for the toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#with-apt-ubuntu-debian). And, do not set up the experimental packages repo. Then [Configure Your Docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-docker).

    During the installation of the `nvidia-container-toolkit` you may receive an error that the `nvidia-container-toolkit-base` package is mission. Please install it manually using the following command:

    ```bash
    sudo apt install nvidia-container-toolkit-base
    ```

2. [Configure Your Docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-docker). You can ignore the Rootless Mode instructions.

    **_NOTE:_**  You may need to add your local user to the local Docker Group. Please restart your machine once your user has been added.

## How to Run the ROS2 Humble Nodes

To ensure safe development, the QCar 2 nodes should not be touched and no packages should be installed on the native Ubuntu. Instead, you will install packages on the Isaac-ROS container and write scripts within the container that will communicate with the ROS nodes running natively. This structure will look like the following:

![Development Structure](https://github.com/quanser/ACC-Competition-2025/blob/stage2/Software_Guides/Pictures/software_architecture_stage2.png)

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

    There may be some warnings, but these can be ignored.

5. Copy the compiled ROS nodes and interfaces to the container so that the container has access to the messages the QCar nodes are using:

    ```bash
    cp -r ~/ros2/install/ ~/Documents/ACC_Development/dev/
    ```

6. Source the recently compiled ROS packages:

    ```bash
    source install/setup.bash
    ```

7. Run the nodes using the following command:

    ```bash
    ros2 launch qcar2_nodes qcar2_launch.py
    ```

8. Open an Isaac-ROS container in a NEW terminal using the following commands:

    ```bash
    cd /home/$USER/Documents/ACC_Development/isaac_ros_common
    ./scripts/run_dev.sh  /home/$USER/Documents/ACC_Development/dev
    ```

    Note: To open additional terminals, run the above 2 commands in a new terminal.

9. Source ROS

    ```bash
    source . install/setup.bash
    ```

10. Open RViz2:

    ```bash
    rviz2
    ```

11. Add 'By Topic' relevant topics such as /laserscan. For /laserscan, switch the Fixed frame to `base_scan`

**IMPORTANT:** For tips and guides on how to develop in this container, visit the [Devlopment Guide](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Guides/Development%20Guide.md).
