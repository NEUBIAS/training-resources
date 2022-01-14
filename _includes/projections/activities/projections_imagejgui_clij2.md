### Install CLIJ2
In ImageJ one can project along the z axis, but there is no easy way to project along the x or y axis.
Thus let's install the the very useful [update site](https://imagej.net/update-sites/following): [CLIJ2](https://clij.github.io/).

- [Help > Update...]
- [Manage update sites]
- [X]  clij
- [X]  clij2

### Open example image

Open [xyz_16bit__spots.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit__spots.tif).

### Z axis projection

- Sum projection: [Plugins › ImageJ on GPU (CLIJ2) › Projections › Sum-Z-projection on GPU]
- Maximum projection: [Plugins › ImageJ on GPU (CLIJ2) › Projections › Max-Z-projection on GPU]
- Compare the pixel values and data types of the two images.
- Appreciate that the data type of the sum projection is different to the original image.
  - Discuss whether this was necessary in this specific case.

### X and Y axis projection

- Maximum projection X: [Plugins › ImageJ on GPU (CLIJ2) › Projections › Max-X-projection on GPU]
- Maximum projection Y: [Plugins › ImageJ on GPU (CLIJ2) › Projections › Max-Y-projection on GPU]

### Appearance of anisotropic images
Notice that the images do not look correct in a physical sense, but squashed.
This is due to a mismatch of the data (voxel) space and physical space.

- Select one of the projected (x or y axis) images
- `run("Properties...")`
- Observe that the voxel sizes are correct, but the ImageJ viewer does not take them into account for rendering.
- Opening the same image in BigDataViewer paints a different picture: [ Plugins > BigDataViewer > Open Current Image...]

### Resampling (optional)
To achieve a more correct appearance in physical space in the ImageJ viewer we need to up-scale the image and add more voxels. Note that while this is good for visualization, it does change the data and should thus be done with care.

- Compute the scaling factor: 0.4 / 0.0941345 = 4.249239
- Rescale the x-projection: `run("Scale...", "x=1.0 y=4.249239 z=1.0 interpolation=None average create");`
- Rescale the y-projection: `run("Scale...", "x=4.249239 y=1.0 z=1.0 interpolation=None average create");`

