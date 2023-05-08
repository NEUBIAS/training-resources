### Median Filtering #################################################
import numpy as np
# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# Read the intensity image
from OpenIJTIFF import open_ij_tiff
image1, axes1, scales1, units1 = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__squares_different_size.tif')
# Inspect image data type and values
print('image type:', image1.dtype,'\n',
      'image shape:', image1.shape,'\n',
      'intensity min:',   np.min(image1),'\n',
      'intensity max:',   np.max(image1),'\n'
      )
# View the intensity image
viewer.add_image(image1, name='original image1')

# First method using the median filter
from skimage import filters
from skimage.morphology import disk

# Local median filtering with radius 1
Median_1 = filters.median(image1, disk(1))
viewer.add_image(Median_1, name='Median1')

# Local median filtering with radius 2
Median_2 = filters.median(image1, disk(2))
viewer.add_image(Median_2, name='Median2')

# Local median filtering with radius 5
Median_3 = filters.median(image1, disk(5))
viewer.add_image(Median_3, name='Median3')

