%--------------------------------------------------------------------%

% This script was intended to be run in the Plane world for the Self
% Driving Car Studio

%Make sure to run your RT Model after you have run this script 

%--------------------------------------------------------------------%


% MATLAB Path

newPathEntry = fullfile(getenv('QAL_DIR'), 'libraries', 'matlab', 'qvl');
pathCell = regexp(path, pathsep, 'split');
if ispc  % Windows is not case-sensitive
  onPath = any(strcmpi(newPathEntry, pathCell));
else
  onPath = any(strcmp(newPathEntry, pathCell));
end

if onPath == 0
    path(path, newPathEntry)
    savepath
end

% Stop RT models
try
    qc_stop_model('tcpip://localhost:17000', 'QCar_Workspace')
catch error
end
pause(1)

% QLab connection
qlabs = QuanserInteractiveLabs();
connection_established = qlabs.open('localhost');

if connection_established == false
    disp("Failed to open connection.")
    return
end
disp('Connected')
verbose = true;
num_destroyed = qlabs.destroy_all_spawned_actors();

%set camera
myCam = QLabsFreeCamera(qlabs);
myCam.spawn_degrees([1,21,20], [0,35,-45]);
myCam.possess();

%World Objects

%Widths
sidewalkWidth = 2.5;
roadWidth = 5;
lineWidth = 0.2;

%generate roads
width = roadWidth;

mySpline = QLabsSplineLine(qlabs);
mySpline.spawn([0,0,0], [0,0,0], [1,1,1], 1);
mySpline.set_points([0,0,0], [[0,0,0.001,width]; [50,0,0.001,width]]);

%generate middle lines
width = lineWidth;

mySpline.spawn([0,0,0], [0,0,0], [1,1,1], 1);
mySpline.set_points([1,1,0], [[0,0,0.005,width]; [22.5,0,0.005,width]]);

mySpline.spawn([0,0,0], [0,0,0], [1,1,1], 1);
mySpline.set_points([1,1,0], [[27.5,0,0.005,width]; [50,0,0.005,width]]);

%generate crosswalk
myCrosswalk = QLabsCrosswalk(qlabs);
myCrosswalk.spawn_id_degrees(2, [25,0,0.005], [0,0,90], [1,2,0.54], 0)

%generate sidewalks
width = sidewalkWidth;
mySidewalk = QLabsBasicShape(qlabs);

mySidewalk.spawn_degrees([25,-3.75,0], [0,0,0], [50,sidewalkWidth,0.25], 0);
mySidewalk.set_material_properties([0.1,0.1,0.1], 1.0);

mySidewalk.spawn_degrees([25,3.75,0], [0,0,0], [50,sidewalkWidth,0.25], 0);
mySidewalk.set_material_properties([0.1,0.1,0.1], 1.0);


%QCar
myCar = QLabsQCar2(qlabs, verbose);
myCar.spawn_id_degrees(0, [0 -1.25 0], [0 0 0], [1, 1, 1], 1) ;

%Pedestrian Movement
%define locations, and flags
LOC1 = [15.8, 3.7, 0.13];
LOC2 = [23.4, 3.7, 0.13];
LOC3 = [23.4, -3.7, 0.13];
LOC4 = [15.8, -3.7, 0.13];

setpointFlag = 0;
locationCounter = 0;

%spawn pedestrian
myPedestrian = QLabsPerson(qlabs);
myPedestrian.spawn_id_degrees(1, LOC1, [0,0,0], [1,1,1], 6);
disp('Pedestrian Spawned')

while(1)

    if locationCounter == 0
        setpointFlag = myPedestrian.move_to(LOC2, myPedestrian.JOG);
    end
    if locationCounter == 1
        setpointFlag = myPedestrian.move_to(LOC3, myPedestrian.WALK);
        pause(4);
    end
    if locationCounter == 2
        setpointFlag = myPedestrian.move_to(LOC4, myPedestrian.JOG);
    end
    if locationCounter == 3
        setpointFlag = myPedestrian.move_to(LOC3, myPedestrian.JOG);
    end
    if locationCounter == 4
        setpointFlag = myPedestrian.move_to(LOC2, myPedestrian.WALK);
        pause(4);
    end
    if locationCounter == 5
        setpointFlag = myPedestrian.move_to(LOC1, myPedestrian.JOG);
    end
    if setpointFlag == 1
        locationCounter = locationCounter + 1;
        locationCounter = mod(locationCounter,6);
    end

    pause(2);

end



