# ❓FAQ ❓ <!-- omit in toc -->

This FAQ is for questions that require a more detailed response and might be relevant to everyone. Also check the [open](https://github.com/quanser/ACC-Competition-2025/issues) and [closed](https://github.com/quanser/ACC-Competition-2025/issues?q=is%3Aissue%20state%3Aclosed) issues to see if your specific problem has been addressed.

- [How can I reset the entire setup of my resources?](#how-can-i-reset-the-entire-setup-of-my-resources)
- [QCar 2 won't spawn in the open plane](#qcar-2-wont-spawn-in-the-open-plane)
- [Hardware requirements and performance expectations](#hardware-requirements-and-performance-expectations)
- [What are my camera intrinsics?](#what-are-my-camera-intrinsics)
- [What are the transformation matrices between the different sensors?](#what-are-the-transformation-matrices-between-the-different-sensors)

## How can I reset the entire setup of my resources?

This is an important troubleshooting step since changes are constantly being made to the resources to fix different issues. Always try this as a first step if you are experiencing issues with the installation instructions
in the ACC Software Instructions document.

Please do the following:

- Download the latest [ACC Resources](https://quanserinc.box.com/s/g2690n3jwbhquwr8uqdz0b45m5wx945z)
- Unzip the folder
- Run the setup_linux.py file

```bash
python3 setup_linux.py
```

- Run the following command to **uninstall** all resources:

```bash
sudo apt purge --auto-remove qlabs-unreal quanser-sdk quarc-runtime
```

- Run the following commands to **reinstall** all resources:

```bash
wget --no-cache https://repo.quanser.com/debian/prerelease/config/configure_repo_prerelease.sh
chmod u+x configure_repo_prerelease.sh
./configure_repo_prerelease.sh
rm -f ./configure_repo_prerelease.sh
```

```bash
sudo apt update
```

```bash
sudo apt-get install qlabs-unreal python3-quanser-apis  quarc-runtime
```

- Update the Docker container:

```bash
docker pull quanser/acc2025-virtual-qcar2:latest
```

Once you do this, try running the containers again and the nodes.

## QCar 2 won't spawn in the open plane

This was previously caused by an error on the back-end of QLabs. This has since been fixed, but if you are still experiencing this issue it may be because your QLabs has cached your current session.
Please try logging out and logging back in to fix the issue.

This can be caused by you not being logged in with the email address you used to register for the competition. Please talk to your team captain about which email address they submitted to the competition.

If it persists please raise an issue in the [issue tab](https://github.com/quanser/ACC-Competition-2025/issues).

## Hardware requirements and performance expectations

The development team has been testing the resources on an RTX 2060 Max-Q GPU, i9-10980HK, and 32GB of RAM. The performance that we receive is ~120fps and ~13cps when limiting the framerate to 200fps in the advanced graphics settings. These results were obtained when running all ROS2 nodes and spawning the QCar 2 in the Plane world.

To see the performance of your machine do the following:

- In the main page of QLabs click on settings
- Turn on 'show advanced options':
![Turning on Advanced Settings](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Guides/Pictures/TurnOnAdvancedOptions.png)

- Navigate to the Plane world in QLabs
- Turn on 'show comms per second' and 'show frames per second' in the settings:
![Turning on CPS and FPS](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Guides/Pictures/TurnOnCPSnFPS.png)

## What are my camera intrinsics?

The following camera intrinsics can be used in your algorithms if necessary:

```python
# CSI camera intrinsic matrix at resolution [820, 410] is:
[[318.86    0.00  401.34]
[  0.00  312.14  201.50]
[  0.00    0.00    1.00]]

# CSI camera distorion paramters at resolution [820, 410] are:
[[-0.9033  1.5314 -0.0173 0.0080 -1.1659]]

# D435 RGB camera intrinsic matrix at resolution [640, 480] is:
[[455.20    0.00  308.53]
[  0.00  459.43  213.56]
[  0.00    0.00    1.00]]

# D435 RGB camera distorion paramters at resolution [640, 480] are:
[[-5.1135e-01  5.4549 -2.2593e-02 -6.2131e-03 -2.0190e+01]]
```

## What are the transformation matrices between the different sensors?

It is important to know where each of the sensors is with respect to each other so that data can be unified correctly. There are transformation matrices in the **hardware user manual** that tell this information. The user manuals for the QCar 2 are in the following directory:

```bash
cd /home/$USER/Documents/ACC_Development/backup/src/user_manuals/qcar2
```
