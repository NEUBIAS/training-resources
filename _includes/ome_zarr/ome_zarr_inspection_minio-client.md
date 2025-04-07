Note: This activity requires the minio-client to be installed.
You can install it via conda using the command below. **It is important to note that this 
conda installation is currently only supported on unix systems without an ARM architecture.** 

```bash
conda install -c joshmoore go-mc
```

If you are on Windows or on an ARM-based machine, follow the 
[instructions](https://min.io/docs/minio/linux/reference/minio-mc.html) from the provider:


**Configure the S3 endpoint:**

```bash
mc alias set uk1s3 https://uk1s3.embassy.ebi.ac.uk
```

No need to provide access and secret keys for this public resource. When requested to supply credentials, simply click `enter`.

**Check out the contents of a bucket containing OME-Zarr data:**

```bash
mc tree -d 1 uk1s3/idr/
``` 

```  bash
mc ls uk1s3/idr/zarr/v0.4/idr0062A/6001240.zarr
```

**Check out the multiscales metadata for an example OME-Zarr dataset:**

```bash
mc cat uk1s3/idr/zarr/v0.4/idr0062A/6001240.zarr/.zattrs
``` 

**Check out the array metadata for the highest resolution array:**

This will allow you to check how much data you have in each dimension and also how it is chunked.

```bash
mc cat uk1s3/idr/zarr/v0.4/idr0062A/6001240.zarr/0/.zarray
```

#### Other examples

```bash
mc alias set embl https://s3.embl.de
mc ls embl/i2k-2020/platy-raw.ome.zarr
mc cat embl/i2k-2020/platy-raw.ome.zarr/.zattrs | jq .
```

In the above example the `| jq .` will result in a pretty printing of the JSON content of the `.zattrs` file.


