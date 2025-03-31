# Running Nav 2 on the QCar 2 <!-- omit in toc -->

This guide will cover the commands and procedure for running the Nav 2 ROS package and setting a goal pose for the QCar 2.

- [Setup](#setup)
- [Setting the Goal Pose for the QCar 2](#setting-the-goal-pose-for-the-qcar-2)

## Setup

Make sure that you have gone through the entire [ACC Software Setup Instructions](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Guides/ACC%20Software%20Setup%20Instructions.md) before continuing with this guide.

1. Open QLabs to the Plane World.
2. Open a new terminal (CTRL + ALT + T) and run the Quanser Virtual Environment Container.

    ```bash
    cd /home/$USER/Documents/ACC_Development/docker/virtual_qcar2
    sudo docker run --rm -it --network host --name virtual-qcar2 quanser/acc2025-virtual-qcar2 bash
    ```

3. Spawn the QCar in the competition environment by running the following commands in the Quanser Virtual Environment Container:

    ```bash
    cd /home/qcar2_scripts/python
    python3 Base_Scenarios_Python/Setup_Competition_Map.py
    ```

4. Open a new terminal and start the Development Container in it.

    ```bash
    cd /home/$USER/Documents/ACC_Development/isaac_ros_common
    ./scripts/run_dev.sh  /home/$USER/Documents/ACC_Development/Development
    ```

5. Build and source the nodes in ROS2.

    ```bash
    colcon build && . install/setup.bash
    ```

6. Run the Nav2 launch file.

    ```bash
    ros2 launch qcar2_nodes qcar2_slam_and_nav_bringup_virtual_launch.py
    ```

7. Open a new terminal and attach the terminal to the Development Container.

    ```bash
    cd /home/$USER/Documents/ACC_Deverviz2lopment/isaac_ros_common
    ./scripts/run_dev.sh  /home/$USER/Documents/ACC_Development/Development
    ```

8. Open `rviz2`.

    ```bash
    rviz2
    ```

9. Add the following topics to the Display. Click on `add` in the bottom left of `rviz2`. `TF` will be under `By display type`. `LaserScan` and `Map` will be under `By topic`.

    ```bash
    Display
        L TF
        L LaserScan
        L Map
    ```

![Rviz2PictureofAddingTopicstoDisplay](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Guides/Pictures/rviz2AddingTopics.png)

## Setting the Goal Pose for the QCar 2

1. In `rviz2` select the `2D Goal Pose`.

![Selecting2DGoalPose](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Guides/Pictures/rviz2SetPoseButton.png)

2. Click and drag within the gridded area to set the goal pose and orientation. A green arrow should appear and show your selection.

If you navigate back to QLabs, you should see that the QCar 2 has begun moving towards the goal location.
