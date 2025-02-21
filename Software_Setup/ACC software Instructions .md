# ROS 2/Python Setup for ACC Competition

## Description: 
Welcome to the ACC Quanser Self-Driving Car Student Competition - software setup!
In this document we will describe:
- System requirements for the virtual portion of the ACC competition
- How to setup your system before starting the competition
- Considerations while doing software development 

## Prerequisites 

Linux System based requirements:

- Ubuntu 24.04 LTS
- ROS 2 Humble 
- Nvidia Based GPU 

Please follow this guide to correctly setup Docker engine on your ground station PC: \
https://docs.docker.com/engine/install/ubuntu/ 

Setting up the software environment: 

1. Download the ACC resources available from Quanser [ACC Resources](https://quanserinc.box.com/s/g2690n3jwbhquwr8uqdz0b45m5wx945z).

2. Extract the content of ACC_Resources folder inside the Downloads folder. 

3. Run the setup_linux.py to configure your development environment

How your system should look like: 
``` bash 
/home/$USER/Documents/ACC_Development/ 
                        L ros2/
                        L isaac_ros_common/
                        L docker/
                        L dev/
                        L backup/
```
This development folder will be used to save your work done for the Isaac ROS development container. 

## Quanser Virtual Environment Container:

The purpose of this docker container is to ensure safe setup of the Quanser Interactive Labs virtual environment. 

1. Download the latest debian packages (only need to do once): 
``` bash 
wget --no-cache https://repo.quanser.com/debian/release/config/configure_repo.sh 
chmod u+x configure_repo.sh
./configure_repo.sh 
rm -f ./configure_repo.sh 
sudo apt update 
```
2. To install QLabs and Python and QUARC runtime 
` sudo apt-get install qlabs-unreal python3-quanser-apis  quarc-runtime ` 

3. Register an account in the [Quanser Academic Portal](https://portal.quanser.com/Accounts/Register) to obtain access for Quanser Interactive Labs

4. Navigate to the SDCS workspace, cityscape Lite   

5. To setup Quanser's custom python docker navigate to the folder `/home/$USER/Documents/ACC_Development/docker/virtual_qcar2` and run the following command: 

 ```sudo docker run --rm -it --network host --name virtual-qcar2 quanser/acc2025-virtual-qcar2 bash  ```

This docker container will include the following setup scripts:
 ``` bash
/home/qcar2_scripts/python 
                        L Base_Scenarios_Python/
```

## Development Container Setup:

For software development we will leverage the isaac_ros docker container. This container can be used for:
- Python only work (Not using ROS)
- ROS focused solutions (Using either python/C++ to write ROS nodes) 

1. To get started please install [Nvidia-Container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-docker) 

**_NOTE:_**  If you're not sure what method to use, scroll to the top of the page and follow the With apt: Ubuntu, Debian' section. You will not need to configure the repository to use experimental packages.

2. you can find the content of the isaac_ros container by going to the following directory: ```/home/$USER/Documents/ACC_Development/isaac_ros_common/```
3. To start the container use the command 

 ``` ./scripts/run_dev.sh  /home/$USER/Documents/ACC_Development/ros2  ``` 

**_NOTE:_**  You may need to add your local user to the local Docker Group. Please restart your machine once your user has been added. 

    
## Getting started:

Once you are ready to start developing, follow these steps to start the virtual environment:

1. Natively in Ubuntu, open the QLabs application and navigate to the SDCS then the Open Plane.
2. Using the Quanser Virtual Environment Docker container, navigate to the following directory: `cd /home/qcar2_scripts/python/`
3. Run the following Python script to spawn the competition map into QLabs: `python3 Base_Scenarios_Python/Setup_Competition_Map.py`

Once everything has run to completion, the QLabs world should look like the following:

![QLabs after running Setup_Competition_Map.py](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Setup/HowToStart.png "QLabs after running Setup_Competition_Map.py")

ROS Specific Instructions:  

These instructions focus on the content inside the isaac ros container. 
1. Compile the QCar2 ros nodes using \
```colcon build``` 
3. Source the QCar2 packages using \
```. install/setup.bash``` 
4. Launch the nodes for the QCar using the launch file configured for the virtual QCar \
 ``` ros2 launch qcar2_nodes qcar2_launch_virtual.py  ```

## How to stop the RT Model

When the Setup_Competition_Map.py file gets run, a real-time application (RT Model) is deployed that communicates with the virtual QCar 2. It is important to gracefully stop this model once you are no longer using your current workspace. Run the following commands to stop the RT Model:

1. Using the Quanser Virtual Environment Docker container, navigate to the following directory: ```cd /home/qcar2_scripts/python/```
2. To stop the RT Model run the following command: ```python3 qcar2_stop.py```

