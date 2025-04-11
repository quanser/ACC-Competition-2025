# region: package imports
import os
import random

# environment objects

from qvl.qlabs import QuanserInteractiveLabs
from qvl.qcar2 import QLabsQCar2
from qvl.free_camera import QLabsFreeCamera
from qvl.spline_line import QLabsSplineLine
from qvl.real_time import QLabsRealTime
from qvl.stop_sign import QLabsStopSign
from qvl.system import QLabsSystem


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#This scenario was designed to by used in the Plane world for the Self Driving Car Studio

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


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


    myCar = QLabsQCar2(qlabs)
    myCar.spawn_id_degrees(actorNumber=0, location=[0,-1.25,0.5], rotation=[0,0,0], scale=[1,1,1])
    rtModel = os.path.normpath(os.path.join(os.environ['RTMODELS_DIR'], 'QCar2/QCar2_Workspace'))
    QLabsRealTime().start_real_time_model(rtModel)

    #set camera
    myCam = QLabsFreeCamera(qlabs)
    myCam.spawn_degrees(location=[1,21,20], rotation=[0,35,-45])
    myCam.possess()

    #widths
    sidewalkWidth = 10
    roadWidth = 5
    lineWidth = 0.2
    mySpline = QLabsSplineLine(qlabs)

    #generate roads
    width = roadWidth

    mySpline = QLabsSplineLine(qlabs)
    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[0,0,0], pointList=[[0,0,0.001,width], [50,0,0.001,width]])

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[0,0,0], pointList=[[25,-25,0.001,width], [25,25,0.001,width]])

    #generate middle lines
    width = lineWidth

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[1,1,0], pointList=[[0,0,0.005,width], [22.5,0,0.005,width]])

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[1,1,0], pointList=[[27.5,0,0.005,width], [50,0,0.005,width]])

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[1,1,0], pointList=[[25,-25,0.005,width], [25,-2.5,0.005,width]])

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[1,1,0], pointList=[[25,25,0.005,width], [25,2.5,0.005,width]])

    #generate stop lines
    width = lineWidth

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[1,1,1], pointList=[[22.394,-0.11,0.0075,width], [22.349,-2.49,0.0075,width]])

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[1,1,1], pointList=[[25.10,-2.6,0.0075,width], [27.50,-2.6,0.0075,width]])

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[1,1,1], pointList=[[27.6,0.1,0.0075,width], [27.6,2.5,0.0075,width]])

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[1,1,1], pointList=[[24.9,2.61,0.0075,width], [22.5,2.61,0.0075,width]])

    #spawn stop sign
    myStopSign = QLabsStopSign(qlabs)
    myStopSign.spawn_degrees(location=[22.3,-2.7,0], rotation=[0,0,180], scale=[1,1,1], waitForConfirmation=False)
    myStopSign.spawn_degrees(location=[27.8,-2.7,0], rotation=[0,0,-90], scale=[1,1,1], waitForConfirmation=False)
    myStopSign.spawn_degrees(location=[22.0,3.0,0], rotation=[0,0,90], scale=[1,1,1], waitForConfirmation=False)
    myStopSign.spawn_degrees(location=[28.0,2.9,0], rotation=[0,0,0], scale=[1,1,1], waitForConfirmation=False)

    return myCar

#function to terminate the real time model running
def terminate():
    # Get the path for the QCar2 rtModel
    rtModel = os.path.normpath(os.path.join(os.environ['RTMODELS_DIR'], 'QCar2/QCar2_Workspace'))
    QLabsRealTime().terminate_real_time_model(rtModel)

if __name__ == '__main__':
    setup()

