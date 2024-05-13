# %% 
# Create a cytoplasmic ring of a nuclei label mask

# %%
from OpenIJTIFF import open_ij_tiff
import napari
from skimage.morphology import square, disk
from skimage.morphology import dilation
from skimage.segmentation import expand_labels

# Create a napari_viewer and visualize image and labels.
viewer = napari.viewer.Viewer()

# %%
# open the label mask image
labels, *_ = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/watershed/xy_8bit_labels__nuclei.tif")
viewer.add_labels(labels)

# %%
# dilate the label image and inspect the result in napari
# observe that the nuclei with the larger label index grow into ones with smaller label indices
# the reason for this is that the implementation of the dilation is a local maximum filter
# this is not a useful result for creating cytoplasmic rings
dilated_labels = dilation(labels, disk(10))
viewer.add_labels(dilated_labels)

# %%
# now dilate the label image with the special "expand_labels" command 
# observe that now the nuclei do not grow into each other
expanded_labels = expand_labels(labels, 10)
viewer.add_labels(expanded_labels)

# %%
# create a cytoplasmic ring by subtracting two differently dilated 
# nuclei label masks from each other
# note that here we subtract slightly dilated nuclei to leave some gap 
# between the nucleus and the cytoplasmic ring
ring_labels = expand_labels(labels, 10) - expand_labels(labels, 2) 
viewer.add_labels(ring_labels)

# %%
# prevent napari from quitting when exectuing from a scripting environment
napari.run()

