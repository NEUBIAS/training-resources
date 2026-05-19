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

### Open a remote OME-Zarr in Fiji
- Open the n5-ij in Fiji via: 
  - `[ File > Import > HDF5/N5/Zarr/OME-NGFF ... ]`<br><br>

- In the window that opens, paste the following path in the uri space:
  - `https://s3.embl.de/ome-zarr-course/data/commons/xyz_8bit_calibrated__fib_sem_crop.ome.zarr`<br><br>

- Then click `Detect datasets` button as shown below: 
<img src="{{ site.baseurl }}/figures/n5-ij/detect_datasets.png" alt="Detect Datasets" style="display: block; margin: 2px 0;" /><br><br>

- The tool will display a multiscales schema with two datasets in the dialog box.
Select one of the datasets as shown below and click OK:
<img src="{{ site.baseurl }}/figures/n5-ij/select_dataset1.png" alt="Detect Datasets" style="display: block; margin: 2px 0;" /><br><br>

- This will open the dataset in Fiji as a normal Fiji image (see below).
<img src="{{ site.baseurl }}/figures/n5-ij/opened_dataset1.png" alt="Detect Datasets" style="display: block; margin: 2px 0;" /><br><br>

<h3>Open a subset of a remote OME-Zarr in Fiji</h3>
- Follow the same steps above do select a dataset but instead of directly opening the dataset,
click the crop button in the window before clicking OK as shown below: <br>
<img src="{{ site.baseurl }}/figures/n5-ij/select_dataset_and_crop2.png" alt="Detect Datasets" style="display: block; margin: 2px 0;" /><br><br>

- In the window that open, select the indices of the subset as shown below: <br> 
<img src="{{ site.baseurl }}/figures/n5-ij/select_dataset_and_crop1.png" alt="Detect Datasets" style="display: block; margin: 2px 0;" /><br><br>

- When you click OK, the specified subset of the image will be opened as shown below: <br>
<img src="{{ site.baseurl }}/figures/n5-ij/cropped_dataset1.png" alt="Detect Datasets" style="display: block; margin: 2px 0;" /><br><br>
