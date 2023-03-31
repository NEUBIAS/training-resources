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
threshold_otsu = image > threshold_otsu(image)

viewer.add_labels(thresholded, name='otsu', num_colors=1, color={0: 'green'})
# Explore the results in the napari viewer. For 3D data one can change the order 
# of visible axes (bottom left in napari viewer window). If not satisfied by the
# results, we can explore other threshold algorithms:
from skimage.filters import threshold_li
thresholded_li = image > threshold_li(image)

viewer.add_labels(thresholded_li, name='li', num_colors=1, color={0: 'orange'})