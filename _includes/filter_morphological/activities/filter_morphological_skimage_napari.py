#######################################################
## To follow along you need to complete the tool
## installation activity for skimage napari.
#######################################################

#%%
# Import python packages.
from OpenIJTIFF import open_ij_tiff
import numpy as np
from napari.viewer import Viewer
from skimage.morphology import square, disk
from skimage.morphology import erosion, dilation
from skimage.morphology import opening, closing

#%% 
# download and read tif file
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__two_spots_different_size.tif"
image_2spots, _, _, _ = open_ij_tiff(fpath)

# Create a napari_viewer and visualize image and labels.
napari_viewer = Viewer()
napari_viewer.add_image(image_2spots, name='image')

#%%
# Perform erosion and dilation with default structuring element (cross, connectivity=1).
eroded = erosion(image_2spots)
dilated = dilation(image_2spots)

#%%
# Now try with connectivity 2 (square).
square3 = square(3)
print(square)
eroded_square3 = erosion(image_2spots, square3)
dilated_square3 = dilation(image_2spots, square3)

#%%
# add images to the viewer and inspect the results
napari_viewer.add_image(eroded, name='eroded1')
napari_viewer.add_image(dilated, name='dilated1')
napari_viewer.add_image(eroded_square3, name='eroded3')
napari_viewer.add_image(dilated_square3, name='dilated3')

# Now try with bigger square (e.g. square(5))
# or a different structuring element (e.g. disk(1))
# Also refer to:
# https://scikit-image.org/docs/stable/api/skimage.morphology.html

#%%
# Explore opening and closing combining erosion and dilation.
# Verify that they give the same results.
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__for_open_and_close.tif"
image_structures, _, _, _ = open_ij_tiff(fpath)

#%%
# Opening: remove thin structures, smoothen objects.
opening_manual = dilation(erosion(image_structures, square(3)), square(3))
opening_1step = opening(image_structures, square(3))
print((opening_manual==opening_1step).all())

#%%
# Closing: fill holes, connect gaps.
closing_manual = erosion(dilation(image_structures, square(3)), square(3))
closing_1step = closing(image_structures, square(3))
print((closing_manual==closing_1step).all())

#%%
# Try using the default structuring element (disk(1)).
# Explain what has changed and why.
closing_disk = closing(image_structures, disk(1))

#%%
# Create a napari_viewer and visualize images.
napari_viewer = Viewer()
napari_viewer.add_image(image_structures, name='image')
napari_viewer.add_image(opening_1step, name='opening')
napari_viewer.add_image(closing_1step, name='closing')
napari_viewer.add_image(closing_disk, name='closing_disk')

#%%
# Explore internal gradient.
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__h2b.tif"
image, _, _, _ = open_ij_tiff(fpath)

# Internal gradient is the difference between the image and the eroded version of it.
eroded = erosion(image)
internal_gradient = image-eroded

#%%
# Create a napari_viewer and visualize images.
napari_viewer = Viewer()
napari_viewer.add_image(image, name='image')
napari_viewer.add_image(internal_gradient, name='internal_gradient')

# The internal gradient represent the edge of the object.
# Discuss when and how this can be useful.
