- Open binary image
[xy_8bit_binary__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nuclei.tif) and discuss data-type (data-type is unsigned 8-bit values,
minimal value is 0, maximal value is 255)
- Open [xy_8bit_binary__two_cells_matlabstyle.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__two_cells_matlabstyle.tif) and see lowest and highest values (data-type is unsigned 8-bit values,
minimal value is 0, maximal value is 1)
- **[ File > Open... ]** [xy_8bit__two_cells.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif)
- Inspect pixel values to find a threshold separating fore- and back-ground
  - Hover over the image and observe the pixel values (in ImageJ status bar)
  - Draw line profile and **[Analyze > Plot Profile ]** or **[Ctrl-K]**
  - Inspect histogram using: **[ Analyze > Histogram ]** or **[Ctrl-H]**
- **[ Image > Adjust > Manual Threshold... ]**
  - `Lower threshold level` which is the value that you observed in the aforementioned step that would separate foreground and background
  - `Upper threshold level` can be set to the maximum bit length (in this case 255)
  - Press **OK**, this will produce an overlaid image where you can see the regions to be segmented in red. This step stores this information as image metadata for the next step (i.e. creating a binary image or mask)
- Verify that binary options are set up correctly
  - **[Process > Binary > Options ..]** [x] Black background
- **[Process > Binary > Convert to Mask ]**
- **[ File > Open... ]** [xy_8bit__two_cells.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif)
- Apply a higher threshold so that only the high intensity level nuclei remains
