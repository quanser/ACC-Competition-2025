# region: package imports
import os

# environment objects

from qvl.qlabs import QuanserInteractiveLabs
from qvl.qcar2 import QLabsQCar2
from qvl.free_camera import QLabsFreeCamera
from qvl.real_time import QLabsRealTime
from qvl.basic_shape import QLabsBasicShape
from qvl.system import QLabsSystem
from qvl.walls import QLabsWalls
from qvl.qcar_flooring import QLabsQCarFlooring
from qvl.crosswalk import QLabsCrosswalk


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#This scenario was designed to by used in the Plane world for the Self Driving Car Studio

#After running this script, make sure to run your RT Model

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#endregion

#Function to setup QLabs, Spawn in QCar, and run real time model
def setup(initialPosition = [-1.205, -0.83, 0.005], initialOrientation = [0, 0, -44.7]):
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
    hFloor.spawn_degrees([x_offset, y_offset, 0.001],rotation = [0, 0, -90], configuration=0)


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
    
    rtModel = os.path.normpath(os.path.join(os.environ['RTMODELS_DIR'], 'QCar2/QCar2_Workspace_studio'))
    QLabsRealTime().start_real_time_model(rtModel)

    #spawn cameras 1. birds eye, 2. edge 1, possess the qcar

    camera1Loc = [0.15, 1.7, 5]
    camera1Rot = [0, 90, 0]
    camera1 = QLabsFreeCamera(qlabs)
    camera1.spawn_degrees(location=camera1Loc, rotation=camera1Rot)

    camera1.possess()

    camera2Loc = [-0.36+ x_offset, -3.691+ y_offset, 2.652]
    camera2Rot = [0, 47, 90]
    camera2=QLabsFreeCamera(qlabs)
    camera2.spawn_degrees (location = camera2Loc, rotation=camera2Rot)

    # Spawning crosswalks
    myCrossWalk = QLabsCrosswalk(qlabs)
    myCrossWalk.spawn_degrees   (location =[-2 + x_offset, -1.475 + y_offset, 0.01],
                                rotation=[0,0,0], 
                                scale = [0.1,0.1,0.075],
                                configuration = 0)

    mySpline = QLabsBasicShape(qlabs)
    mySpline.spawn_degrees (location=[2.05 + x_offset, -1.5 + y_offset, 0.01], 
                            rotation=[0, 0, 0], 
                            scale=[0.27, 0.02, 0.001], 
                            waitForConfirmation=False)

    return car2

#function to terminate the real time model running
def terminate():
    rtModel = os.path.normpath(os.path.join(os.environ['RTMODELS_DIR'], 'QCar2/QCar2_Workspace_studio'))
    QLabsRealTime().terminate_real_time_model(rtModel)

if __name__ == '__main__':
    setup()
