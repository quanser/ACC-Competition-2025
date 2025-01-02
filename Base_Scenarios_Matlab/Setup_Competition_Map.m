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
verbose = false;
num_destroyed = qlabs.destroy_all_spawned_actors();

%World Objects
% Flooring

x_offset = 0.13;
y_offset = 1.67;
hFloor = QLabsQCarFlooring(qlabs);
hFloor.spawn_degrees([x_offset, y_offset, 0.001],[0, 0, -90]);


%region: Walls
hWall = QLabsWalls(qlabs);
hWall.set_enable_dynamics(false);

for y = 0:4
    hWall.spawn_degrees([-2.4 + x_offset, (-y*1.0)+2.55 + y_offset, 0.001], [0, 0, 0]);
end

for x = 0:4
    hWall.spawn_degrees([-1.9+x + x_offset, 3.05+ y_offset, 0.001], [0, 0, 90]);
end

for y = 0:5
    hWall.spawn_degrees([2.4+ x_offset, (-y*1.0)+2.55 + y_offset, 0.001], [0, 0, 0]);
end

for x = 0:3
    hWall.spawn_degrees([-0.9+x+ x_offset, -3.05+ y_offset, 0.001], [0, 0, 90]);
end

hWall.spawn_degrees([-2.03 + x_offset, -2.275+ y_offset, 0.001], [0, 0, 48]);
hWall.spawn_degrees([-1.575+ x_offset, -2.7+ y_offset, 0.001], [0, 0, 48]);

%spawn cameras 1. birds eye, 2. edge 1, possess the qcar

camera1Loc = [0.15, 1.7, 5];
camera1Rot = [0, 90, 0];
camera1 = QLabsFreeCamera(qlabs);
camera1.spawn_degrees(camera1Loc, camera1Rot);

camera1.possess();

camera2Loc = [-0.36+ x_offset, -3.691+ y_offset, 2.652];
camera2Rot = [0, 47, 90];
camera2=QLabsFreeCamera(qlabs);
camera2.spawn_degrees (camera2Loc, camera2Rot);

% Spawning crosswalks
myCrossWalk = QLabsCrosswalk(qlabs);
myCrossWalk.spawn_id_degrees([-2 + x_offset, -1.475 + y_offset, 0.01],[0,0,0], [0.1,0.1,0.075],0);

mySpline = QLabsBasicShape(qlabs);
mySpline.spawn_degrees ([2.05 + x_offset, -1.5 + y_offset, 0.01], [0, 0, 0], [0.27, 0.02, 0.001]);


%QCar
myCar = QLabsQCar(qlabs);
myCar.spawn_id_degrees(0, [-1.205, -0.83, 0.005], [0, 0, -44.7], [1/10, 1/10, 1/10], 1);    
file_workspace = fullfile(getenv('RTMODELS_DIR'), 'QCar', 'QCar_Workspace_studio.rt-win64');

% Start RT models
pause(2)
system(['quarc_run -D -r -t tcpip://localhost:17000 ', file_workspace]);
pause(3)



