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
sidewalkWidth = 10;
roadWidth = 5;
lineWidth = 0.2;
roundaboutWidth = 3.5;

%generate roads
width = roadWidth;

mySpline = QLabsSplineLine(qlabs);
mySpline.spawn([0,0,0], [0,0,0], [1,1,1], 1);
mySpline.set_points([0,0,0], [[0,0,0.001,width]; [50,0,0.001,width]]);

mySpline.spawn([0,0,0], [0,0,0], [1,1,1], 1);
mySpline.set_points([0,0,0], [[63.45,-7.88,0.001,width]; [88.45,-51.18,0.001,width]]);

mySpline.spawn([0,0,0], [0,0,0], [1,1,1], 1);
mySpline.set_points([0,0,0], [[63.45,7.88,0.001,width]; [88.45,51.18,0.001,width]]);

%generate roundabout
width = roundaboutWidth;

myCircle = QLabsSplineLine(qlabs);
myCircle.spawn([58.9,0,0], [0,0,0], [1,1,1], 1);
myCircle.circle_from_center(8, width, [0,0,0], 50);


%generate middle yellow lines
width = lineWidth;

mySpline.spawn([0,0,0], [0,0,0], [1,1,1], 1);
mySpline.set_points([1,1,0], [[0,0,0.005,width]; [49.0,0,0.005,width]]);

mySpline.spawn([0,0,0], [0,0,0], [1,1,1], 1);
mySpline.set_points([1,1,0], [[63.7,-8.31,0.005,width]; [88.45,-51.18,0.009,width]]);

mySpline.spawn([0,0,0], [0,0,0], [1,1,1], 1);
mySpline.set_points([1,1,0], [[63.7,8.31,0.005,width]; [88.45,51.18,0.005,width]]);

%generate white lines
width = lineWidth;
mySpline.spawn([0,0,0], [0,0,0], [1,1,1], 1);
mySpline.set_points([1,1,1], [[48.9,-0.11,0.005,width]; [48.9,-2.5,0.005,width]]);

mySpline.spawn([0,0,0], [0,0,0], [1,1,1], 1);
mySpline.set_points([1,1,1], [[63.86,-8.46,0.005,width]; [65.91,-7.13,0.005,width]]);

mySpline.spawn([0,0,0], [0,0,0], [1,1,1], 1);
mySpline.set_points([1,1,1], [[63.7,8.45,0.005,width]; [61.64,9.74,0.005,width]]);

%generate Yield signs
myYieldSign = QLabsYieldSign(qlabs);
myYieldSign.spawn_degrees([49.5,-2.8,0.002], [0,0,180], [1,1,1]);
myYieldSign.spawn_degrees([66.1,-7.0,0.002], [0,0,-60], [1,1,1]);
myYieldSign.spawn_degrees([61.47,9.9,0.002], [0,0,60], [1,1,1]);


%generate roundabout signs
myroundaboutSign = QLabsRoundaboutSign(qlabs);
myroundaboutSign.spawn_degrees([42.9,-2.8,0.002], [0,0,180], [1,1,1]);
myroundaboutSign.spawn_degrees([69.8,-13.1,0.002], [0,0,-60], [1,1,1]);
myroundaboutSign.spawn_degrees([64.49,15.2,0.002], [0,0,60], [1,1,1]);


%QCar
myCar = QLabsQCar(qlabs, verbose);
myCar.spawn_id_degrees(0, [0 -1.25 0], [0 0 0], [1, 1, 1], 1) ;
file_workspace = fullfile(getenv('RTMODELS_DIR'), 'QCar', 'QCar_Workspace.rt-win64');

% Start RT models
pause(2)
system(['quarc_run -D -r -t tcpip://localhost:17000 ', file_workspace]);
pause(3)



