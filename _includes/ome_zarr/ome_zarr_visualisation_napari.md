#### Visualise the remote data using Napari together with the napari-ome-zarr plugin.

**Use command line:**
``` bash
napari --plugin napari-ome-zarr https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0062A/6001240.zarr
```

**Use Python code:**

Approach 1: Open the full OME-Zarr from the top level url:
```python
import napari
import zarr, dask.array as da
 
v = napari.Viewer()
v.open("https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0062A/6001240.zarr",
       plugin = 'napari-ome-zarr'
       )
napari.run()
```
Note that this approach automates a lot of tasks for the user,
discovering look-up tables, pixel scalings and units from the OME-Zarr metadata.

Approach 2: Read arrays and open them individually:
```python
import napari
import zarr, dask.array as da

url = "https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0062A/6001240.zarr"
gr = zarr.open_group(url, mode = 'r')
#array0 = da.from_zarr(gr[0])
array2 = da.from_zarr(gr[2])
#label_array0 = da.from_zarr(gr.labels['0'][0])
label_array2 = da.from_zarr(gr.labels['0'][2])
v = napari.Viewer()
#v.add_image(array0, contrast_limits = (0, 2000), colormap = 'yellow')
v.add_image(array2, contrast_limits = (0, 2000), colormap = 'red')
#v.add_labels(label_array0)
v.add_labels(label_array2)
napari.run()
```

Note that approach 2 is flexible but does not use any metadata. You have to
specify the metadata to the viewer manually.