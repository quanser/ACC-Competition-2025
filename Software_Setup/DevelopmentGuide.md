# Development Guide for the Development Container <!-- omit in toc -->

This guide will provide instructions and tips for developing your self-driving algorithm in the Isaac-ROS Development Container.

Developing in a Docker container can be tricky since everytime the container is restarted, all files and actions that took place in the container get reset.

The topics are listed below and will be updated with new information periodically:

- [How to create files that persist in the container](#how-to-create-files-that-persist-in-the-container)
- [How to add Python packages via `pip3` that persist](#how-to-add-python-packages-via-pip3-that-persist)


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

## How to add Python packages via `pip3` that persist

Any packages that get installed via `pip3` in the command line of the Development Container do not persist once the container is closed. When you are installing packages in the terminal make sure to edit the Docker file called **Dockerfile.quanser**. This Docker file is used to configure the Development container and can be found in the following folder:

```bash
cd /home/$USER/Documents/ACC_Development/docker
```

At the bottom of the `# Install system libraries that quanser-sdk depends on` comment, begin installing your Python packages as shown below:

```bash
# Install system libraries that quanser-sdk depends on
RUN apt-get update && apt-get install -y \
    libasound2-dev \
    libsndfile1-dev \
    libavcodec-dev \
    libavformat-dev \
    libglib2.0-dev \
    libfreenect-dev \
    && rm -rf /var/lib/apt/lists/*

RUN cp /usr/local/bin/pip3.8 /usr/bin/

# Install Python Packages if necessary
RUN pip3 install -U \
    pytransform3d \
    pyqtgraph
```

This example will install pytransform3d and pyqtgraph everytime the container is started. **As you develop in the Development Container**, make sure you record any packages installed via `pip3` in the Docker file mentioned above.

**IMPORTANT:** If you ever download the ACC_Resources.zip file and run the `setup_linux.py` file again, this will create a new ACC_Development folder and record a backup of your previous one. Make sure to copy any changes made to `Dockerfile.quanser` over to the new ACC_Development folder.
