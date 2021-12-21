%These matlab scripts illustrate separating the foreground from the
%background using a threshold value provided by the user
%Prompt user for a threshold value
thres_val = input('Enter a threshold value: '); 
% Prompt user to choose an image, e.g. xy_8bit__two_cells.tif
[file, path] = uigetfile("*.tif");
%Read input image
in_image = imread(fullfile(path, file));
%display input image
figure; imagesc(in_image); 
%Binarize input image with the threshold valuein_image
bin_image = uint8(in_image>= thres_val);
% Display binary image
figure; imagesc(bin_image); 
