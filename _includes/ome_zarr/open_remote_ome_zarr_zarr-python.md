**Import the necessary tools:**
```Python
import zarr, s3fs, os, pprint
import numpy as np
```

**Open a remote OME-Zarr using `zarr.open_group`**
```Python
url = "https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0062A/6001240.zarr"
dataset = zarr.open_group(url, mode = 'r')
print(f"Type of the dataset: {type(dataset)}")
```

**Summarize group-level metadata:**
```Python
dataset.info
```
Note the store type, the number of arrays and groups. \
Note also the group named 'labels'.

**Print the full metadata:**
```Python
pprint.pprint(dict(dataset.attrs))
```

**Get multiscales metadata:**
```Python
meta = dict(dataset.attrs['multiscales'][0])
```

**Print the axis ordering and the units**
```Python
pprint.pprint(meta['axes'])
axis_order = ''.join(item['name'] for item in meta['axes'])
print(f"Axis order is {axis_order}")
```
**Print the voxel scaling for each resolution level**
```Python
for idx, transform in enumerate(meta['datasets']):
    print(f"\033[1mVoxel transform for the level {idx}:\033[0m")
    pprint.pprint(transform)
```
**Get the top resolution array:**
```Python
zarr_array0 = dataset[0]
print(f"Array type: {type(zarr_array0)}")
print(f"Shape of the top-level array: {zarr_array0.shape}")
```
**Get a downscaled array:**
```Python
zarr_array1 = dataset[1]
print(f"Array type: {type(zarr_array1)}")
print(f"Shape of the first-level downscaled array: {zarr_array1.shape}")
```
**Summarize array-level metadata:**
```Python
zarr_array0.info
zarr_array1.info
```
**Print chunk size for the top layer:**
```Python
print(f"Chunk size: {zarr_array0.chunks}")
```

**Convert the zarr array to a numpy array:**
```Python
numpy_array0 = zarr_array0[:]
print(f"Array type: {type(numpy_array0)}")
# or use numpy directly
numpy_array0 = np.array(zarr_array0)
print(f"Array type: {type(numpy_array0)}")
```


