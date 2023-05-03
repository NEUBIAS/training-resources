Check out what we have at our s3 bucket:

``` 
mc tree -d 3 s3/ome-zarr-course/
``` 
``` 
mc ls s3/ome-zarr-course/data/MFF/
``` 
``` 
mc ls s3/ome-zarr-course/data/JPEG/
```
``` 
mc ls s3/ome-zarr-course/data/ZARR/common/
```

Check out the multiscales metadata for one of the existing OME-Zarr datasets:
``` 
mc cat s3/ome-zarr-course/data/ZARR/common/13457537T.zarr/.zattrs
```

Check out the array metadata for the highest resolution array:
``` 
mc cat s3/ome-zarr-course/data/ZARR/common/13457537T.zarr/0/.zarray
```
