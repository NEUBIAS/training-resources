**Import the relevant tools:**

```python
import zarr, os
import numcodecs
from ome_zarr import writer, scale
from ome_zarr.io import parse_url
from skimage.data import astronaut
```

**Create fake data:**

```python
data = astronaut().swapaxes(0, 2).swapaxes(1, 2)
```

**Create a zarr store to write:**

For the sake of simplicity, here we demonstrate how to write to a local store.
It is also possible to write to a remote location by simply specifying a remote 
url as input to the `parse_url` function.

```python
# Specify the path where you want to write
# output_path = f"{os.path.expanduser('~')}/image_data_formats/day2/astronaut.zarr"
output_path = "/path/to/astronaut.zarr"
# Parse the url as a zarr store. Note that "mode = 'w'" enables writing to this store.
store = parse_url(output_path, mode = 'w').store 
root = zarr.open_group(store)
```

**Specify a scaler:**

In order to create an image pyramid, one has to instantiate a scaler. 
This scaler requires the parameters: scale factor, number of resolution
layers and downscaling method.
```python
scaler = scale.Scaler(downscale=2, # Downscaling factor for x and y axes
                      max_layer=4, # Number of downscalings = 5
                      method = 'nearest' # downscaling method
                      )
```

**Specify the axis identities and the corresponding units:**

This dictionary will impose the axis order and the units corresponding to 
each axis.

```python
axes = [
    dict(name = 'c', type = 'channel'),
    dict(name = 'y', type = 'space', unit = 'micrometer'),
    dict(name = 'x', type = 'space', unit = 'micrometer'),
]
```

**Specify the voxel sizes for each resolution level:**

This is a list of list, where the length of the outer list must match 
the number of resolution levels. The inner lists contain dictionaries 
for different types of coordinate transforms. Each inner list must 
contain a scaling transform, a dictionary that takes `scale` as key 
and an iterable of voxel sizes as value.
 
```python
coordinate_transforms = [
    [{'scale': [1, 0.2, 0.2], 'type': 'scale'}],
    [{'scale': [1, 0.4, 0.4], 'type': 'scale'}],
    [{'scale': [1, 0.8, 0.8], 'type': 'scale'}],
    [{'scale': [1, 1.6, 1.6], 'type': 'scale'}],
    [{'scale': [1, 3.2, 3.2], 'type': 'scale'}]
]
```

**Specify zarr storage options**

The most important zarr storage options are the `chunks` and the `compression` 
parameters. The `chunks` parameter is simply a tuple of integers corresponding 
to each axis. The `compression` parameter requires compressor object from 
the `Numcodecs` package, which is a dependency of `zarr-python`.

```python
storage_options=dict(
                    chunks=(1, 64, 64),  # Output chunk shape
                    compression = numcodecs.Zlib(), # Compressor to be used, defaults to numcodecs.Blosc()
                    overwrite = True # Overwrite the output path
                )
```

**Save the array:**

Here we use the `ome_zarr.writer.write_image` function to save the array. 
This function takes the parameters specified above as input, downscales the 
array accordingly and writes the resulting pyramid to the specified zarr group. 

```python
writer.write_image(image = data, # In this case, a numpy array
                   group = root,
                   axes = axes, # Dimensionality order
                   scaler=scaler,
                   coordinate_transformations = coordinate_transforms,
                   storage_options = storage_options
                   )
```
