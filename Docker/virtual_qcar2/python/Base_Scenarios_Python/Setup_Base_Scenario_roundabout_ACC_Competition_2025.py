# region: package imports
import os
import time

# environment objects

from qvl.qlabs import QuanserInteractiveLabs
from qvl.qcar2 import QLabsQCar2
from qvl.spline_line import QLabsSplineLine
from qvl.real_time import QLabsRealTime
from qvl.roundabout_sign import QLabsRoundaboutSign
from qvl.yield_sign import QLabsYieldSign
from qvl.system import QLabsSystem
from qvl.free_camera import QLabsFreeCamera


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#This scenario was designed to by used in the Plane world for the Self Driving Car Studio

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

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

    #Set the Workspace Title
    hSystem = QLabsSystem(qlabs)
    x = hSystem.set_title_string('ACC Self Driving Car Competition', waitForConfirmation=True)

    setup(qlabs=qlabs)




#Function to setup QLabs, Spawn in QCar, and run real time model
def setup(qlabs):

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
    roundaboutWidth = 3.5
    lineWidth = 0.2
    mySpline = QLabsSplineLine(qlabs)

    #generate roads
    width = roadWidth

    mySpline = QLabsSplineLine(qlabs)
    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[0,0,0], pointList=[[0,0,0.001,width], [50,0,0.001,width]])

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[0,0,0], pointList=[[63.45,-7.88,0.001,width], [88.45,-51.18,0.001,width]])

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[0,0,0], pointList=[[63.45,7.88,0.001,width], [88.45,51.18,0.001,width]])

    #generate roundabout
    width = roundaboutWidth

    myCircle = QLabsSplineLine(qlabs)
    myCircle.spawn(location=[58.9,0,0], scale=[1,1,1], configuration=1)
    myCircle.circle_from_center(radius=8, lineWidth=width, color=[0,0,0], numSplinePoints=50)


    #generate middle yellow lines
    width = lineWidth

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[1,1,0], pointList=[[0,0,0.005,width], [49.0,0,0.005,width]])

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[1,1,0], pointList=[[63.7,-8.31,0.005,width], [88.45,-51.18,0.009,width]])

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[1,1,0], pointList=[[63.7,8.31,0.005,width], [88.45,51.18,0.005,width]])

    #generate white lines
    width = lineWidth
    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[1,1,1], pointList=[[48.9,-0.11,0.005,width], [48.9,-2.5,0.005,width]])

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[1,1,1], pointList=[[63.86,-8.46,0.005,width], [65.91,-7.13,0.005,width]])
    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[1,1,1], pointList=[[63.7,8.45,0.005,width], [61.64,9.74,0.005,width]])   

    #generate Yield signs
    myYieldSign = QLabsYieldSign(qlabs)
    myYieldSign.spawn_degrees(location=[49.5,-2.8,0.002], rotation=[0,0,180], scale=[1,1,1])
    myYieldSign.spawn_degrees(location=[66.1,-7.0,0.002], rotation=[0,0,-60], scale=[1,1,1])
    myYieldSign.spawn_degrees(location=[61.47,9.9,0.002], rotation=[0,0,60], scale=[1,1,1])


    #generate roundabout signs
    myroundaboutSign = QLabsRoundaboutSign(qlabs)
    myroundaboutSign.spawn_degrees(location=[42.9,-2.8,0.002], rotation=[0,0,180], scale=[1,1,1])
    myroundaboutSign.spawn_degrees(location=[69.8,-13.1,0.002], rotation=[0,0,-60], scale=[1,1,1])
    myroundaboutSign.spawn_degrees(location=[64.49,15.2,0.002], rotation=[0,0,60], scale=[1,1,1])

    return myCar

#function to terminate the real time model running
def terminate():
    # Get the path for the QCar2 rtModel
    rtModel = os.path.normpath(os.path.join(os.environ['RTMODELS_DIR'], 'QCar2/QCar2_Workspace'))
    QLabsRealTime().terminate_real_time_model(rtModel)

if __name__ == '__main__':
    main()

