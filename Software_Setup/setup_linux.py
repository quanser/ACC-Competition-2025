#region: File imports
import subprocess
import time
#endregion 


def main():   
        # Check to make sure the files are present in the downloads folder
        
        
        checkStatus = subprocess.call("ls /home/$USER/Downloads/ACC_Resources/src/", shell=True)

        if checkStatus==2:
            print("Please make sure you have not moved the downloaded files from the downloads folder in your system...")
            return 
        
        
        directoryCreateStatus = subprocess.call("ls /home/$USER/Documents/ACC_Development", shell=True)
                    
        if directoryCreateStatus ==0:
            # The directory already exists.... 
            print("Directory already exists....Creating a backup copy ")

            timestr = time.strftime("%Y%m%d-%H%M%S")
            backupDir = "mv /home/$USER/Documents/ACC_Development /home/$USER/Documents/ACC_Development_backup_"+timestr
            directoryCreateStatus = subprocess.call(backupDir, shell=True)
            createNewDir = subprocess.call("mkdir /home/$USER/Documents/ACC_Development", shell=True)


        else : 
            directoryCreateStatus = subprocess.call("mkdir /home/$USER/Documents/ACC_Development", shell=True)

    
        copyFileStatus = subprocess.call("cp -r /home/$USER/Downloads/ACC_Resources/src/ /home/$USER/Documents/ACC_Development", shell=True)
        if copyFileStatus !=0:
    
            print("Issues creating root ACC directory.. please make sure the downloaded resources include a /src directory or download again... ")
            return


        # clone to ACC repo to obtain docker files for Quanser Virtual Labs docker image 
        cloneACCGithub = subprocess.call("cd /home/$USER/Documents/ACC_Development/; git clone -b docker https://github.com/quanser/ACC-Competition-2025.git", shell=True)
        if cloneACCGithub!=0:
            subprocess.call("sudo apt-get install git", shell = True)
            cloneACCGithub = subprocess.call("cd /home/$USER/Documents/ACC_Development/; git clone https://github.com/quanser/ACC-Competition-2025.git", shell=True)


        # Copy files necessary for Quanser Virtual Labs docker image
        copyQVLDockerFiles = subprocess.call("cp -r /home/$USER/Documents/ACC_Development/ACC-Competition-2025/Docker /home/$USER/Documents/ACC_Development/docker", shell=True)

        if copyQVLDockerFiles !=0:
            print("Unable to copy the QVL docker image.... please delete folder ACC_Development folder and try again.. ")
            return

        createDevDir = subprocess.call("mkdir /home/$USER/Documents/ACC_Development/dev", shell=True)
        if createDevDir !=0:
            print("Issues creating development directory.. please make sure Documents/ACC_Development folder has not been modified...")
            return

        # clone github repo for isaac_ros and setup ros2 folder for virtual QCar2
        cloneIsaacROS = subprocess.call("git-lfs --version", shell=True)
        if cloneIsaacROS!=0:
            subprocess.call("sudo apt-get install git-lfs", shell = True)
            print("Please restart PC and rerun setup script for git-lfs to be correctly configured....")
            return
        
        cloneIsaacROS = subprocess.call("cd /home/$USER/Documents/ACC_Development/; git clone -b release-2.1 https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_common.git", shell=True)
        isaacROSFiles =  subprocess.call("cp /home/$USER/Documents/ACC_Development/src/examples/sdcs/qcar2/acc/isaac_ros_common/config/.isaac_ros_common-config /home/$USER/Documents/ACC_Development/isaac_ros_common/scripts",shell=True)

        if isaacROSFiles !=0:
            print("Issues copying Isaac_ROS config file... delete /Documents/ACC_Development/ directory and rerun setup again... ")

        dockerQVLFiles =  subprocess.call("cp -r /home/$USER/Documents/ACC_Development/src/examples/sdcs/qcar2/acc/docker /home/$USER/Documents/ACC_Development/",shell=True)
        if dockerQVLFiles !=0:
            print("Issues copying isaac_ros_common configuration files... please make sure Documents/ACC_Development/src/examples/sdcs/qcar2/acc/isaac_ros_common exists...")
            return        

        QCarROSFiles =  subprocess.call("cp -r /home/$USER/Documents/ACC_Development/src/examples/sdcs/qcar2/ros2 /home/$USER/Documents/ACC_Development",shell=True)
        if QCarROSFiles !=0:
            print("QCar2 ros files do not exist in src folder... please redownload resources and rerun setup_linux.py")
            return
        
        # Copy the libraries folder inside isaac ros folder for it to be mounted in isaac ros image
        copyScenariosROSFiles =  subprocess.call("cp -r /home/$USER/Documents/ACC_Development/src/libraries/ /home/$USER/Documents/ACC_Development/docker/",shell=True)
        
        # create a backup directory
        createBackupDir = subprocess.call("mkdir /home/$USER/Documents/ACC_Development/backup", shell=True)
        copyBackup =  subprocess.call("cp -r /home/$USER/Documents/ACC_Development/src /home/$USER/Documents/ACC_Development/backup ;cp -r /home/$USER/Documents/ACC_Development/ACC-Competition-2025 /home/$USER/Documents/ACC_Development/backup ",shell=True)
        cleanup = subprocess.call( "rm -fr /home/$USER/Documents/ACC_Development/src /home/$USER/Documents/ACC_Development/ACC-Competition-2025 ", shell=True)
        if createBackupDir!=0 or copyBackup !=0 or cleanup!=0:
            print("Issues creating backup....  System files have been configured correctly")

        print("System configured correctly! Good Luck!")  




# Using the special variable 
if __name__=="__main__":
    main()