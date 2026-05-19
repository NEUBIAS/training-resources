# %% [markdown]
# ### Opening and closing of binary
#
# Part of teaching module [Morphological filtering](https://neubias.github.io/training-resources/filter_morphological/index.html#openclose)

# %%
# Import python packages.
from OpenIJTIFF import open_ij_tiff
from napari.viewer import Viewer
from skimage.morphology import footprint_rectangle as rectangle
from skimage.morphology import disk
from skimage.morphology import erosion, dilation
from skimage.morphology import opening, closing

# %%
# Explore opening and closing combining erosion and dilation.
# Verify that they give the same results.
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__for_open_and_close.tif"
image, _, _, _ = open_ij_tiff(fpath)
viewer = Viewer()
viewer.add_image(image)

# %% [markdown]
# Morphological *opening* is the *dilation* of an *eroded* image using the same structuring element

# %%
# Opening operation
eroded = erosion(image, footprint = rectangle((3,3)))
opened = dilation(eroded, footprint = rectangle((3,3)))
viewer.add_labels(eroded)
viewer.add_labels(opened)

# %% [markdown]
# Appreciate how the *opening* operation removed thin structures (< structuring element size) and smoothen objects

# %%
# Opening operations are so common that often they have their own command
opened_1step = opening(image, rectangle((3,3)))
print((opened==opened_1step).all())


# %% [markdown]
# Morphological *closing* is the *erosion* of a *dilated* image using the same structuring element

# %%
# Closing: fill holes, connect gaps.
dilated = dilation(image, footprint = rectangle((3,3)))
closed = erosion(dilated, rectangle((3,3)))
viewer.add_labels(dilated)
viewer.add_labels(closed)

# %%
# Closing operations are so common that often they have their own command
closed_1step = closing(image, rectangle((3,3)))
print((closed==closed_1step).all())

# %% [markdown]
# Appreciate how the *closing* operation filled holes and connected gaps (< structuring element size)

# %% [markdown]
# **Learning opportunity**\
# Try using the default structuring element (`disk(1)`)\
# Explain what has changed and why. Hint: Look at the dilated image prior to erosion

# %% 
# Close the viewer (CI test requires this)
viewer.close()