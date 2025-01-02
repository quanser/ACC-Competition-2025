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
    qc_stop_model('tcpip://localhost:17000', 'QCar_Workspace');
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



%QCar
myCar = QLabsQCar(qlabs, verbose);
myCar.spawn_id_degrees(0, [0 -1.25 0], [0 0 0], [1, 1, 1], 1) ;
file_workspace = fullfile(getenv('RTMODELS_DIR'), 'QCar', 'QCar_Workspace.rt-win64');

% Start RT models
pause(2)
system(['quarc_run -D -r -t tcpip://localhost:17000 ', file_workspace]);
pause(3)

%spawn Traffic Lights
trafficLight1 = QLabsTrafficLight(qlabs);
trafficLight2 = QLabsTrafficLight(qlabs);
trafficLight3 = QLabsTrafficLight(qlabs);
trafficLight4 = QLabsTrafficLight(qlabs);

trafficLight1.spawn_id_degrees(1, [20.8,-2.75,0], [0,0,180], [1,1,1]);
trafficLight2.spawn_id_degrees(2, [28.0,-4.0,0], [0,0,-90], [1,1,1]);
trafficLight3.spawn_id_degrees(3, [22.0,4.1,0], [0,0,90], [1,1,1]);
trafficLight4.spawn_id_degrees(4, [29.3,2.9,0], [0,0,0], [1,1,1]);

disp('traffic lights spawned')

intersection1Flag = 0;

while(1)
    if intersection1Flag == 0
        trafficLight1.set_color(trafficLight1.COLOR_RED);
        trafficLight4.set_color(trafficLight4.COLOR_RED);
        trafficLight2.set_color(trafficLight2.COLOR_GREEN);
        trafficLight3.set_color(trafficLight3.COLOR_GREEN);
    end

    if intersection1Flag == 1
        trafficLight1.set_color(trafficLight1.COLOR_RED);
        trafficLight4.set_color(trafficLight4.COLOR_RED);
        trafficLight2.set_color(trafficLight2.COLOR_YELLOW);
        trafficLight3.set_color(trafficLight3.COLOR_YELLOW);
    end

    if intersection1Flag == 2
        trafficLight1.set_color(trafficLight1.COLOR_GREEN);
        trafficLight4.set_color(trafficLight4.COLOR_GREEN);
        trafficLight2.set_color(trafficLight2.COLOR_RED);
        trafficLight3.set_color(trafficLight3.COLOR_RED);
    end

    if intersection1Flag == 3
        trafficLight1.set_color(trafficLight1.COLOR_YELLOW);
        trafficLight4.set_color(trafficLight4.COLOR_YELLOW);
        trafficLight2.set_color(trafficLight2.COLOR_RED);
        trafficLight3.set_color(trafficLight3.COLOR_RED);
    end

    intersection1Flag = mod(intersection1Flag + 1, 4);

    pause(5);
end

