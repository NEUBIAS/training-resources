<h4 id="measure"><a href="#measure">Measure intensities (with background subtraction)</a></h4>

##### Use the labels provided to measure objects intensities

- Open image [xy_16bit__h2b.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__h2b.tif)
- H2B-mCherry staining acquired with a widefield microscope
- Open label mask [xy_8bit_labels__h2b.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b.tif)
- Using the label mask, measure the mean and max intensities as well as the objects' pixel area.
- Exports the results as a table (and open in a spreadsheet software)
- Manually measure the mean intensity in the background.
- Add the background measurement as a new column to the table
- Create new columns for background corrected mean, max, and sum intensity.
- Discuss the measurements' biophysical interpretation

##### Now try using larger labels (optional)

- Open image [xy_16bit__h2b.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__h2b.tif) 
- Open label mask [xy_8bit_labels__h2b_dilate_labels.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b_dilate_labels.tif)
- Appreciate that it is not always clear how large exactly the label regions have to be
- Measure the intensities with the larger label mask
- Discuss which values changed compared to label mask [xy_8bit_labels__h2b.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b.tif) and by how much percent
