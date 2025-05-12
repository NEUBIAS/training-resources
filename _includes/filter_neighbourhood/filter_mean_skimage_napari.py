# %% 
# Apply mean filters to an image to aid foreground background segmentation 

# %%
# Instantiate the napari viewer
import napari
from OpenIJTIFF import open_ij_tiff
viewer = napari.Viewer()

# %%
# Read the intensity image
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_very_noisy.tif')

# %%
# View the image 
# - Appreciate that it is quite noisy
# - Inspect the pixel values to find a threshold that separates the nuclei from the background
viewer.add_image(image)

# %%
# Binarise the image
# - Appreciate that one cannot segment the nuclei by a simple intensity threshold
binary_image = image > 40
viewer.add_image(binary_image)

# %% 
# Prepare filtering the image by defining a circular structural element with a radius of 1 pixel
from skimage.morphology import disk
disk_radius_1 = disk(1)
print(disk_radius_1)

# %%
# Apply a mean filter to the image with the above structural element
from skimage.filters.rank import mean
mean_image_1 = mean(image, disk_radius_1)

# Add the filtered image to napari
# Napari:
# - Zoom in and inspect the pixel values to check that the filtered image indeed contains the local mean values of the raw image
viewer.add_image(mean_image_1)

# %%
# Binarise the filtered image
# - Appreciate that one still cannot readily segment the nuclei
binary_image_1 = mean_image_1 > 35
viewer.add_image(binary_image_1)

# %% 
# Apply mean filter with a disk of radius 3
mean_image_3 = mean(image, disk(3))
viewer.add_image(mean_image_3)

# %%
# Now the nuclei can be segmented by a simple threshold :)
binary_image_3 = mean_image_3 > 32
viewer.add_image(binary_image_3)

# %% 
# Close the viewer (CI test requires this)
viewer.close()