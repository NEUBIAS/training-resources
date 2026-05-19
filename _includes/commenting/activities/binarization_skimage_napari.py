import matplotlib.pyplot as plt
from OpenIJTIFF import open_ij_tiff

# load the image from file
image_file = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif"
image, _, _, _ = open_ij_tiff(image_file)

# binarize the image, so that all values larger than the threshold are foreground
threshold_value = 60
binarized = image > threshold_value

# display the original and the binarized image
fig, ax = plt.subplots(2)
ax[0].imshow(image)
ax[0].set_title("Image")
ax[1].imshow(binarized)
ax[1].set_title("Binarized")

# For associated course material in jupyter, go to https://nbviewer.jupyter.org/github/embl-bio-it/image-analysis-with-python/blob/carpentry/image-analysis-session/image-binarization.ipynb#Image-Binarization
# You can also spin up an interactive binder session: https://gke.mybinder.org/v2/gh/embl-bio-it/image-analysis-with-python/carpentry?filepath=image-analysis-session/image-binarization.ipynb

# %%
# Close the viewer (CI test requires this)
plt.close('all')