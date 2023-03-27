import numpy as np
from skimage.io import imread
import napari

# Read the image
image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__nuclei_autothresh.tif')

# Inspect image data type and values
print(f'Type: {image.dtype} \nShape: {image.shape} \nMin: {np.min(image)} \nMax: {np.max(image)}')

# Instantiate the napari viewer
viewer = napari.Viewer()

# Visualize images using matplotlib
viewer.add_image(image, name='image')

# Obtain threshold value using Otsu's algorithm
from skimage.filters import threshold_otsu
thr_otsu = threshold_otsu(image)
thresholded = image > thr_otsu

viewer.add_labels(thresholded, name='otsu_thr')
