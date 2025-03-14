# Detailed Scenario

Since the definitition of the video submission has been vague, the development team wanted to provide the teams with a clear objective to shoot for and surpass. This objective is represented in [this video](https://youtu.be/NtgBwlfGbMc).

Below is a step-by-step sequence of events that are representative of what will be tested during Stages 2 and 3 of the competition. It is still expected that teams communicate important aspects of their algorithm throughout their video video.

## Scenario

1. Run the [Setup_Real_Scenario.py](https://github.com/quanser/ACC-Competition-2025/blob/main/Docker/virtual_qcar2/python/Base_Scenarios_Python/Setup_Real_Scenario.py) file. This will spawn the QCar 2 in the Taxi Hub Area:
 
![Taxi Hub Area](TaxiHubArea.png)

2. Navigate to the pick-up coordinate [0.125, 4.395] (meters):

![Pick-Up coordinate](PickUpCoordinate.png)

3. Pause for 3 seconds to indicate that a passenger is being picked up. To make it more obvious that you are picking up a passenger up we recommend that teams change the RGB LED strip on the QCar 2.

4. Navigate to the drop-off coordinate [-0.905, 0.800] (meters):

![Drop Off Coordinate](DropOffCoordinate.png)

5. Pause for 3 seconds to indicate that a passenger is being dropped off. To make it more obvious that you are dropping off a passenger up we recommend that teams change the RGB LED strip on the QCar 2.

6. Navigate back to the Taxi Hub Area to await another ride.

**END OF SCENARIO**
