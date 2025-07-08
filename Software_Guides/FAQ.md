# ❓FAQ ❓ <!-- omit in toc -->

This FAQ is for questions that require a more detailed response and might be relevant to everyone. Also check the [open](https://github.com/quanser/ACC-Competition-2025/issues) and [closed](https://github.com/quanser/ACC-Competition-2025/issues?q=is%3Aissue%20state%3Aclosed) issues to see if your specific problem has been addressed.

- [How can I control the Traffic Light](#how-can-i-control-the-traffic-light)
- [How can I change my ROS\_DOMAIN\_ID?](#how-can-i-change-my-ros_domain_id)

## How can I control the Traffic Light

Please refer to the Web API portion of the following document: [TrafficLight_UserManual](https://github.com/quanser/Quanser_Academic_Resources/blob/dev-windows/3_user_manuals/traffic_light/user_manual_traffic_light.pdf).

## How can I change my ROS_DOMAIN_ID?

Anybody who uses the same ROS_DOMAIN_ID can publish commands and data to your QCar 2 if you are on the same network. By default, your ROS_DOMAIN_ID is 0.

You can change your ROS_DOMAIN_ID by setting it as an environment variable in the `.bashrc`.

For the 2025 ACC competition, the following is the ROS_DOMAIN_ID assignments:

![ROS_DOMAIN_IDs](https://github.com/quanser/ACC-Competition-2025/blob/stage2/Software_Guides/Pictures/ROSDomainIDsACC2025.png)