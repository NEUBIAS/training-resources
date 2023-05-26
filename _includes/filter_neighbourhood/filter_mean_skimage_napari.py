# %%
# Instantiate the napari viewer
import napari
from OpenIJTIFF import open_ij_tiff
viewer = napari.Viewer()

# %%
# Read the intensity image
image, axes, scales, units = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_very_noisy.tif')

# %%
# View the intensity image
viewer.add_image(image)

# %%
# Appreciate that one cannot segment the nuclei by a simple intensity threshold
binary_image = image > 40
viewer.add_image(binary_image)

# %% 
# Define a circular structural element with a radius of 1 pixel
from skimage.morphology import disk
radius = 1
disk_radius1 = disk(radius)
print(disk_radius1)

# %%
# Apply a mean filter with the structural element
from skimage.filters.rank import mean
mean_disk_radius1 = mean(image, disk_radius1)

# Add the filtered image to napari
# Napari: Zoom in to appreciate that the filtered image 
# contains the local mean values of the raw image
viewer.add_image(mean_disk_radius1)

# %%
# One still cannot readily segment the nuclei
# (rerun the below code with different thresholds)
binary_mean_disk_radius1 = mean_disk_radius1 > 35
viewer.add_image(binary_mean_disk_radius1)

# %% 
# Apply mean filter with a disk of radius 3
mean_disk_radius3 = mean(image, disk(3))
viewer.add_image(mean_disk_radius3)

# %%
# Now the nuclei can be segmented
binary_mean_disk_radius3 = mean_disk_radius3 > 32
viewer.add_image(binary_mean_disk_radius3)