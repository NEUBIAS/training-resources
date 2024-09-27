- Open the 3D multi-channel image [xyzc_8bit_spheres.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit_spheres.tif).
  - Use the sliders to explore different dimensions in the data.
  - Explore the voxel dimensions, using **[ Image > Properties... ]** or **[Ctrl-Shift-P]**.
    - Observe that the voxel dimensions are anisotropic.
  - Crop out the green sphere (i.e. "subset" the data).
    - Select the rectangular selection tool and draw an ROI around the green sphere.
    - Duplicate the selection, using **[ Image > Duplicate ]** or **[Ctrl-Shift-D]**.
      - [X] `Duplicate hyperstack`
      - `Channels: 2`
      - `Slices: 3-11`
    - Draw a vertical line along the sphere and create a YZ slice with and without interpolation:
      - **[ Image > Stacks > Reslice]** or press **/** to open the reslice menu.
        - Output spacing: 2.000 um
        - Select `Top`
        - [X] `Rotate 90 degrees`
        - [ ] `avoid interpolation`
        - Click `OK`.
      - **[ Image > Stacks > Reslice]** or press **/** to open the reslice menu.
        - Select `Top`
        - [X] `Rotate 90 degrees`
        - [X] `avoid interpolation`
        - Click `OK`.

Further explanation

Since the voxels dimensions are anisotropic in this data set, reslicing it would yield rectangular pixels. However, on your screen pixels always appear as squares. Therefore there are two options:
- new pixels are added by interpolation to keep the proportions such that they follow the calibration of the image (you can witness the effect in the black square in the green sphere).
- no pixels are added by interpolation, but we keep in mind that the voxel size is larger in one dimension than in the other (this is stored in the calibration metadata). In the green sphere slice, you will see that the black square is a rectangle in the YZ view. 

