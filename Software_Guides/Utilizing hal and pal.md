# Utilizing `hal` and `pal` in the Development Container <!-- omit in toc -->

Two Python libraries from Quanser's standard resources are included in the Development Container by default, `hal` and `pal`. **Files have been modified** from the standard Quanser resources to make them compatible in Linux. You can view how they are added into the Development Container at the bottom of the `docker.quanser` file.

`hal` stands for high-level applications library and contains userful functions like EKF's, image processing, and controllers.

`pal` stands for product application library and contains userful QCar functions like creating a QCar class that can read and write information to the QCar, and other classes for interfacing with the lidar and cameras.

This guide will cover all the information necessary to utilize the `hal` and `pal` libraries in the Development Container.

- [Location of Libraries](#location-of-libraries)
- [Modifying `hal/pal`](#modifying-halpal)
- [Examples using `hal/pal`](#examples-using-halpal)

## Location of Libraries

`hal/pal` are downloaded as part of the ACC_Resources. They are stored within:

```bash
cd /home/$USER/Documents/ACC_Development/docker/libraries/python
```

Everytime the Development Container is started, it will pull these libraries into the Development Container here:

```bash
cd /home/Quanser/libraries/python
```

## Modifying `hal/pal`

Whenever you would like to modify `hal/pal`:

1. Make changes to them in the Development Environment.
2. Test that the changes work.
3. Extract the libraries from the Container.
4. Replace the `hal/pal` in `/home/$USER/Documents/ACC_Development/docker/libraries/python` outside of the container.

## Examples using `hal/pal`

For those of you that are using only Python, some example code has been provided in the following folder:

```bash
cd /home/$USER/Documents/ACC_Development/Development/python_dev
```

This code will be copied into the Development Container here:

```bash
cd /workspaces/isaac_ros-dev/python_dev
```

We have included the basic hardware tests that showcase how to interface with the QCar 2. There is also a more complex application called vehicle control which utilizes many classes within `hal/pal` and is intended to be run after spawning the QCar 2 via `Setup_Competition_Map.py` in the Quanser Virtual Environment Docker Container.

```bash
/workspaces/isaac_ros-dev/python_dev
                                L QCar2_hardware_test_basic_io.py
                                L QCar2_hardware_test_csi_cameras.py
                                L QCar2_hardware_test_intelrealsense.py
                                L QCar2_hardware_test_rp_lidar_a2.py
                                L vehicle_control.py
```

**NOTE:** Vehicle Control has been modified from the original lab in the standard resources so that it works in the Development Container.
