Open the multidimensional image [xyz_16bit_t1-head.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit_t1-head.tif).
- Reslice the image from different directions, such that you can view the image stack from the side, from the top, and from the front.
- Are the voxels in this data isotropic or anisotropic?
- How do you think one could see the head from 3/4 view? Tip: there is a function called 'rotate' in ImageJ (**[Image > Transform > Rotate]**).

> ## Solution
> - **[File > Open...]** [xyz_16bit_t1-head.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit_t1-head.tif)
> - **[Image > Stacks > Reslice [/]...]** or **[/]** opens the Reslice menu.
> - Select 'Top' in the 'Start at:' drop-down menu to reslice the image from the top and view the head from above.
> - Select 'Left' in the 'Start at:' drop-down menu to reslice the image from the left and view the head from the front.
> - Tick the 'Rotate 90 degrees' button to rotate the output image (you can use this when reslicing from the left, so that the top of the head remains pointing upwards.)
> - When viewing the head from the top, you can select **[Image > Transform > Rotate]**. Select 45 degrees and 'Enlarge Image' and say yes to 'Process Stack?" question. If you now reslice again from the top, you will see the head in 3/4 view.
{: .solution}
