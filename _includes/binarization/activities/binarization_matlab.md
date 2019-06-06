```matlab
function src_binarize_image()
%This function illustrates separating foreground from background using a
%fixed threshold value

threshold = 50; %example hreshold value
%Read input image
in_image = imread(['image_data' filesep 'xy_8bit__two_cells.tif']);
figure; imagesc(in_image); %display input image
%Binarized input image with the threshold value;
bin_image = uint8(in_image>= threshold);
figure; imagesc(bin_image) % display binary image
end
```
