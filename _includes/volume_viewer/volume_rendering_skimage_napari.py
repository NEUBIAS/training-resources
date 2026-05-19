###
# To create an animation of the volume the napari-animation plugin is needed.
# pip install napari-animation
###

import numpy as np
from skimage.io import imread
import napari

# Read the image
# image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzt_8bit__starfish_chromosomes.tif')
# image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit__em_synapses_and_labels.tif')
image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__mri_full_head.tif')
# image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__organoid_nuclei.tif')
# image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__fib_sem_crop.tif')
# image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated_labels__platy_tissues.tif')

# Check image type and values
print(image.dtype)
print(np.min(image), np.max(image))
print(image.shape)

# Instantiate the napari viewer
viewer = napari.Viewer()

# View the intensity image as grayscale
viewer.add_image(image, name='image', colormap='gray')
# Napari GUI: choose a colormap according to the data type

# Napari GUI: change viewer from 2D to 3D, zoom in and out and rotate the volume
# Note: these values are optimized for xyz_8bit_calibrated__mri_full_head.tif
viewer.dims.ndisplay = 3
viewer.camera.zoom = 2
viewer.camera.angles = (0, -60, 90)

# Napari GUI: use rendering (and attenuation) modes
# Parameters can be changed for reproducibility
viewer.layers['image'].rendering = 'attenuated_mip'
viewer.layers['image'].attenuation = 1.

# Take a screenshot of the scene created
from napari.utils import nbscreenshot
nbscreenshot(viewer)

# Acquire the frame as numpy array and add it to the napari GUI
screenshot = viewer.screenshot()
viewer.add_image(screenshot, name='screenshot')
viewer.dims.ndisplay = 2

# Napari GUI: realize this is a 2D RGBA image and can be saved as a PNG for presentations
print(screenshot.dtype)
print(np.min(screenshot), np.max(screenshot))
print(screenshot.shape)

# Napari GUI: use napari-animation (https://github.com/napari/napari-animation) to create an animation of the volume

# %% 
# Close the viewer (CI test requires this)
viewer.close()