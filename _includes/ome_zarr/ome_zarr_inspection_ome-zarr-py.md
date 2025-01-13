**Use the ome_zarr tool for the inspecting and downloading OME-Zarrs from s3:**

Remote OME-Zarr data stored in a public s3 bucket can be inspected and downloaded using 
the `ome-zarr-py` tool. 

Inspect 3 different remote datasets:

```bash
ome_zarr info https://uk1s3.embassy.ebi.ac.uk/EuBI/anna_steyer0/20160112_C.elegans_std_fullhead.zarr
```

```bash
ome_zarr info https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0062A/6001240.zarr
```

```bash
ome_zarr info https://s3.embl.de/i2k-2020/platy-raw.ome.zarr
```

**Optional:** Download the dataset `6001240.zarr` from s3 to a local path:

```bash
# cd ~/ome_zarr_course/data/zarr
cd /path/to/local/zarr # where you want to keep the data on your system
ome_zarr download https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0062A/6001240.zarr
```

