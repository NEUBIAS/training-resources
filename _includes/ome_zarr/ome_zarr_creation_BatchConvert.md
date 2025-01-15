#### Perform parallelised conversion of image data collections to OME-Zarr using BatchConvert

**Important note: BatchConvert is currently only supported on unix-based systems**

As input, use the `tiff_series` dataset.

**Perform parallelised, independent conversion:**
```bash
batchconvert omezarr \
/path/to/tiff_series \
/path/to/zarr_series 
```
This command maps each input file in the `tiff_series` folder to a single OME-Zarr, 
which is then transferred to the `zarr_series` folder.

Check the content of the `zarr_series` folder:
```bash 
ls /path/to/zarr_series
```
Optional: Inspect the created OME-Zarr. 

**Perform grouped conversion:**

```bash
batchconvert omezarr \
--merge_files \
/path/to/tiff_series \
/path/to/zarr_series_concatenated
```
This conversion mode assumes that the input files are part of the same image and thus will merge them along a specific axis during the conversion process.
The `--merge_files` flag specifies the grouped conversion option.

Check the content of the `zarr_series_concatenated` folder:
```bash 
ls /path/to/zarr_series_concatenated
```
Optional: Inspect the created OME-Zarr. 


**Perform grouped conversion with specific chunking and downscaling parameters:**

```bash
batchconvert omezarr \
--merge_files \
-ms 32 \
-cx 32 \
-cy 32 \
-cz 6 \
/path/to/tiff_series \
/path/to/zarr_series_concatenated_rechunked
```
Here we do not only concatenate images, but we create a resolution pyramid and
specify chunk sizes in x, y and z dimensions.

Check the content of the `zarr_series_concatenated_rechunked` folder:
```bash 
ls /path/to/zarr_series_concatenated_rechunked
```
Optional: Inspect the created OME-Zarr. Compare it to the one created earlier.



```bash
batchconvert omezarr input_path output_path 
```

```bash
bfconvert input_path output_path 
```