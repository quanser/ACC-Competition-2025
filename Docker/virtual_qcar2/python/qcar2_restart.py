import os

from qvl.qlabs import QuanserInteractiveLabs
from qvl.qcar2 import QLabsQCar2
from qvl.free_camera import QLabsFreeCamera
from qvl.real_time import QLabsRealTime

def setup(
        initialPosition=[0, 0, 0],
        initialOrientation=[0, 0, 0],
    ):

    # Try to connect to Qlabs
    qlabs = QuanserInteractiveLabs()
    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
        #qlabs.open("host.docker.internal")
        print("Connected to QLabs")
    except:
        print("Unable to connect to QLabs")
        quit()

    # Delete any previous QCar instances and stop any running spawn models
    qlabs.destroy_all_spawned_actors()
    QLabsRealTime().terminate_all_real_time_models()
    #QLabsRealTime().terminate_all_real_time_models(RTModelHostName='host.docker.internal')

    # Get the path for the QCar2 rtModel
    rtModel = os.path.normpath(os.path.join(os.environ['RTMODELS_DIR'], 'QCar2/QCar2_Workspace_studio'))

    # Spawn a QCar at the given initial pose
    hqcar = QLabsQCar2(qlabs)
    hqcar.spawn_id(
        actorNumber=0,
        location=[p*10 for p in initialPosition],
        rotation=initialOrientation,
        waitForConfirmation=True
    )

    # Create a new camera view and attach it to the QCar
    hcamera = QLabsFreeCamera(qlabs)
    hcamera.spawn()
    hqcar.possess()

    # Start spawn model
    QLabsRealTime().start_real_time_model(rtModel)
    #QLabsRealTime().start_real_time_model(rtModel, RTModelHostName='host.docker.internal')
    
    return hqcar

if __name__ == '__main__':
    setup()