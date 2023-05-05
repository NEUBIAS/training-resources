Visualise the remote data using Napari together with the napari-ome-zarr plugin.

```
napari --plugin napari-ome-zarr https://s3.embl.de/ome-zarr-course/data/ZARR/$USER/xyzct_8bit__mitosis.ome.zarr
```

Optional: visualise local OME-Zarr data in the same way:
```
napari --plugin napari-ome-zarr ~/data/ZARR/xyzct_8bit__mitosis.ome.zarr
```