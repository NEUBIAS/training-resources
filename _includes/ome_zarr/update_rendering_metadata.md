**Import the necessary modules**

```python
import zarr, os
from ome_zarr.io import parse_url
import matplotlib.colors as mcolors
```

**At this stage inspect the image using the OME-Zarr validator:**

```bash
ome_zarr view ~/ome_zarr_course/data/zarr/outputs/astronaut.zarr
```

**Define a utility function to get the hex color code by simple color names**

```python
def get_color_code(color_name):
    try:
        color_code = mcolors.CSS4_COLORS[color_name.lower()]
        return color_code
    except KeyError:
        return f"Color '{color_name}' not found."
```

**Now add rendering metadata**

```python
path = f"{os.path.expanduser('~')}/ome_zarr_course/data/zarr/outputs/astronaut.zarr"
store = parse_url(path, mode = 'w').store # Create a zarr store to save the data. Note that this can also be an s3 object store.
root = zarr.open_group(store=store)
root.attrs["omero"] = {
    "channels": [
        {
            "color": get_color_code('cyan'),
            "window": {"start": 0, "end": 255, "min": 0, "max": 255},
            "label": "ch0",
            "active": True,
        },
        {
            "color": get_color_code('magenta'),
            "window": {"start": 0, "end": 255, "min": 0, "max": 255},
            "label": "ch1",
            "active": True,
        },
        {
            "color": get_color_code('yellow'),
            "window": {"start": 0, "end": 255, "min": 0, "max": 255},
            "label": "ch2",
            "active": True,
        },
    ]
}
```

It is important to know here that not all OME-Zarr readers recognize each of these settings. \
Apply the validator again to the data to see the changes:
```bash
ome_zarr view ~/ome_zarr_course/data/zarr/outputs/astronaut.zarr
```
As the data looks valid, now visualize using different viewers to see if the rendering is working.