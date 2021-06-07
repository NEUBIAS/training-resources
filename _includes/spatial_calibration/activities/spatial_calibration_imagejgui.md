## Explore pixel sizes 

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
  * 3D distance measurements between two voxels, v0 and v1 at indices (x0,y0,z0) and (x1,y1,z1)
    * sqrt( (x0*dx-x1*dx)^2 + (y0*dy-y1*dy)^2 + (z0*dz-z1*dz)^2  
* Appreciate that image calibration can be confusing, e.g.
  * not consistently used in image filter parameter specification
