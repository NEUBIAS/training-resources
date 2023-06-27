<h4 id="measure"><a href="#measure">Measure object intensities with background subtraction</a></h4>

##### Measure object intensities

- Measure the objects' **mean** and **max** intensities and pixel **area**.
- Measure the mean intensity in the image background
- Exports the results as a table and open in a spreadsheet software.
- Create new columns for background corrected mean, max, and sum intensity.
- Discuss the measurements' biophysical interpretation

##### Explore influence of the object regions on measurement results

- Discuss that due to the diffraction limit is not obvious how to exactly deliniate objects in a fluorescence microscopy image
- Measure the objects' intensities in significantly larger regions as above.
- Explore and understand how the measurement values changed.

#### Data

- Intensity image: [xy_16bit__h2b.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__h2b.tif)
    - H2B-mCherry staining acquired with a widefield microscope
- Label image: [xy_8bit_labels__h2b.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b.tif)
- Larger label image: [xy_8bit_labels__h2b_dilate_labels.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b_dilate_labels.tif)
