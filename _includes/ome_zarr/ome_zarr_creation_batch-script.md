The remote datasets can be converted in a parallelised manner by using the batchconvert tool.

#### First check out what data we have the s3 end:
```
mc tree -d 2 s3/ome-zarr-course/
```

#### Independent conversion of the input files:
The followin command will map each input file in the `data/MFF` folder to a single OME-Zarr series, which will be located in a specific directory for each user. 

```
batchconvert omezarr -st s3 -dt s3 --drop_series data/MFF data/ZARR/$USER;
```
Note that the `-st s3` option will make sure that the input path is searched for in the s3 bucket, while `-dt s3` will trigger the output files to be transferred to the s3 bucket under the output path.

#### Grouped conversion mode:

Another conversion mode will assume that the input files are part of the same series and thus will merge them along a specific axis during the conversion process.
```
batchconvert omezarr -st s3 -dt s3 --drop_series --merge_files --concatenation_order t data/JPEG data/ZARR/$USER;
```
The `merge_files` flag will ensure the grouped conversion option and the `--concatenation_order t` option will make sure that the files will be merged along the time channel. 

#### Check what has changed at the s3 end after the conversion:
```
mc tree -d 2 s3/ome-zarr-course/
```
```
mc ls s3/ome-zarr-course/data/ZARR/$USER/
```

#### (Optional) Copy the converted Zarr data to the home folder:
```
mc mirror s3/ome-zarr-course/data/ZARR/$USER ~/data/ZARR;
```
