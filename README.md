<img src="https://github.com/quanser/ACC-Competition-2025/blob/stage2/Software_Guides/Pictures/accBannerv2.png" width="100%">

# Welcome to Stage 2 and 3 of the ACC 2025 Competition!

This Github Repo will host all the Stage 2 and 3 competition resources you will need to successfuly compete at the in-person event in Colorado.

To get started setting up your QCar 2 visit the following guide: [Physical QCar2 Software Setup](https://github.com/quanser/ACC-Competition-2025/blob/stage2/Software_Guides/physical_qcar2_software_setup_instructions.md)

## ❗ Stage 2 and 3 Announcements

- [Running Isaac-ROS container with no internet guide](https://github.com/quanser/ACC-Competition-2025/blob/stage2/Software_Guides/physical_qcar2_development_guide.md#how-to-run-the-isaac-ros-container-with-no-internet-connection) has been created
- For those who want to print the SDCS map, there is a detailed file here: [SDCS_Detailed_roadmap.pdf](https://github.com/quanser/ACC-Competition-2025/blob/stage2/Software_Guides/SDCS_detailed_roadmap.pdf). Dimensions for the map can be found in the appendix of the handbook.
- A [development guide](https://github.com/quanser/ACC-Competition-2025/blob/stage2/Software_Guides/physical_qcar2_development_guide.md) for the physical QCar 2 has been released
- The list of coordinates and example rides can be found here: [coordinates_and_rides.txt](https://github.com/quanser/ACC-Competition-2025/blob/stage2/Handbook/coordinates_and_rides_example.txt)
- It is very important that everyone participating looks at the [Handbook](https://github.com/quanser/ACC-Competition-2025/tree/stage2/Handbook)
- Post any issues in the [Discussions](https://github.com/quanser/ACC-Competition-2025/discussions) tab or the [Issues](https://github.com/quanser/ACC-Competition-2025/issues) tab. If it is competition details related you can email studentcompetition@quanser.com.

## 🪧 Stage 2 Objective

Each team will have access to a QCar 2 and will implement the algorithm they developed in Stage 1 on the physical hardware. All teams who were chosen to advance to Stage 2 will also advance to Stage 3. Stage 3 will be held in Denver, Colorado, USA. During Stage 2, teams will need to prepare to travel to the American Controls Conference, which will involve the following:

- Obtaining VISAs to The United States of America.
- Getting your team’s QCar 2 to the venue.

## 🪧 Stage 3 Objective

Stage 3 is the in-person event in Colorado at the ACC. There is a [section at the bottom](#details-of-a-ride) that contains the important information about completing rides during the competition. These details are more clearly laid out in the Stage 2 and 3 Handbook.

Your goal during Stage 3 will be to maximize the amount of money that you earn in a period of 5-minutes. Teams will receive a list of rides that they can take in the form of a .txt file. An example of this file has been provided here: [coordinates_and_rides.txt](https://github.com/quanser/ACC-Competition-2025/blob/stage2/Handbook/coordinates_and_rides_example.txt). These coordinates are denoted as numbers (i.e. 1, 2, 3, ect.). This list will not change for the competition. What will change is the list of rides at the bottom that are denoted by letters (i.e. A,B,C., ect.).

For each completed ride a team does, they will receive a rating. This rating will multiply the amount of money earned for a ride, so it is beneficial to follow the rules of the road. If there are too many infractions during a ride, the team will not receive any money for that ride! For more thorough details about the scoring please read the [Handbook](https://github.com/quanser/ACC-Competition-2025/tree/stage2/Handbook).

## ❓ FAQ

This [FAQ](https://github.com/quanser/ACC-Competition-2025/blob/stage2/Software_Guides/FAQ.md#faq--) is for questions that require a more detailed response and might be relevant to everyone. Also check the [open](https://github.com/quanser/ACC-Competition-2025/issues) and [closed](https://github.com/quanser/ACC-Competition-2025/issues?q=is%3Aissue%20state%3Aclosed) issues to see if your specific problem has been addressed.

## 📣 Discussions

Teams may discuss amongst each other in the [discussions](https://github.com/quanser/ACC-Competition-2025/discussions) tab of the Github.

We would also like you to post any issues with supplied resources if you find them so that other teams may help or a Quanser representative can address them!

## 🗄️ Resources

- [FAQ](https://github.com/quanser/ACC-Competition-2025/blob/stage2/Software_Guides/FAQ.md)
- [Handbook](https://github.com/quanser/ACC-Competition-2025/tree/stage2/Handbook)
- [Competition Resources](https://quanserinc.box.com/s/g2690n3jwbhquwr8uqdz0b45m5wx945z)
  - Password: acc2025denver
- [Competition Website](https://www.quanser.com/winners/2025-american-control-conference-self-driving-car-student-competition/)
- [Registration](https://forms.office.com/Pages/ResponsePage.aspx?id=Avj7Fe66dkyl9OR6d9iruwqgKheKAv1Bg6C4zWQQj3BUOFlBR0lITDA3VU9NN0VDUUtPNFBVUTgxVi4u) (Closed)
- [Quanser Interactive Labs Support Page](https://portal.quanser.com/Support)
- [Quanser Interactive Labs Documentation](https://qlabs.quanserdocs.com/en/latest/ )
- [Quanser Python API Documentation](https://docs.quanser.com/quarc/documentation/python/index.html)
- [Quanser C API Documentation](https://docs.quanser.com/quarc/documentation/hardware_reference_c.html)
- [Quanser QUARC Blocks for MALTAB/Simulink Documentation](https://docs.quanser.com/quarc/documentation/quarc_block_categories.html)

## Details of a Ride

The objective of the competition will be to maximize the amount of money earned by completing taxi rides within a certain amount of time. All teams will be given a .txt file that contains the different rides they can attempt. Rides can have multiple stops, which will add complexity. Teams will earn more money for more complex rides.

The first coordinate in a ride will always be the Pickup location. Teams must indicate a pickup by changing the QCar 2 LED strip to Blue and wait for clearly stop at the pickup location.

The last coordinate in a ride will always be the Drop Off location. Teams must indicate a drop off by changing the QCar 2 LED strip to Yellow and clearly stop at the drop off location.

Any coordinates in a ride that aren’t the first and last coordinates will be a Stop. Teams must indicate a stop by changing the QCar 2 LED strip to Red and clearly stop at the stop location.

**When driving between any coordinates**, teams must change their LED strip to Green.

The sequence of a single ride will consist of the following:

1. The QCar 2 will start in the Taxi Hub Area with Magenta LEDs and must be clearly stopped.
2. Teams will need to write down the ride number they are attempting and show the judges. A whiteboard or other device will be provided.
3. Teams will need to navigate to the pickup location with their LEDs Green.
4. Once the QCar 2 has arrived at the pickup location, it must clearly stop and change the onboard LED strip to Blue.
5. If there are any stops in the ride, teams will need to navigate to the stop location with Green LEDs, then come to a clear stop at the stop location and change the LED strip to Red.
6. For the final coordinate, teams will need to navigate to the drop off location with Green LEDs, then come to a clear stop at the drop off location and change the LED strip to Yellow.  
7. Once the drop off has been completed, teams will need to navigate back to the Taxi Hub Area with Green LEDs, come to a clear stop, and change their LEDs to Magenta to signal the end of the ride.

Once all the above steps have been completed, the judges will mark down the successful completion of a ride. The team will receive a preset dollar amount for the completion of the ride. The team will also receive a rating for the ride based on whether they followed the rules of the road correctly. Infractions will lower the rating the team receives. Please refer to the Handbook for details.

If the team feels they want to restart the ride or they think they have received too many infractions, they can pick up their QCar 2 and place it back in the Taxi Hub Area. Any time a team touches their QCar 2, it will disqualify that ride, and they must place it back in the Taxi Hub Area.

Teams may repeat the same ride number as many times as the wish. Only the best rated, completed ride for a specific ride number will contribute towards the total money earned. Any lower rated rides for the same ride number will be discarded.
