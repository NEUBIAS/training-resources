import napari
viewer = napari.Viewer()

# Read the intensity image
from skimage.io import imread
image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif')

# View the image
viewer.add_image(image)

# Check the image's datatype
print(image.dtype)

# Check the image's minimum and maximum intensity
import numpy as np
print(np.min(image),np.max(image))

# Repeat the above steps for the other images
# (Note that we do not need to import imread and numpy again)
image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_intensity_clipping_issue_a.tif')
viewer.add_image(image)
print(image.dtype)

