- Open [xyz_16bit__spots.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit__spots.tif)
  - [File > Import URL]: https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit__spots.tif

### Z axis projection

- `run("Z Project...", "projection=[Max Intensity]");`
- `run("Z Project...", "projection=[Sum Slices]");`
- Compare pixel values and image data types

### X and Y axis projection
 
There is no easy way to project along the x or y axis in ImageJ. 
We first need to rotate the stack and then project again along the z-axis.

For rotating we use TransformJ, which has many useful functions for dealing with 3D data.
This requires the very useful [update site](https://imagej.net/update-sites/following): [ImageScience](https://imagej.net/libs/imagescience).

- `run("TransformJ Turn", "z-angle=0 y-angle=90 x-angle=0");`
- `run("Z Project...", "projection=[Max Intensity]");`
- `run("TransformJ Turn", "z-angle=0 y-angle=0 x-angle=90");`
- `run("Z Project...", "projection=[Max Intensity]");`

### Resampling for isotropic appearance

You notice that the images do not look correct in a physical sense, but squashed.
This is a mismatch of the "data space", where the voxels live, and "physical space".
To counter this we need to resample the images, generating new voxels in the data space by interpolation.
Note that some image viewers may do such resampling automatically.

- Select one of the projected (x or y axis) images
- run("Properties...")
- Compute the scaling factor: 0.4 / 0.0941345 = 4.249239
- Rescale the x-projection: run("Scale...", "x=1.0 y=4.249239 z=1.0 interpolation=Bilinear average create");
- Rescale the y-projection: run("Scale...", "x=4.249239 y=1.0 z=1.0 interpolation=Bilinear average create");

