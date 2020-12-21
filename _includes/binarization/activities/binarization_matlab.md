%These matlab scripts illustrate separating the foreground from the
%background using a threshold value provided by the user

%Prompt user for a threshold value
thres_val = input('Enter a threshold value: ');
%Read input image
in_image = imread(['image_data' filesep 'xy_8bit__two_cells.tif']);
figure; imagesc(in_image); %display input image
%Binarize input image with the threshold valuein_image
bin_image = uint8(in_image>= thres_val);
figure; imagesc(bin_image) % Display binary image
