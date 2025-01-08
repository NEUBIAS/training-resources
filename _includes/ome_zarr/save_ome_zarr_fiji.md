<style>
body {
    font-size: 20px !important;
}
h3 {
    font-size: 24px !important;
}
h4 {
    font-size: 22px !important;
}
</style>

### Export OME-Zarr from Fiji


- Drag and drop the czi image from the path `~/ome_zarr_course/data/czi/xyz__multiple_images.czi` as shown below: 
<img src="{{ site.baseurl }}/figures/n5-ij/save_image/import_czi.png" alt="Import czi" style="display: block; margin: 2px 0;" /><br><br>
- A window titled **Bioformats Import Options** will open. Then click OK without changing any options.<br><br>
- Another window titled **Bioformats Series Options** will open. This shows that the czi file contains two independent
images (or "series" in bioformats terminology). Then select one of the images and click OK as shown below:<br><br>
<img src="{{ site.baseurl }}/figures/n5-ij/save_image/select_series.png" alt="Select series" style="display: block; margin: 2px 0;" /><br><br>
- Now open the **n5-ij's saving tool** via: 
  - `[ File > Save As > HDF5/N5/Zarr/OME-NGFF ... ]` as shown below<br><br>
<img src="{{ site.baseurl }}/figures/n5-ij/save_image/save_as_zarr.png" alt="Open n5-ij" style="display: block; margin: 2px 0;" /><br><br>
- This will open a window with saving options (which define the properties of the output OME-Zarr) as shown below:
<img src="{{ site.baseurl }}/figures/n5-ij/save_image/configure_parameters_for_ngff.png" alt="Configure params" style="display: block; margin: 2px 0;" /><br><br>