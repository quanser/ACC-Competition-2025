## Core Principles of Self-Driving 🚗
👀 <strong>Data Collection:</strong>
A Self-Driving algorithm must be able to collect and filter information from interoceptive and exteroceptive sensors. Demonstrating conversion of raw data to meaningful information is critical for Self-Driving cars to make higher level decisions during an autonomous task.

💻 <strong>Interpretation:</strong>
Using system relevant data, a Self-Driving car must correlate the gathered information to factors happening internally or externally in the environment. Examples of external factors include identification of traffic signs, traffic lights, pedestrians, and other cars. Examples of internal data include battery monitoring, system state identification.

🏎️ <strong>Control Systems:</strong>
From the set of viable options determined in the interpretation of the world, the car must be able to execute accurately on the chosen option. This includes staying within lanes, executing turns, stopping at traffic controls, altering a path based on an obstacle, and maintaining a desired speed. 

🗺️ <strong>Localization and Path Planning:</strong>
For a car to arrive at pick up and drop off locations, it must understand where it is within the roadmap. This may involve storing a global or local map of the environment in memory. A successful driving algorithm should be able to determine where it is space and how to get to another location on the competition roadmap. It must also be able to adjust the selected route based on information obtained on its trip such as vehicles on the road, road obstructions and pedestrians entering/leaving the roadway.
