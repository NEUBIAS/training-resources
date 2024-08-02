# %%
# This script has two parts: the first part shows a script that opens two images and inspect their data type and values sequentially
# and the second part shows a function to do this task

# %%
# Import libraries and instantiate napari
import napari
import numpy as np
import matplotlib.pyplot as plt
from OpenIJTIFF import open_ij_tiff


# %%
# Part 1: write a script to open and inspect images
viewer = napari.Viewer()

# %%
# Open one image and view it
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_intensity_clipping_issue_a.tif')
viewer.add_image(image)

# %%
# Check the image's datatype
print(image.dtype)

# %%
# Check minimum and maximum pixel values
print("Min:", image.min()) # check minimum pixel value
print("Max:", image.max()) # check maximum pixel value



# %%
# Open second image and view it
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif')
viewer.add_image(image)


# %%
# Check the image's datatype
print(image.dtype)

# %%

# Check minimum and maximum pixel values
print("Min:", image.min()) # check minimum pixel value
print("Max:", image.max()) # check maximum pixel value

# %%
# Part 2: Write a function to perform above tasks
# NOTE: Please manually close any opened Napari Viewer Windows
viewer = napari.Viewer()

# %%
# Define a function to read and inspect image
def open_inspect_image(image_path):
    image, *_ = open_ij_tiff(image_path)
    print(image.dtype)
    print("Min:", image.min())
    print("Max:", image.max())
    return image

image1 = open_inspect_image('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_intensity_clipping_issue_a.tif')
image2 = open_inspect_image('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif')

# %%
# Display images
viewer.add_image(image1)
viewer.add_image(image2)
