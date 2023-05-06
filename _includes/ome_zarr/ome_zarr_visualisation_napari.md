**Visualise the remote data using Napari together with the napari-ome-zarr plugin.**

```
napari --plugin napari-ome-zarr https://s3.embl.de/ome-zarr-course/data/ZARR/$USER/xyzct_8bit__mitosis.ome.zarr
```

```
napari --plugin napari-ome-zarr https://s3.embl.de/ome-zarr-course/data/ZARR/$USER/xyz_8bit_calibrated__fib_sem_crop.ome.zarr
```

**Optional: visualise local OME-Zarr data in the same way:**
```
napari --plugin napari-ome-zarr ~/data/ZARR/xyzct_8bit__mitosis.ome.zarr
```

**Optional: visualise big remote OME-Zarr data:**
```
napari --plugin napari-ome-zarr https://s3.embl.de/i2k-2020/platy-raw.ome.zarr
```
Note that compared to BigDataViewer, there are more delays with Napari.
