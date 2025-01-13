Create a local directory and download a set of sample images:

```bash
mkdir /path/to/tiff_series # eg: ~/image_data_course/data/tiff/tiff_series
cd /path/to/tiff_series # eg: ~/image_data_course/data/zarr/outputs/zarr_series
for i in {001..020}; do
    curl -L0 \
    https://github.com/NEUBIAS/training-resources/raw/refs/heads/master/image_data/xyz_8bit__em_volume_tiff_series/c_elegans_em_z0$i.tif \
    --output $PWD/c_elegans_em_z0$i.tif
done
```
There are multiple conversion modes. Let's try each of them.

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
