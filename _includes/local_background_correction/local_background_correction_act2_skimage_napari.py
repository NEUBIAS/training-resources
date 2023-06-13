# %% [markdown]
# ### Background subtraction using a maximum intensity projection
# Activity is part of the teaching module [Local background correction](https://neubias.github.io/training-resources/local_background_correction/index.html#bgmaxima)

# %%
import numpy as np
# Read the intensity image
from OpenIJTIFF import open_ij_tiff
image, axes, scales, units = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyt_8bit_polyp.tif')

# Inspect image data type and values
print('image type:', image.dtype,'\n',
      'image shape:', image.shape,'\n',
      'intensity min:',   np.min(image),'\n',
      'intensity max:',   np.max(image),'\n'
      'axis order:', axes
      )

# %%
# Instantiate the napari viewer
import napari
viewer = napari.Viewer()
viewer.add_image(image, name='original image')

# %%
# Remember the axis order 0=t, 1=x, 2=y
# Maximum projection along t-axis
max_t_image = np.max(image, axis = 0)
viewer.add_image(max_t_image, name = 'background')

# %%
# Cast to signed int16 to include also negative values
foreground = image.astype('int16') - max_t_image.astype('int16')
viewer.add_image(foreground, name = 'foreground')

