# region: package imports
import os
import time


# environment objects

from qvl.qlabs import QuanserInteractiveLabs
from qvl.qcar2 import QLabsQCar2
from qvl.free_camera import QLabsFreeCamera
from qvl.real_time import QLabsRealTime
from qvl.basic_shape import QLabsBasicShape
from qvl.system import QLabsSystem
from qvl.walls import QLabsWalls
from qvl.qcar_flooring import QLabsQCarFlooring
from qvl.stop_sign import QLabsStopSign
from qvl.yield_sign import QLabsYieldSign
from qvl.roundabout_sign import QLabsRoundaboutSign
from qvl.crosswalk import QLabsCrosswalk
from qvl.traffic_light import QLabsTrafficLight

def main():

        # Try to connect to Qlabs

    os.system('cls')
    qlabs = QuanserInteractiveLabs()
    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
        print("Connected to QLabs")
    except:
        print("Unable to connect to QLabs")
        quit()

    # Delete any previous QCar instances and stop any running spawn models
    qlabs.destroy_all_spawned_actors()
    QLabsRealTime().terminate_all_real_time_models()


    setup(qlabs=qlabs, initialPosition = [-1.205, -0.83, 0.005], initialOrientation = [0, 0, -44.7])

    #spawing active components (traffic lights)
    # initialize 7 traffic light instances in qlabs
    trafficLight1 = QLabsTrafficLight(qlabs)
    trafficLight2 = QLabsTrafficLight(qlabs)
    trafficLight3 = QLabsTrafficLight(qlabs)
    trafficLight4 = QLabsTrafficLight(qlabs)

    #intersection 1
    trafficLight1.spawn_id_degrees(actorNumber=1, location=[0.6, 1.55, 0.006], rotation=[0,0,0], scale=[0.1, 0.1, 0.1], configuration=0, waitForConfirmation=False)
    trafficLight2.spawn_id_degrees(actorNumber=2, location=[-0.6, 1.28, 0.006], rotation=[0,0,90], scale=[0.1, 0.1, 0.1], configuration=0, waitForConfirmation=False)
    trafficLight3.spawn_id_degrees(actorNumber=3, location=[-0.37, 0.3, 0.006], rotation=[0,0,180], scale=[0.1, 0.1, 0.1], configuration=0, waitForConfirmation=False)
    trafficLight4.spawn_id_degrees(actorNumber=4, location=[0.75, 0.48, 0.006], rotation=[0,0,-90], scale=[0.1, 0.1, 0.1], configuration=0, waitForConfirmation=False)

    intersection1Flag = 0

    print('Starting Traffic Light Sequence')

    while(True):

        #intersection 1

        if intersection1Flag == 0:
            trafficLight1.set_color(color=QLabsTrafficLight.COLOR_RED)
            trafficLight3.set_color(color=QLabsTrafficLight.COLOR_RED)
            trafficLight2.set_color(color=QLabsTrafficLight.COLOR_GREEN)
            trafficLight4.set_color(color=QLabsTrafficLight.COLOR_GREEN)

        if intersection1Flag == 1:
            trafficLight1.set_color(color=QLabsTrafficLight.COLOR_RED)
            trafficLight3.set_color(color=QLabsTrafficLight.COLOR_RED)
            trafficLight2.set_color(color=QLabsTrafficLight.COLOR_YELLOW)
            trafficLight4.set_color(color=QLabsTrafficLight.COLOR_YELLOW)

        if intersection1Flag == 2:
            trafficLight1.set_color(color=QLabsTrafficLight.COLOR_GREEN)
            trafficLight3.set_color(color=QLabsTrafficLight.COLOR_GREEN)
            trafficLight2.set_color(color=QLabsTrafficLight.COLOR_RED)
            trafficLight4.set_color(color=QLabsTrafficLight.COLOR_RED)

        if intersection1Flag == 3:
            trafficLight1.set_color(color=QLabsTrafficLight.COLOR_YELLOW)
            trafficLight3.set_color(color=QLabsTrafficLight.COLOR_YELLOW)
            trafficLight2.set_color(color=QLabsTrafficLight.COLOR_RED)
            trafficLight4.set_color(color=QLabsTrafficLight.COLOR_RED)

        intersection1Flag = (intersection1Flag + 1)%4

        time.sleep(5)



#Function to setup QLabs, Spawn in QCar, and run real time model
def setup(qlabs, initialPosition = [-1.205, -0.83, 0.005], initialOrientation = [0, 0, -44.7]):

    # Try to connect to Qlabs

    os.system('cls')
    qlabs = QuanserInteractiveLabs()
    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
        print("Connected to QLabs")
    except:
        print("Unable to connect to QLabs")
        quit()

    # Delete any previous QCar instances and stop any running spawn models
    qlabs.destroy_all_spawned_actors()
    QLabsRealTime().terminate_all_real_time_models()

    #Set the Workspace Title
    hSystem = QLabsSystem(qlabs)
    x = hSystem.set_title_string('ACC Self Driving Car Competition', waitForConfirmation=True)

    ### Flooring

    x_offset = 0.13
    y_offset = 1.67
    hFloor = QLabsQCarFlooring(qlabs)
    hFloor.spawn_degrees([x_offset, y_offset, 0.001],rotation = [0, 0, -90])


    ### region: Walls
    hWall = QLabsWalls(qlabs)
    hWall.set_enable_dynamics(False)

    for y in range (5):
        hWall.spawn_degrees(location=[-2.4 + x_offset, (-y*1.0)+2.55 + y_offset, 0.001], rotation=[0, 0, 0])

    for x in range (5):
        hWall.spawn_degrees(location=[-1.9+x + x_offset, 3.05+ y_offset, 0.001], rotation=[0, 0, 90])

    for y in range (6):
        hWall.spawn_degrees(location=[2.4+ x_offset, (-y*1.0)+2.55 + y_offset, 0.001], rotation=[0, 0, 0])

    for x in range (4):
        hWall.spawn_degrees(location=[-0.9+x+ x_offset, -3.05+ y_offset, 0.001], rotation=[0, 0, 90])

    hWall.spawn_degrees(location=[-2.03 + x_offset, -2.275+ y_offset, 0.001], rotation=[0, 0, 48])
    hWall.spawn_degrees(location=[-1.575+ x_offset, -2.7+ y_offset, 0.001], rotation=[0, 0, 48])


    # Spawn a QCar at the given initial pose
    car2 = QLabsQCar2(qlabs)
    car2.spawn_id(actorNumber=0, 
                location=initialPosition, 
                rotation=initialOrientation,
                scale=[.1, .1, .1], 
                configuration=0, 
                waitForConfirmation=True)

    #spawn cameras 1. birds eye, 2. edge 1, possess the qcar

    camera1Loc = [0.15, 1.7, 5]
    camera1Rot = [0, 90, 0]
    camera1 = QLabsFreeCamera(qlabs)
    camera1.spawn_degrees(location=camera1Loc, rotation=camera1Rot)

    #camera1.possess()

    camera2Loc = [-0.36+ x_offset, -3.691+ y_offset, 2.652]
    camera2Rot = [0, 47, 90]
    camera2=QLabsFreeCamera(qlabs)
    camera2.spawn_degrees (location = camera2Loc, rotation=camera2Rot)

    camera2.possess()

    # stop signs
    #parking lot
    myStopSign = QLabsStopSign(qlabs)
    
    myStopSign.spawn_degrees (location=[-1.5, 3.6, 0.006], 
                            rotation=[0, 0, -35], 
                            scale=[0.1, 0.1, 0.1], 
                            waitForConfirmation=False)    

    myStopSign.spawn_degrees (location=[-1.5, 2.2, 0.006], 
                            rotation=[0, 0, 35], 
                            scale=[0.1, 0.1, 0.1], 
                            waitForConfirmation=False)  
    
    #x+ side
    myStopSign.spawn_degrees (location=[2.410, 0.206, 0.006], 
                            rotation=[0, 0, -90], 
                            scale=[0.1, 0.1, 0.1], 
                            waitForConfirmation=False)  
    
    myStopSign.spawn_degrees (location=[1.766, 1.697, 0.006], 
                            rotation=[0, 0, 90], 
                            scale=[0.1, 0.1, 0.1], 
                            waitForConfirmation=False)  

    #roundabout signs
    myRoundaboutSign = QLabsRoundaboutSign(qlabs)
    myRoundaboutSign.spawn_degrees(location= [2.392, 2.522, 0.006],
                              rotation=[0, 0, -90],
                              scale= [0.1, 0.1, 0.1],
                              waitForConfirmation=False)
    
    myRoundaboutSign.spawn_degrees(location= [0.698, 2.483, 0.006],
                              rotation=[0, 0, -145],
                              scale= [0.1, 0.1, 0.1],
                              waitForConfirmation=False)
    
    myRoundaboutSign.spawn_degrees(location= [0.007, 3.973, 0.006],
                            rotation=[0, 0, 135],
                            scale= [0.1, 0.1, 0.1],
                            waitForConfirmation=False)


    #yield sign
    #one way exit yield
    myYieldSign = QLabsYieldSign(qlabs)
    myYieldSign.spawn_degrees(location= [0.0, -1.3, 0.006],
                              rotation=[0, 0, -180],
                              scale= [0.1, 0.1, 0.1],
                              waitForConfirmation=False)
    
    #roundabout yields
    myYieldSign.spawn_degrees(location= [2.4, 3.2, 0.006],
                            rotation=[0, 0, -90],
                            scale= [0.1, 0.1, 0.1],
                            waitForConfirmation=False)
    
    myYieldSign.spawn_degrees(location= [1.1, 2.8, 0.006],
                            rotation=[0, 0, -145],
                            scale= [0.1, 0.1, 0.1],
                            waitForConfirmation=False)
    
    myYieldSign.spawn_degrees(location= [0.49, 3.8, 0.006],
                            rotation=[0, 0, 135],
                            scale= [0.1, 0.1, 0.1],
                            waitForConfirmation=False)
    
    

    # Spawning crosswalks
    myCrossWalk = QLabsCrosswalk(qlabs)
    myCrossWalk.spawn_degrees   (location =[-2 + x_offset, -1.475 + y_offset, 0.01],
                                rotation=[0,0,0], 
                                scale = [0.1,0.1,0.075],
                                configuration = 0)

    myCrossWalk.spawn_degrees   (location =[-0.5, 0.95, 0.006],
                                rotation=[0,0,90], 
                                scale = [0.1,0.1,0.075],
                                configuration = 0)
    
    myCrossWalk.spawn_degrees   (location =[0.15, 0.32, 0.006],
                                rotation=[0,0,0], 
                                scale = [0.1,0.1,0.075],
                                configuration = 0)

    myCrossWalk.spawn_degrees   (location =[0.75, 0.95, 0.006],
                                rotation=[0,0,90], 
                                scale = [0.1,0.1,0.075],
                                configuration = 0)

    myCrossWalk.spawn_degrees   (location =[0.13, 1.57, 0.006],
                                rotation=[0,0,0], 
                                scale = [0.1,0.1,0.075],
                                configuration = 0)

    myCrossWalk.spawn_degrees   (location =[1.45, 0.95, 0.006],
                                rotation=[0,0,90], 
                                scale = [0.1,0.1,0.075],
                                configuration = 0)

    #Signage line guidance (white lines)
    mySpline = QLabsBasicShape(qlabs)
    mySpline.spawn_degrees (location=[2.21, 0.2, 0.006], 
                            rotation=[0, 0, 0], 
                            scale=[0.27, 0.02, 0.001], 
                            waitForConfirmation=False)

    mySpline.spawn_degrees (location=[1.951, 1.68, 0.006], 
                            rotation=[0, 0, 0], 
                            scale=[0.27, 0.02, 0.001], 
                            waitForConfirmation=False)

    mySpline.spawn_degrees (location=[-0.05, -1.02, 0.006], 
                            rotation=[0, 0, 90], 
                            scale=[0.38, 0.02, 0.001], 
                            waitForConfirmation=False)

    # define rt model path
    rtModel = os.path.normpath(os.path.join(os.environ['RTMODELS_DIR'], 'QCar2/QCar2_Workspace_studio'))
    # Start spawn model
    QLabsRealTime().start_real_time_model(rtModel)

    return car2

#function to terminate the real time model running
def terminate():
    rtModel = os.path.normpath(os.path.join(os.environ['RTMODELS_DIR'], 'QCar2/QCar2_Workspace_studio'))
    QLabsRealTime().terminate_real_time_model(rtModel)
if __name__ == '__main__':
    main()

