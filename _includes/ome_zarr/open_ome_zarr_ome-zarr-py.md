**Import the relevant tools:**

```python
import ome_zarr, zarr, pprint, os
from ome_zarr.reader import Reader
from ome_zarr.io import parse_url
```
**Read remote OME-Zarr:**
```python
# local_path = f"{os.path.expanduser('~')}/ome_zarr_course/data/zarr/6001240.zarr"
remote_path = f"https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0062A/6001240.zarr"
reader = Reader(parse_url(remote_path))
# Note here that 'parse_url' can parse both remote and local urls.
# No need for explicit use of s3fs.
```


Note that ome-zarr-py uses the term 'node' for different zarr groups \
and reads them in a flat list. 

**Print the node information per resolution level:**

```python 
nodes = list(reader())
for idx, node in enumerate(nodes):
    print(f"The node at the level {idx} is {node}")
```

**Get the data and metadata of the top-level node:**

```python
dataset = nodes[0].data
meta = nodes[0].metadata
```
**Check the 'data' instance to examine the array shape and the chunks for each resolution layer:**

```python
for idx, array in enumerate(dataset):
    print(f"The array {idx} is a {type(array)} and has shape {array.shape} and has chunks with shape {array.chunksize}")
```

**Print the axis types and units of the arrays using the metadata instance**
```python
print(f"Axis properties of the dataset:")
pprint.pprint(meta['axes'])
```
**Print the voxel sizes per resolution level (and any other voxel transforms that may exist)**
```python
for idx, transforms in enumerate(meta['coordinateTransformations']):
    print(f"\033[1mThe transform metadata for the level {idx}:\033[0m")
    print(f"{transforms}")
```

