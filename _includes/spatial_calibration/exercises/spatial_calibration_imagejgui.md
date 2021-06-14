1. Open [xy_8bit__nucleus_calibrated.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nucleus_calibrated.tif)
 and note down the pixel width and pixel height. 
2. Open [xyz_8bit__nucleus.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__nucleus.tif) and add the spatial calibration. 
The pixel width and pixel height is the same as previous image. Voxel-depth is 0.52 um.
3. What is the length of the longest axis of the nucleus?

> ## Solution
> 1. **[File > Open ]** the image and then **[Image > Properties ...]** or **[Ctrl-Shift-P]**. Pixel-height = pixel-width = 0.13 um.
> 2. Open the 3D image and change the properties from the **[Image > Properties ...]** gui and the unit.
> 3. Maximal extension is ~ 19.2 um. Move to the middle of the nucleus (~ z-slice 3) and draw a line using the line-tool. 
{: .solution}