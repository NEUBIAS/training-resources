% This MATLAB script illustrates how to explore different ways 
% to inspect pixel values and indices 
% It is recommended to read comments and to run sections separately 
% one after the other with the corresponding command in the Editor Toolstrip 

%% Choose and load the image %% 
% Read input image
in_image = webread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif');
% Display input image figure
figure;imagesc(in_image); axis equal 

%% 1 - Explore pixels with mouse (Data Tips)%% 
% In the Figure window, click the Data Tips symbol 
% (text baloon icon on the top right corner of the image) 
% or select from [Tools>Data Cursor] in the Figure Toolstrip 
% Now if you click on the image a Data Tip window will appear 
% showing the coordinates [X,Y], the pixel intensity [Index] 
% and the assigned colour in the current display [R,G,B] 
% To exit the Data Tips mode, click again on the Data Tips icon 
% To stop displaying Data Tips, right click on the image and select 
% [Delete All Data Tips] 
% N.B. The point with the lowest coordinates [X,Y = 0,0] is normally found 
% on the top left corner 

%% 2 - Explore by linescans %% 
% Draw a line across the image to evaluate its intensity profile 
% 1. Click on the starting point of the line on the image 
% 2. Click on the end point of the line on the image 
% 3. Press [Enter] 
[x_coord, y_coord, line_profile] = improfile; 
% Plot sampled line on the image 
hold on; plot(x_coord, y_coord, 'w.') 
% Create new figure showing the line profile 
figure; plot(line_profile, 'k', 'LineWidth', 2);
xlabel('Distance (pixels)');
ylabel('Gray value'); 
set(findall(gcf, '-property', 'FontSize'), 'FontSize', 14) 

%% 3 - Explore by plotting the image histogram %% 
% Produce the image histogram 
figure; histogram(in_image);
xlabel('Gray value');
ylabel('Counts');
set(findall(gcf, '-property', 'FontSize'), 'FontSize', 14) 
% Calculate some metrics from the histogram 
% Number of pixels included in the count: 
px_count = size(in_image,1)*size(in_image,2); 
% Mean gray value 
px_mean = mean(in_image(:)); 
% Standard deviation for gray values 
px_std = std(double(in_image(:))); 
% Minimum gray value 
px_min = min(in_image(:)); 
% Maximum gray value 
px_max = max(in_image(:)); 
% Mode for gray values 
[px_mode, px_mode_frequency] = mode(in_image(:)); 
% Print metrics to screen 
fprintf('Count = %i\n', px_count); 
fprintf('Mean = %.3f\n', px_mean); 
fprintf('StdDev = %.3f\n', px_std); 
fprintf('Min = %i\n', px_min); 
fprintf('Max = %i\n', px_max); 
fprintf('Mode = %i (%i)\n', px_mode, px_mode_frequency);