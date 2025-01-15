<h4 id="open_em_tiff_series"><a href="#open_em_tiff_series">Open volume EM TIFF series</a></h4>

- Open a series of 2D TIFF files representing an EM volume 
- Observe the data is distributed onto several files on disk
- Observe that crucial metadata, namely the z slice position, is part of the file name
- Observe that the pixel calibration metadata is wrong
  - Try to find the metadata at the [EMPIAR website](https://www.ebi.ac.uk/empiar/EMPIAR-10982/)
- Discuss that for a 2D file series, it is not obvious where to store the z spacing, because the individual files are only 2D and thus may not have a metadata tag for the z-dimension
- Discuss that using [pattern files](https://bio-formats.readthedocs.io/en/stable/formats/pattern-file.html) might be useful for such data that is distributed across multiple files  

##### Data

- [EM-TIFF-Series.ZIP](https://github.com/NEUBIAS/training-resources/raw/refs/heads/master/image_data/xyz_8bit__em_volume_tiff_series.zip)
  - The data is from https://www.ebi.ac.uk/empiar/EMPIAR-10982/ 
  - If the above link does not work, please [download from here](https://github.com/NEUBIAS/training-resources/blob/master/image_data/xyz_8bit__em_volume_tiff_series.zip)