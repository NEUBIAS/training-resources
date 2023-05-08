import numpy as np
# Read the intensity image
from OpenIJTIFF import open_ij_tiff

image, axes, scales, units = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyt_8bit_polyp.tif')

# Inspect image data type and values
print('image type:', image.dtype,'\n',
      'image shape:', image.shape,'\n',
      'intensity min:',   np.min(image),'\n',
      'intensity max:',   np.max(image),'\n'
      )

# Instantiate the napari viewer
import napari
viewer = napari.Viewer()
viewer.add_image(image, name='original image')

# Remember the axis order 0=z, 1=x, 2=y
# Maximum projection along z-axis
max_z_image = np.max(image, axis=0)

foreground = image.astype('int16') - max_z_image.astype('int16')
viewer.add_image(foreground, name='foreground')

