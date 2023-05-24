### Mean Filtering   #################################################
import numpy as np
# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# Read the intensity image
from OpenIJTIFF import open_ij_tiff
image2, axes2, scales2, units2 = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__squares_different_size.tif')
# Inspect image data type and values
print('image type:', image2.dtype,'\n',
      'image shape:', image2.shape,'\n',
      'intensity min:',   np.min(image2),'\n',
      'intensity max:',   np.max(image2),'\n'
      )
# View the intensity image
viewer.add_image(image2, name='original image2')

# First method using the median filter
from skimage.filters import rank
from skimage.morphology import disk

# Local mean filtering with radius 1
Mean_1 = rank.mean(image2, disk(1))
viewer.add_image(Mean_1, name='Mean1')

# Local mean filtering with radius 2
Mean_2 = rank.mean(image2, disk(2))
viewer.add_image(Mean_2, name='Mean2')

# Local mean filtering with radius 5
Mean_3 = rank.mean(image2, disk(5))
viewer.add_image(Mean_3, name='Mean3')
