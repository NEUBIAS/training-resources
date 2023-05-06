**Check out what we have at our s3 bucket:**
``` 
mc tree -d 2 s3/ome-zarr-course/
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


**Check out the multiscales metadata for one of the OME-Zarr datasets we created:**
``` 
mc cat s3/ome-zarr-course/data/ZARR/common/13457537T.zarr/.zattrs
``` 

**Check out the array metadata for the highest resolution array:**
``` 
mc cat s3/ome-zarr-course/data/ZARR/common/13457537T.zarr/0/.zarray
```

**Configure mc for anonymous access to public s3 buckets:**
```
mc alias set s3pub https://s3.embl.de
```

**Have a look at the metadata for a big OME-Zarr data:**
```
mc cat s3pub/i2k-2020/platy-raw.ome.zarr/.zattrs
```

```
mc cat s3pub/i2k-2020/platy-raw.ome.zarr/s0/.zarray
```
