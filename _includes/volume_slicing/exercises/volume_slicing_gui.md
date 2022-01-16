Open the multidimensional image [xyz_16bit_t1-head.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit_t1-head.tif).
- Reslice the image from different directions, such that you can view the image stack from -the side, from the top, and from the front.
- Are the voxels in this data isotropic or anisotropic?
- What do you think the 'avoid interpolation function is doing?'


> ## Solution
> - **[File > Open...]** [xyz_16bit_t1-head.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit_t1-head.tif)
> - **[Image > Stacks > Reslice [/]...]** or **[/]** opens the Reslice menu.
> - Select 'Top' in the 'Start at:' drop-down menu to reslice the image from the top and view the head from above.
> - Select 'Left' in the 'Start at:' drop-down menu to reslice the image from the left and view the head from the front.
> - Tick the 'Rotate 90 degrees' button to rotate the output image (you can use this when reslicing from the left, so that the top of the head remains pointing upwards.)
> - Ticking the 'Avoid interpolation box' matters when you have anisotropic data. In this case the data is isotropic (voxels are 1.5 x 1.5 x 1.5 mm), so it has no effect, unless you specified a different output spacing in the 'Output spacing' box at the top of the menu. You can view what happens when you change the voxel dimensions in the properties window (**[Ctrl-Shift-P]**). For example, set the voxel depth to 5 mm. If you now reslice and tick the 'Avoid interpolation box' the output image will still show the same proportions, and the voxel dimensions will be adjusted (now Pixel height or width will be 5 mm). If you leave the 'Avoid interpolation box' unticked, you will see a stretched image. To obtain this result, FIJI has added pixels along one dimension, using interpolation, while removing pixels in the other dimension. You can see this when you compare the image XYZ dimensions.
{: .solution}
