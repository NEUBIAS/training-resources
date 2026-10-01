# %%
# Using different Lookup Tables (LUTs) in napari
import napari
from bioio import BioImage


# %%
# Read an image and its metadata
# from OpenIJTIFF import open_ij_tiff
# image, *_ = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_high_dynamic_range.tif")

img_obj = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_high_dynamic_range.tif')
img = img_obj.data    # or img_data = img_obj.data

print(f'Axes order = {img_obj.dims.order}')

# %%
# Instantiate the napari viewer
viewer = napari.Viewer()

# %%
# Add the image
viewer.add_image(img)

# %%
# Napari:
# Activity: Adjust the contrast limits and colormap to see dim and bright regions in the same image
# Right click on "contrast limits" and adjust to see the brightest regions & dim nuclei
#
# Appreciate the such a multi-color LUT can be useful to see dim and bright regions

# %%
# Programatically show the image several times with different LUT settings
viewer.layers.clear() # remove all layers
# viewer.add_image(image, name="image_turbo", colormap="turbo", contrast_limits=[0,255])

## Display full bit-depth range
viewer.add_image(img, name="image_gray_1", colormap="gray", contrast_limits=[0,255])
viewer.layers["image_gray_1"].bounding_box.visible = True
viewer.layers["image_gray_1"].colorbar.visible = True

## Display bright objects
viewer.add_image(img, name="image_gray_2", colormap="gray", contrast_limits=[130,255])
viewer.layers["image_gray_2"].bounding_box.visible = True
viewer.layers["image_gray_2"].colorbar.visible = True

## Display dim objects
viewer.add_image(img, name="image_gray_3", colormap="gray", contrast_limits=[0,50])
viewer.layers["image_gray_3"].bounding_box.visible = True
viewer.layers["image_gray_3"].colorbar.visible = True

## Display extreme values using a multi-color LUT
viewer.add_image(img, name="image_hilo", colormap="HiLo")
viewer.layers["image_hilo"].bounding_box.visible = True
viewer.layers["image_hilo"].colorbar.visible = True

## Enable grid mode to see the images side by side
viewer.grid.enabled = True # turn on the grid mode to see the images side by side

# %%
# Close the viewer (CI test requires this)
viewer.close()
