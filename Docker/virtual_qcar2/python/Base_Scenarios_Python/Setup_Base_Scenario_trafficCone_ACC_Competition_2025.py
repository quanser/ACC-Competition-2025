# region: package imports
import os
import time

# environment objects

from qvl.qlabs import QuanserInteractiveLabs
from qvl.qcar2 import QLabsQCar2
from qvl.spline_line import QLabsSplineLine
from qvl.real_time import QLabsRealTime
from qvl.system import QLabsSystem
from qvl.crosswalk import QLabsCrosswalk
from qvl.traffic_cone import QLabsTrafficCone
from qvl.basic_shape import QLabsBasicShape
from qvl.free_camera import QLabsFreeCamera
# import pal.resources.rtmodels as rtmodels

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
    sidewalkWidth = 2.5
    roadWidth = 5
    lineWidth = 0.2
    mySpline = QLabsSplineLine(qlabs)

    #generate roads
    width = roadWidth

    mySpline = QLabsSplineLine(qlabs)
    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[0,0,0], pointList=[[0,0,0.001,width], [50,0,0.001,width]])

    #generate middle lines
    width = lineWidth

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[1,1,0], pointList=[[0,0,0.005,width], [22.5,0,0.005,width]])

    mySpline.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    mySpline.set_points(color=[1,1,0], pointList=[[27.5,0,0.005,width], [50,0,0.005,width]])

    #generate crosswalk
    myCrosswalk = QLabsCrosswalk(qlabs)
    myCrosswalk.spawn_degrees(location=[25,0,0.005], rotation=[0,0,90], scale=[1,2,0.54], configuration=0)

    #generate sidewalks
    width = sidewalkWidth
    mySidewalk = QLabsBasicShape(qlabs)

    mySidewalk.spawn_degrees(location=[25,-3.75,0], rotation=[0,0,0], scale=[50,sidewalkWidth,0.25], configuration=0)
    mySidewalk.set_material_properties(color=[0.1,0.1,0.1], roughness=1.0)

    mySidewalk.spawn_degrees(location=[25,3.75,0], rotation=[0,0,0], scale=[50,sidewalkWidth,0.25], configuration=0)
    mySidewalk.set_material_properties(color=[0.1,0.1,0.1], roughness=1.0)

    #Spawn Traffic Cone
    myTrafficCone = QLabsTrafficCone(qlabs)
    myTrafficCone.spawn_degrees(location=[16.1,-2.0,0.005], rotation=[0,0,0], scale=[1.5,1.5,1.5], configuration=2)
    myTrafficCone.set_material_properties(materialSlot=1, color=[1,1,1])

    return myCar

#function to terminate the real time model running
def terminate():
    # Get the path for the QCar2 rtModel
    rtModel = os.path.normpath(os.path.join(os.environ['RTMODELS_DIR'], 'QCar2/QCar2_Workspace'))
    QLabsRealTime().terminate_real_time_model(rtModel)

if __name__ == '__main__':
    main()

