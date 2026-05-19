* Open image:  [xyz_8bit__mitotic_plate_calibrated.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__mitotic_plate_calibrated.tif)
* Check the pixel sizes (calibration) of this image
* Where to see the calibration?
  * Next to the pixel indices in the ImageJ menu bar
  * Properties of the image **[Image > Properties]** or **[Shift-Ctrl-P]**
* How to check whether the calibration makes sense?
  * Explore the typical size of objects in 3D. 
     * Orthogonal view **[Image > Stacks > Orthogonal Views]** or **[Ctrl-Shift-H]**
  * An example of a wrong calibration: [xyz_8bit__mitotic_plate_badZcalibrated.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__mitotic_plate_badZcalibrated.tif)
* Appreciate that image calibration might be necessary, e.g.
  * 2D distance measurement between two pixels
    * One can use the Line tool
  * 3D distance measurement between two voxels
    * One cannot use the Line tool but needs to measure manually: `sqrt( (x0-x1)^2 + (y0-y1)^2 + (z0-z1)^2 )`
      * Note: It is critical to use the calibrated voxel positions and not the voxel indices in above formula!
* Appreciate that image calibration can be confusing, e.g.
  * It is not consistently used in image filter parameter specification
