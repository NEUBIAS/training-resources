<h4 id="no_optical_sectioning_in_wf"><a href="#wf">No optical sectioning in widefield microscopy</a></h4>
- Example data:
  - Z-Stack with two "channels", namely the same nucleus imaged with confocal and widefield fluorescence microscopy: [xyzc_16bit__dna_conf_wf.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_16bit__dna_conf_wf.tif)
- Appreciate that a widefield image has the following properties:
  - Depending on the z-position, different structures appear crisp
  - However, the sum intensity in the image does (ideally) not depend in the z-position
  - The latter has severe consquences for intensity measurements, namely wide-field microsopy is great to measure the total sum intensity of an object, but cannot be used to compare intensities at different z-positions
  - This is very different from a confocal image, where the pinhole serves to only collect light at the current z-position
