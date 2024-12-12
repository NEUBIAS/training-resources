**First check out what data we have the s3 end:**
```bash
mc tree -d 2 s3/ome-zarr-course/
```

There are multiple conversion modes. Let's try each of them.

**Perform parallelised, independent conversion:**
```bash
batchconvert omezarr -st s3 -dt s3 --drop_series data/MFF data/ZARR/$USER;
```
This command maps each input file in the `data/MFF` folder to a single OME-Zarr series, which is then transferred to a user-specific folder.
Note that the `-st s3` option makes sure that the input path is searched for in the s3 bucket, while `-dt s3` triggers the output files to be transferred to the s3 bucket under the output path.

**Perform grouped conversion:**

```bash
batchconvert omezarr -st s3 -dt s3 --drop_series --merge_files --concatenation_order t data/JPEG data/ZARR/$USER;
```
This conversion mode assumes that the input files are part of the same series and thus will merge them along a specific axis during the conversion process.
The `--merge_files` flag specifies the grouped conversion option and the `--concatenation_order t` option allows the files to be merged along the time channel. 

**Check what has changed at the s3 end after the conversion:**
```bash
mc tree -d 2 s3/ome-zarr-course/
```
```bash
mc ls s3/ome-zarr-course/data/ZARR/$USER/
```

**Optional: Copy the converted Zarr data to the home folder:**
```bash
mc mirror s3/ome-zarr-course/data/ZARR/$USER ~/data/ZARR;
```
