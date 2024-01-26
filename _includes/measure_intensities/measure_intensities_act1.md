<h4 id="measure"><a href="#measure">Measure background corrected intensities</a></h4>

- Open image [xy_16bit__h2b.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__h2b.tif)
  - The image contains H2B-mCherry staining acquired with a widefield microscope
- Delinate the nuclei, either
  - Manually draw the object outlines (ROIs), or
  - Open a label mask [xy_8bit_labels__h2b.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b.tif)
- Measure the mean and max intensities as well as the objects' pixel area.
- Make sure to also measure the mean intensity in the background and record this information
- Export the results as a table and open in a spreadsheet software
- Compute new columns for background corrected mean, max, and sum intensity.
- Discuss the measurements' biophysical interpretation

##### Repeat the activity using larger object regions

Due to the diffraction blur there is some subjectivity to how excatly to delineate the objects. Thus is is useful to compare how the measured values change when using larger regions.

- Open image [xy_16bit__h2b.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__h2b.tif) 
- Measure the intensities with the larger object regions, either
  - Manually draw larger ROIs, or
  - Open an enlarged label mask [xy_8bit_labels__h2b_dilate_labels.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b_dilate_labels.tif)
- Discuss how the results are affected by the ROI size
