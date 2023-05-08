# %%
# Import modules
import napari
from OpenIJTIFF import open_ij_tiff
from skimage.measure import label, regionprops_table
import pandas as pd

# %%
# Instantiate the napari viewer
napari_viewer = napari.Viewer()

# %%
# Read and inspect the image:
fpath = 'https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t1.tif'
image_t1, axes_t1, voxel_size_input_t1, units_t1 = open_ij_tiff(fpath)

napari_viewer.add_image(image_t1, name='frame 1')


# %%
def nuclei_quantification(image, viewer, thr):
    print(f"Threshold: {thr}")
    # Binarize the image:
    image = image > thr
    viewer.add_labels(image, name='binary')
    # Find labels:
    img_labels = label(image)
    viewer.add_labels(img_labels, name='labels')
    # Obtain cell properties:
    properties = regionprops_table(
        img_labels,
        properties = {'label', 'area'}
    )
    # Print areas for each cell:
    areas = pd.DataFrame(properties)
    print(areas)

# %%
# Run workflow on each image:
threshold = 25
nuclei_quantification(image_t1, napari_viewer, threshold)

# Now try running the workflow using the second image!
