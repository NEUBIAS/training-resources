from load_from_url import load_from_url
from napari.viewer import Viewer

### NOTE: xml/h5 currently not working!

# image_url = load_from_url('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_PLK1_control.tif')
# image_url = load_from_url('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_xyc__two_images.lif')
# image_url = load_from_url('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz__multiple_images.czi')
image_url = load_from_url('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzct_16bit__mitosis.ics')
### image_url = load_from_url('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzct_16bit__mitosis.xml')


# Visualize and explore available metadata
print(image_url.metadata)

# Explore some useful metadata
# Appreciate that accessing the metadata is not always straightforward
print(image_url.dims)
print(image_url.physical_pixel_sizes)
print(image_url.metadata.images[0].pixels.time_increment)

# Visualize the dataset in napari viewer
napari_viewer = Viewer()
napari_viewer.add_image(image_url.data, scale = image_url.physical_pixel_sizes)

# Resave the dataset as ome tif with pixel size
from aicsimageio.writers.ome_tiff_writer import OmeTiffWriter
import numpy as np
OmeTiffWriter.save(image_url.data.astype(np.uint16), 
                   "file.ome.tif", 
                   dim_order="TCZYX",
                   physical_pixel_sizes=image_url.physical_pixel_sizes)

# Resave dataset as gif
from aicsimageio.writers.timeseries_writer import TimeseriesWriter
OmeTiffWriter.save(image_url.data.astype(np.uint16), 
                   "file.gif", 
                   dim_order="TCZYX",
                   physical_pixel_sizes=image_url.physical_pixel_sizes)

# Reload ome tif
from aicsimageio import AICSImage
resaved = AICSImage('file.ome.tif')

# Appreciate that metadata has changed
print(resaved.metadata)
