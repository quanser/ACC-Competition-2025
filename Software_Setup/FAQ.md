# ❓FAQ ❓

This FAQ is for questions that require a more detailed response and might be relevant to everyone. 

- [How can I reset the entire setup of my resources?](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Setup/FAQ.md#how-can-i-reset-the-entire-setup-of-my-resources)
- [QCar 2 won't spawn in the open plane](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Setup/FAQ.md#how-can-i-reset-the-entire-setup-of-my-resources)
- [Hardware requirements and performance expectations](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Setup/FAQ.md#hardware-requirements-and-performance-expectations)

## How can I reset the entire setup of my resources?

This is an important troubleshooting step since changes are constantly being made to the resources to fix different issues. Always try this as a first step if you are experiencing issues with the installation instructions
in the ACC Software Instructions document.

Please do the following:

- Download the latest [ACC Resources](https://quanserinc.box.com/s/g2690n3jwbhquwr8uqdz0b45m5wx945z)
- Unzip the folder
- Run the setup_linux.py file
```
python3 setup_linux.py
```
- Run the following command to <strong>uninstall</strong> all resources:
```
sudo apt purge --auto-remove qlabs-unreal quanser-sdk quarc-runtime
```
- Run the following commands to <strong>reinstall</strong> all resources:
```
wget --no-cache https://repo.quanser.com/debian/prerelease/config/configure_repo_prerelease.sh
chmod u+x configure_repo_prerelease.sh
./configure_repo_prerelease.sh
rm -f ./configure_repo_prerelease.sh
```
```
sudo apt update
```
```
sudo apt-get install qlabs-unreal python3-quanser-apis  quarc-runtime
```
- Update the Docker container:
```
docker pull quanser/acc2025-virtual-qcar2:latest
```
## QCar 2 won't spawn in the open plane
This was previously caused by an error on the back-end of QLabs. This has since been fixed, but if you are still experiencing this issue it may be because your QLabs has cached your current session.
Please try logging out and logging back in to fix the issue. If it persists please raise an issue in the [issue tab](https://github.com/quanser/ACC-Competition-2025/issues).

## Hardware requirements and performance expectations
The development team has been testing the resources on an 4060 GPU, i7-12700KF, and 32GB of RAM. The performance that we receive is ~120fps and ~13cps when limiting the framerate to 200fps in the advanced graphics settings. These results were obtained when running all ROS2 nodes and spawning the QCar 2 in the Plane world.

To see the performance of your machine do the following:
- In the main page of QLabs click on settings
- Turn on 'show advanced options':
![Turning on Advanced Settings](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Setup/Pictures/TurnOnAdvancedOptions.png)

- Navigate to the Plane world in QLabs
- Turn on 'show comms per second' and 'show frames per second' in the settings:
![Turning on CPS and FPS](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Setup/Pictures/TurnOnCPSnFPS.png)
