# ROS 2/Python setup for ACC Competition

## Description: 
Welcome to then ACC Quanser Self-Driving Car Student Competition - software setup!
In this document we will describe:
- System requirements for the virtual portion of the ACC competition
- How to setup your system before starting the competition
- Considerations while doing software development 

## Prerequisites 

Linux System based requirements:

- Ubuntu 24.04 LTS
- ROS 2 Humble 
- Nvidia Based GPU 

Please follow this guide to correctly setup Docker engine on your ground station PC:
https://docs.docker.com/engine/install/ubuntu/ 

Setting up the software environment: 

1. Download the ACC resources available from Quanser [ACC Resources](https://quanserinc.box.com/shared/static/aobhyo9fwv5otzfb87i4ccos1nxfn2rz.zip).

2. Extract the content of ACC_Resources folder inside the Downloads folder. 

If you are using windows it is assumed the files you're using will be for MATLAB. Please look inside the qcar virtual 

For LINUX Systems:
1. run the setup_linux.py to configure your development environment

How your system should look like: 
``` bash
/home/$USER/Documents/ACC_Development/ 
                        L ros2/
                        L isaac_ros_common/
                        L docker/
                        L dev/
                        L backup/
```
This development folder will be used to save your work done inside Quanser's Docker container and/or the Isaac ROS development container. 

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
* qlabs_reset (Necessary in the case your experiment failed and would like to reset the virtual environment to default) 
* qlabs_stop (In the case you would like to gracefully close all virtual assets and close your system) 

You will find the python reset and stop under the folder /home/qcar2_scripts/python.

## Development Container Setup:

For software development we will leverage the isaac_ros docker container. This container can be used for:
- Python only work (Not using ROS)
- ROS focused solutions (Using either python/C++ to write ROS nodes) 

1. To get started please install [Nvidia-Container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-docker) 

**_NOTE:_**  If you're not sure what method to use, we recommend you follow the instruction for installing with Apt. 

2. you can find the content of the isaac_ros container by going to /home/$USER/Documents/ACC_Development/isaac_ros_common/
3. To start the container use the command 

 ``` .scripts/run_dev.sh  /home/$USER/Documents/ACC_Development/ros2  ``` 

**_NOTE:_**  You may need to add your local user to the local Docker Group. Please restart your machine once your user has been added. 

    
## Getting started:

Once you are aready to start developing reset the virtual environment:

1. Using the Qunaser's custom container type: python3 qlabs_reset.py 

ROS Specific instructions: 

1. Compile the QCar2 ros nodes using colcon build 
2. Source the QCar2 packages using  
```. /install/setup.bash``` 
3. Launch the nodes for the QCar using the launch file configured for the virtual QCar \
 ``` ros2 launch qcar2_nodes qcar_launch_virtual.py  ```

