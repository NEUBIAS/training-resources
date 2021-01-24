- Open a binary image 
[xy_8bit__binary_nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__binary_nuclei.tif) and discuss data-type (data-type is unsigned 8-bit values, 
minimal value is 0, maximal value is 255)
- Open binary file from MATLAB 
[xy_8bit_binary__two_cells_matlabstyle.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__two_cells_matlabstyle.tif) lower and highest value (data-type is unsigned 8-bit values, 
minimal value is 0, maximal value is 255)
- Verify that binary options are set up correctly. 
    - **[Process > Binary > Options ..]** [x] Black background
- **[ File > Open... ]** [xy_8bit__two_cells.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_two_cells.tif)
- **[ Image > Adjust > Threshold... ]** or **[Ctrl-Shift-T]**, vary lower threshold and discuss what happens to preview image
- Choose a value so that both cells are foreground, e.g. 49-255 
- Press **[Apply]** discuss resulting image
- **[ File > Open... ]** [xy_8bit__two_cells.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_two_cells.tif)
- Apply a higher threshold so that only the high intensity level nuclei remains 