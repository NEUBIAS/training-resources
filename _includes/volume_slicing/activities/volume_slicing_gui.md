-  Open the 3D image [xyz_8bit_sphere_calibrated.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_sphere_calibrated.tif).
- Go to **[ Image > Stacks > Orthogonal Views ]** or **[Ctrl-Shift-H]** to see the orthogonal views of the image.
- Go to **[ Image > Properties... ]** or **[Ctrl-Shift-P]** to open the properties window to view the voxel dimensions. If you change all dimensions to 1 pixel, you will see that the ball appears as an oval in the 'Orthogonal Views' option.
- Open the multidimensional image [xyzc_8bit_beads_p_open.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit_beads_p_open.tif).
- Use the sliders to explore different dimensions in the data.
- Use **[ Image > Color > Channels Tool... ]** or **[Ctrl-Shift-Z]** to toggle different channels.
- Go to **[ Image > Properties... ]** or **[Ctrl-Shift-P]** to open the properties window to view the voxel dimensions. In this image the voxel dimensions are anisotropic (voxel width and height are not equal to voxel depth).
- Select the rectangular selection tool and draw an ROI around the green bead.
- Go to **[ Image > Duplicate ]** or **[Ctrl-Shift-D]**. Tick 'Duplicate hyperstack', select channel 1 and slice 15-25 to crop out the green bead.
- With the cropped out green bead as the active image, go to **[ Image > Stacks > Reslice]** or press **/** to open the reslice menu. Select 'Top' and click OK.

Since the voxels dimensions are anisotropic in this data set, reslicing it would yield rectangular pixels. However, on your screen pixels always appear as squares. Therefore there are two options:
- new pixels are added by interpolation to keep the proportions such that they follow the calibration of the image.
- the pixels are kept the same, but we keep in mind that the voxel size is larger in one dimension than in the other (this is stored in the calibration metadata)

With the 'avoid interpolation' box NOT selected, the resliced output of a calibrated image will contain new pixels (calculated by interpolation), such that the XYZ proportions in the image follow the image XYZ calibration. However, the resliced output image no longer contains the exact same pixels as the input image, and reslicing it back will give you a slightly different image than the input image that you started with. If you select the 'avoid interpolation' box, the output image will have the same number of pixels as the input image. In this case, reslicing it back again will return  the exact same input image that you started with. However, the proportions that you see on your screen do not reflect the 'real' physical proportions that the original object had.
