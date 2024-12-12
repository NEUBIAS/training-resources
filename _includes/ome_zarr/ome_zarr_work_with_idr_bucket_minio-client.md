**Create a project directory and cd into that**
```bash
mkdir ~/ome_zarr_course && cd ~/ome_zarr_course
mkdir data 
```

**Connect to the EBI server:**

'''
mc alias set uk1s3 https://uk1s3.embassy.ebi.ac.uk
'''

No need to provide access and secret keys for this public resource. When requested to supply credentials, simply click `enter`.

**Check out the contents of the IDR bucket dedicated to OME-Zarr data:**
``` 
mc tree -d 1 uk1s3/idr/
``` 
``` 
mc ls uk1s3/idr/zarr/v0.4/idr0062A/6001240.zarr
```

**Check out the multiscales metadata for an example OME-Zarr dataset:**
``` 
mc cat uk1s3/idr/zarr/v0.4/idr0062A/6001240.zarr/.zattrs
``` 

**Check out the array metadata for the highest resolution array:**
``` 
mc cat uk1s3/idr/zarr/v0.4/idr0062A/6001240.zarr/0/.zarray
```

**Download the example data for local use:**
```
mc mirror uk1s3/idr/zarr/v0.4/idr0062A/6001240.zarr ~/ome_zarr_course/data/zarr/6001240.zarr
```