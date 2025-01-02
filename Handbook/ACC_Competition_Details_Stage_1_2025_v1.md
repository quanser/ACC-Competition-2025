<img src="media/image1.png" style="width:6.4625in;height:6.45278in" />

**Stage 1 Handbook**

**ACC Competition 2025**

<img src="media/image2.png" style="width:2.40625in;height:0.6875in"
alt="Logo Description automatically generated" />© 2025 Quanser Inc.,
All rights reserved.

Quanser Inc.

119 Spy Court

Markham, Ontario

L3R 5H6

Canada

info@quanser.com

Phone: 19059403575

Fax: 19059403576

Printed in Markham, Ontario.

For more information on the solutions Quanser Inc. offers, please visit
the web site at:  
<http://www.quanser.com>

This document and the software described in it are provided subject to a
license agreement. Neither the software nor this document may be used or
copied except as specified under the terms of that license agreement.
Quanser Inc. grants the following rights: a) The right to reproduce the
work, to incorporate the work into one or more collections, and to
reproduce the work as incorporated in the collections, b) to create and
reproduce adaptations provided reasonable steps are taken to clearly
identify the changes that were made to the original work, c) to
distribute and publicly perform the work including as incorporated in
collections, and d) to distribute and publicly perform adaptations. The
above rights may be exercised in all media and formats whether now known
or hereafter devised. These rights are granted subject to and limited by
the following restrictions: a) You may not exercise any of the rights
granted to You in above in any manner that is primarily intended for or
directed toward commercial advantage or private monetary compensation,
and b) You must keep intact all copyright notices for the Work and
provide the name Quanser Inc. for attribution. These restrictions may
not be waved without express prior written permission of Quanser Inc.

ACC Self-Driving Competition

Stage 1 Competitor Guide

ACC Self-Driving Competition

In recent years, Self-Driving has become increasingly prevalent around
the world. With the advent of Self-Driving cars hitting the roads, the
demand for research behind Self-Driving is at an all-time high and
algorithms need to be validated for safety and reliability. There are an
infinite number of situations encountered daily by drivers that can vary
drastically. An algorithm needs to be able to identify the scenario and
accurately respond with a correct behavior. At their core, Self-Driving
cars excel or are held back in their capacity for autonomy by their
knowledge and understanding of the state of the environment surrounding
the car. The ACC competition presents a great opportunity to showcase
world-class driving algorithms running in a safe and approachable manner
at a 1/10<sup>th</sup> scale and in a virtual setting.

Competition Overview

In this year’s competition, teams will try to maximize their profits as
an autonomous taxi service. They will need to navigate through the city
to selected pick-up and drop-off coordinates. During the trip, they will
encounter different traffic scenarios that they will need to solve while
adhering to the rules of the road. Depending on their performance during
the trip, the teams will receive a rating for the executed ride that
will influence the amount of money earned for the completion of the
ride. Students will then receive additional ride requests and will try
to maximize the amount of money they earn within a fixed timeframe.

The three stages of the competition are outlined below:

**Stage 1**: Virtual Design and Submission

**Stage 2:** Implementation of Self-Driving algorithm on the Physical
QCar 2

**Stage 3:** On-site Competition

All registrants will gain access to the Stage 1 virtual design phase,
where a team’s skills will be tested in Quanser’s virtual environment.
**The top 6 teams**, **based on selected criteria,** **will be chosen to
move on to the second and third stages of the competition**.

In stage 2, the selected teams will receive a physical QCar 2 from
Quanser and implement their Self-Driving algorithms on the physical
QCar. They will then be **required to bring their QCar 2** to the
competition venue and compete live against other selected teams.

More details will be released about stages 2 and 3 in a subsequent
handbook.

Competition Schedule

|                         |               **Description**               |
|-------------------------|:-------------------------------------------:|
| January 1<sup>st</sup>  |         Stage 1 Registration Opens          |
| February 1<sup>st</sup> |               Stage 1 Begins                |
| April 30<sup>th</sup>   |                Stage 1 Ends                 |
| May 7<sup>th</sup>      | Teams will be selected to move onto Stage 2 |
| TBD (in July)           |                   Stage 3                   |

Stage 1: Virtual Design and Submission

Overview

As a registered student team, you automatically participate in stage 1.
This is a qualifying stage so please submit your best result!

Teams will receive access to the QCar 2 digital twin, available through
Quanser Interactive Labs (QLabs). The digital twin provides access to
all the same sensors and actuators that are on the physical QCar 2.
These sensors will behave in the same manner that the physical does and
are accessed through the same APIs that the physical uses.

Teams will be provided with basic scenarios to test their Self-Driving
algorithms. These scenarios will serve as a starting point, but it is
encouraged to develop more complex scenarios to truly highlight the
capabilities of your Self-Driving algorithm for your video submission.
Custom environments can be created in QLabs, so we encourage teams to
get creative!

Teams will be ranked using the following criteria:

1.  Readiness of a Self-Driving algorithm based on the core principles
    as stated in the Core Principles of Self-Driving section.

2.  Accuracy of driving (staying within the lanes).

3.  Timely reaction to road signage and traffic controls while adhering
    to traffic laws as stated in the Traffic Controls Rules section.

4.  Clear and concise communication of Self-Driving concepts
    demonstrated in the video.

Core Principles of Self-Driving

**Data Collection**:

A Self-Driving algorithm must be able to collect and filter information
from interoceptive and exteroceptive sensors. Demonstrating the
conversion of raw data to meaningful information is critical for
Self-Driving cars to make higher-level decisions during an autonomous
task.

**Interpretation**:

Using system-relevant data, a Self-Driving car must correlate the
gathered information to factors happening internally or externally in
the environment. Examples of external factors include the identification
of traffic signs, traffic lights, pedestrians, and other cars. Examples
of internal data include battery monitoring and system state
identification.

**Control Systems**:

From the set of viable options determined in the interpretation of the
world, the car must be able to execute accurately on the chosen option.
This includes staying within lanes, executing turns, stopping at traffic
controls, altering a path based on an obstacle, and maintaining a
desired speed.

**Localization and Path Planning**:

For a car to arrive at pick-up and drop-off locations, it must
understand where it is within the roadmap. This may involve storing a
global or local map of the environment in memory. A successful driving
algorithm should be able to determine where it is in space and how to
get to another location on the competition roadmap. It must also be able
to adjust the selected route based on information obtained on its trip
such as vehicles on the road, road obstructions, and pedestrians
entering/leaving the roadway.

Software Compatibility Requirements

**Important: It is expected that teams will use Linux and ROS 2. Any
other languages used are allowed but will not be supported.**

**Linux:**

If using Linux, teams are required to use **Ubuntu 20.04** since this is
the Ubuntu version that is on the QCar 2.

**Python:**

During the virtual stage 1 students must use **Python 3.11.4** since
this is the Python version that is installed with the QCar 2 resources
provided.

IMPORTANT NOTE: During stages 2 and 3, the Physical QCar 2 has **Python
3.8.10** installed on it. This version of Python **CANNOT** change.
Ensure that your code in the Stage 1 submission is compatible with
Python 3.8.10. Avoid packages that will not be compatible since they
will not work using a physical QCar 2 in stages 2 and 3!

**ROS:**

The ROS nodes supplied are for ROS 2 Humble.

Submission requirements

1.  For **Stage 1** teams may use any of the following software:

    1.  Python 3.11.4

    2.  ROS 2 Humble

    3.  MATLAB/Simulink

    4.  C++

> The above software must comply with the Software Compatibility
> Requirements section above.

2.  Maximum 3-minute video demonstration of the Self-Driving
    capabilities and explanations.

3.  Submission must provide the following:

    1.  Software: **GitHub** **link** to the repository with your team’s
        submission. The code will be run by a Quanser engineer to
        validate performance.

    2.  Video: **YouTube link** demonstrating your code.

Technical Information

Getting Started

Follow the below steps to get set up for the competition:

1.  Create a Quanser Interactive Labs account here: [Create Quanser
    Interactive Labs
    Account](https://portal.quanser.com/Accounts/Login?returnUrl=/).

2.  Use [QLabs Installation](https://portal.quanser.com/Downloads) to
    download and install QLabs on your system.

    1.  If using MATLAB use the following link to install QLabs: [Matlab
        QLabs Installation
        Instructions](https://quanserinc.sharepoint.com/sites/CustomerSuccess/Shared%20Documents/ACC_Competition/Matlab%20QLabs%20Installation%20Instructions).

3.  Download the SDCS Resources containing QCar 2 resources from here:
    [QCar
    Resources](https://quanserinc.box.com/shared/static/hb3t1xj1zw8t8a191ao8mrdcyjc1nhd6.zip)

4.  Explore!

Available Documentation

1.  Information for interacting with the virtual environment: [QLabs
    Documentation](https://qlabs.quanserdocs.com/en/latest/)

2.  Python API Documentation: [Python
    API](https://docs.quanser.com/quarc/documentation/python/index.html)

3.  C API Function Documentation: [C
    API](https://quanserinc.sharepoint.com/sites/CustomerSuccess/Shared%20Documents/ACC_Competition/C%20API)

4.  Current examples released for the Self-Driving Car Studio: [QCar
    Resources](https://quanserinc.box.com/shared/static/aobhyo9fwv5otzfb87i4ccos1nxfn2rz.zip)

    1.  Password is: acc2025denver

5.  Competition webpage:
    [Competition](https://quanserinc.sharepoint.com/sites/CustomerSuccess/Shared%20Documents/ACC_Competition/Competition)

Stage 1 Virtual Scenarios

There will be 7 base scenarios that are provided for the virtual world
as follows:

1.  Setup_Base_Scenario_stop_ACC_Competition_2025

2.  Setup_Base_Scenario_yield_ACC_Competition_2025

3.  Setup_Base_Scenario_trafficLight_ACC_Competition_2025

4.  Setup_Base_Scenario_trafficCone_ACC_Competition_2025

5.  Setup_Base_Scenario_roundabout_ACC_Competition_2025

6.  Setup_Base_Scenario_pedestrian_ACC_Competition_2025

7.  Setup_Competition_Map

These scenarios serve as a basis for how teams can test their code. They
can also be used as examples of how to spawn in different objects and
create custom scenarios!

**Tip: When designing custom scenarios, it is helpful to use the
coordinate tool to spawn actors:**

<img src="media/image3.png" style="width:6.5in;height:3.49583in" />

Figure : Coordinate Tool

Coordinate System

In the Stage 2 & 3 of the competition, a series of coordinates will be
provided to teams indicating pick-up and drop-off locations. The
coordinate system is defined as follows:

- The coordinate system’s origin will coincide with the origin in the
  Quanser Interactive Labs Cityscape world:

> <img src="media/image4.png" style="width:6.5in;height:3.49097in"
> alt="A screenshot of a video game Description automatically generated" />

Figure : Origin of the Coordinate System

- The map used in this world is full scale, and a 1/10<sup>th</sup>
  scale map will be used for the physical portion of the competition.

Traffic Controls Rules

All traffic control rules will be based on The Official Ministry of
Transportation (MTO) Driver’s Handbook which can be found here:

[**The Official Ministry of Transportation (MTO) Driver’s
Handbook**](https://www.ontario.ca/document/official-mto-drivers-handbook)

© Quanser Inc. All rights reserved.

<img src="media/image5.png" style="width:2.40625in;height:0.69107in"
alt="Logo, company name Description automatically generated" />

Solutions for teaching and research. Made in Canada.
