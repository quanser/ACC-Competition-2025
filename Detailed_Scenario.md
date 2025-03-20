# Detailed Scenario <!-- omit in toc -->

Since the definitition of the video submission has been vague, the development team wanted to provide the teams with a clear objective to shoot for and surpass. This objective is represented in [this video](https://youtu.be/NtgBwlfGbMc).

Below is a step-by-step sequence of events that are representative of what will be tested during Stages 2 and 3 of the competition. It is still expected that teams communicate important aspects of their algorithm throughout their video submission.

## Scenario

1. Run the [Setup_Real_Scenario.py](https://github.com/quanser/ACC-Competition-2025/blob/main/Docker/virtual_qcar2/python/Base_Scenarios_Python/Setup_Real_Scenario.py) file. This will spawn the QCar 2 in the Taxi Hub Area:
 
![Taxi Hub Area](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Guides/Pictures/TaxiHubArea.png)

2. Navigate to the pick-up coordinate [0.125, 4.395] (meters):

![Pick-Up coordinate](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Guides/Pictures/PickUpCoordinate.png)

3. Pause for 3 seconds to indicate that a passenger is being picked up. To make it more obvious that you are picking up a passenger, we recommend that teams change the RGB LED strip on the QCar 2.

4. Navigate to the drop-off coordinate [-0.905, 0.800] (meters):

![Drop Off Coordinate](https://github.com/quanser/ACC-Competition-2025/blob/main/Software_Guides/Pictures/DropOffCoordinate.png)

5. Pause for 3 seconds to indicate that a passenger is being dropped off. To make it more obvious that you are dropping off a passenger, we recommend that teams change the RGB LED strip on the QCar 2.

6. Navigate back to the Taxi Hub Area to await another ride.

**END OF SCENARIO**

**CHANGING LEDS**: The command for setting LEDs is below:

```bash
ros2 param set qcar2_hardware led_color_id <value>
```

They are formatted as `0: red , 1: green, 2: blue, 3: yellow , 4: cyan , 5: magenta`.

## Base Coordinate Frame

As mentioned in the Handbook, the base coordinate frame for the competition is the origin of the competition map. This is also the origin of the QLabs world and is shown here:

![OriginOfTheBaseCoordinateFrame]()

All coordinates given will be with respect to this origin.

## Expectatations

When the judges are viewing the video submissions, they will be watching for the following, but not limited to:

1. Cars crossing over lane lines.
2. Cars not fully stopping at traffic controls.
3. Timely reactions to traffic controls.
4. Properly stopping to pick-up and drop-off passengers.
5. Avoiding any obstacles.
6. Moving as fast as possible (moving as fast as possible will be important for stage 2 and 3)

It is important to keep in mind that this scenario only represents a single "ride". Stages 2 and 3 will require you to complete as many rides as possible in a certain time period.
