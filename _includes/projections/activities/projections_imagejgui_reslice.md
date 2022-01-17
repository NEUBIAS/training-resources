#### Open an image

- Open [xyz_16bit__spots.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit__spots.tif)
- Drag and drop above link onto Fiji or [File > Import > URL...]: https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit__spots.tif

#### Z axis projection

- `run("Z Project...", "projection=[Max Intensity]");`
- `run("Z Project...", "projection=[Sum Slices]");`
- Compare pixel values and image data types
- Appreciate that the data type of the sum projection is different to the original image.
- Discuss whether the data type change was necessary in this specific case.

#### X and Y axis projection
There is no easy way to project along the x or y axis in ImageJ.
We need to rearrange the stack such that the new z axis is the one along which to project.

- Maximum projection along x axis
  - `run("Reslice [/]...", "start=Left avoid");`
  - Note that the image has the same number of pixels, but rearranged.
  - Note that also the voxel sizes `run("Properties..)` have changed. 
  - `run("Z Project...", "projection=[Max Intensity]");`
- Maximum projection along y axis
  - `run("Reslice [/]...", "start=Top avoid");`
  - `run("Z Project...", "projection=[Max Intensity]");`

#### Appearance of anisotropic images
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

