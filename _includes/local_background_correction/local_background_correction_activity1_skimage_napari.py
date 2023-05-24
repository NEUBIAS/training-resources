import numpy as np

# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# Read the intensity image
from OpenIJTIFF import open_ij_tiff
image, axes, scales, units = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__some_spots_with_uneven_bg.tif')

# View the intensity image
viewer.add_image(image, name='original image')

# Inspect image data type and values
print('image type:', image.dtype,'\n',
      'image shape:', image.shape,'\n',
      'intensity min:',   np.min(image),'\n',
      'intensity max:',   np.max(image),'\n'
      )

######################################
# using the median filter from skimage
from skimage import filters
from skimage.morphology import disk

# Local median filtering with radius 15
background = filters.median(image, disk(15))
viewer.add_image(background, name='background')
foreground = image.astype('int16') - background.astype('int16')
viewer.add_image(foreground, name='foreground')


######################################
# Inspect the intensity image values in order to identify a threshold
# that segments cells
# napari GUI: hover with mouse, line profile

# Threshold the image
binary_image_cells = foreground > 8
# Overlay the binary image
viewer.add_image(binary_image_cells, name='segmented image')

