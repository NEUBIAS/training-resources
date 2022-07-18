- Open the 3D image [xyz_8bit__chromosomes.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__chromosomes.tif).
  - Slice the data in XY, XZ, and YZ using `Orthogonal views`: **[ Image > Stacks > Orthogonal Views ]** or **[Ctrl-Shift-H]**.
  - Go to **[ Image > Properties... ]** or **[Ctrl-Shift-P]** to open the properties window to view the voxel dimensions. 
    - Change all dimensions to 1 pixel.
    - Observe that the cell appears as an oval in the `Orthogonal Views`.
- Open the 3D multi-channel image [xyzc_8bit_beads_p_open.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit_beads_p_open.tif).
  - Use the sliders to explore different dimensions in the data.
  - Use **[ Image > Adjust > Brightness/Contrast...]** to adjust the display settings of the individual channels.
  - Explore different viewing modes, using **[ Image > Color > Channels Tool... ]**.
  - Explore the voxel dimensions, using **[ Image > Properties... ]** or **[Ctrl-Shift-P]**.
    - Observe that the voxel dimensions are anisotropic. 
  - Crop out the green bead (i.e. "subset" the data).
    - Select the rectangular selection tool and draw an ROI around the green bead.
    - Duplicate the selection, using **[ Image > Duplicate ]** or **[Ctrl-Shift-D]**.
      - [X] `Duplicate hyperstack`
      - `Channels: 1`
      - `Slices: 15-25`
    - Create a side view of the green bead:
      - **[ Image > Stacks > Reslice]** or press **/** to open the reslice menu.
        - Select `Top`
        - Click `OK`.
      - Explore and understand the different parameters:
        - `Left/Right/Top/Bottom`... as if looking from that direction onto the stack **on your screen** (e.g., `Top` does **not** mean to look on the stack from the top as in along the z-direction).
        - `Output spacing`: the spacing of the pixels along the slicing direction.
        - `avoid interpolation`
          - uncheck this in order to apply the `output spacing` and create new pixel by interpolation.
          - check this to ignore the output spacing argument and keep the original pixels.

------

### Additional information (move to main text?)

Since the voxels dimensions are anisotropic in this data set, reslicing it would yield rectangular pixels. However, on your screen pixels always appear as squares. Therefore there are two options:
- new pixels are added by interpolation to keep the proportions such that they follow the calibration of the image.
- the pixels are kept the same, but we keep in mind that the voxel size is larger in one dimension than in the other (this is stored in the calibration metadata)

With the 'avoid interpolation' box NOT selected, the resliced output of a calibrated image will contain new pixels (calculated by interpolation), such that the XYZ proportions in the image follow the image XYZ calibration. However, the resliced output image no longer contains the exact same pixels as the input image, and reslicing it back will give you a slightly different image than the input image that you started with. If you select the 'avoid interpolation' box, the output image will have the same number of pixels as the input image. In this case, reslicing it back again will return  the exact same input image that you started with. However, the proportions that you see on your screen do not reflect the 'real' physical proportions that the original object had.
