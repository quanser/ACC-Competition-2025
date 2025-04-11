import os

from qvl.real_time import QLabsRealTime

def terminate():
    QLabsRealTime().terminate_real_time_model("QCar2_Workspace")
    QLabsRealTime().terminate_real_time_model("QCar2_Workspace_studio")
    QLabsRealTime().terminate_real_time_model("QCar2_Workspace_interleaved")
    QLabsRealTime().terminate_real_time_model("QCar2_Workspace_studio_interleaved")
    #QLabsRealTime().terminate_real_time_model("QCar2_Workspace", RTModelHostName="host.docker.internal")

if __name__ == '__main__':
    terminate()