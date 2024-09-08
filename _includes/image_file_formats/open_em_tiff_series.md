<h4 id="open_em_tiff_series"><a href="#open_em_tiff_series">Open volume EM TIFF series</a></h4>

- Open a series of 2D TIFF files representing an EM volume 
- Observe the data is distributed onto several files on disk
- Observe that crucial metadata, namely the z slice position, is part of the file name
- Observe that the pixel calibration metadata is wrong
  - Try to find the metadata at the EMPIAR website 
- Discuss that while the 2D calibration could be part of the TIFF slice files, it is not so obvious where to store the z spacing, because the individual files are only 2D and thus may not have a metadata tag for the z-dimension  

##### Data

- [EM TIFF Series](https://github.com/NEUBIAS/training-resources/raw/master/image_data/image_data/xyz_8bit__em_volume_tiff_series.zip)
  - From https://www.ebi.ac.uk/empiar/EMPIAR-10982/ 
  - ZIP archive, please uncompress after download 