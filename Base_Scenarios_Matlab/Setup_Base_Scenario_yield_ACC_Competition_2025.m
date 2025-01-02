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
myCam.spawn_degrees([1,21,20], [0,35,-45])
myCam.possess();

%World Objects

%Widths
sidewalkWidth = 10;
roadWidth = 5;
lineWidth = 0.2;
mySpline = QLabsSplineLine(qlabs);

%Generate Roads
width = roadWidth;

mySpline = QLabsSplineLine(qlabs);
mySpline.spawn([0,0,0], [0,0,0], [1,1,1], 1);
mySpline.set_points([0,0,0], [[0,0,0.001,width]; [50,0,0.001,width]]);

mySpline.spawn([0,0,0],[0,0,0],[1,1,1],1);
mySpline.set_points([0,0,0], [[25,-25,0.001,width]; [25,25,0.001,width]]);

%generate middle lines
width = lineWidth;

mySpline.spawn([0,0,0],[0,0,0],[1,1,1],1);
mySpline.set_points([1,1,0], [[0,0,0.005,width]; [22.5,0,0.005,width]]);

mySpline.spawn([0,0,0],[0,0,0],[1,1,1],1);
mySpline.set_points([1,1,0], [[27.5,0,0.005,width]; [50,0,0.005,width]]);

mySpline.spawn([0,0,0],[0,0,0],[1,1,1],1);
mySpline.set_points([1,1,0], [[25,-25,0.005,width]; [25,-2.5,0.005,width]]);

mySpline.spawn([0,0,0],[0,0,0],[1,1,1],1);
mySpline.set_points([1,1,0], [[25,25,0.005,width]; [25,2.5,0.005,width]]);

%generate stop lines
width = lineWidth;

mySpline.spawn([0,0,0],[0,0,0],[1,1,1],1);
mySpline.set_points([1,1,1], [[22.394,-0.11,0.0075,width]; [22.349,-2.49,0.0075,width]]);

mySpline.spawn([0,0,0],[0,0,0],[1,1,1],1);
mySpline.set_points([1,1,1], [[25.10,-2.6,0.0075,width]; [27.50,-2.6,0.0075,width]]);

mySpline.spawn([0,0,0],[0,0,0],[1,1,1],1);
mySpline.set_points([1,1,1], [[27.6,0.1,0.0075,width]; [27.6,2.5,0.0075,width]]);

mySpline.spawn([0,0,0],[0,0,0],[1,1,1],1);
mySpline.set_points([1,1,1], [[24.9,2.61,0.0075,width]; [22.5,2.61,0.0075,width]]);

%spawn yield signs
myYieldSign = QLabsYieldSign(qlabs);
myYieldSign.spawn_degrees([22.3,-2.7,0], [0,0,180], [1,1,1]);
myYieldSign.spawn_degrees([28.0,2.9,0], [0,0,0], [1,1,1]);

% QCar
myCar = QLabsQCar(qlabs, verbose);
myCar.spawn_id_degrees(0, [0 -1.25 0], [0 0 0], [1, 1, 1], 1) ;
file_workspace = fullfile(getenv('RTMODELS_DIR'), 'QCar', 'QCar_Workspace.rt-win64');

% Start RT models
pause(2)
system(['quarc_run -D -r -t tcpip://localhost:17000 ', file_workspace]);
pause(3)
