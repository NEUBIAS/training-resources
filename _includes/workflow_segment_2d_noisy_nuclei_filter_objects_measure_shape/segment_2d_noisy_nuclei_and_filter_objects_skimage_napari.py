# %%
# Import modules
import napari
from OpenIJTIFF import open_ij_tiff
from skimage.filters.rank import mean
from skimage.morphology import disk, remove_small_objects, remove_small_holes
from skimage.measure import label, regionprops_table
from skimage.segmentation import clear_border
import pandas as pd

# %%
# Instantiate the napari viewer
napari_viewer = napari.Viewer()

# %%
# Read and inspect the image:
fpath = 'https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_small.tif'
image1, axes_image1, scales_image1, units_t1 = open_ij_tiff(fpath)

napari_viewer.add_image(image1, name='frame 1')

# %%
def noisy_nuclei_quantification(
    image, 
    viewer, 
    radius=3,
    thr=25,
    min_size_holes=100,
    connectivity=2,
    min_size_regions=100,
):
    # Applying local mean filter
    disk_radius = disk(radius)
    image_denoise = mean(image, disk_radius)
    viewer.add_image(image_denoise, name='denoise')
    # Binarize the image:
    image_binary = image_denoise > thr
    viewer.add_labels(image_binary, name='binary')
    # Remove small holes
    img_binary_fill = remove_small_holes(image_binary, area_threshold=min_size_holes)
    viewer.add_labels(img_binary_fill, name='filled')
    # Find labels:
    img_labels = label(img_binary_fill, connectivity=connectivity)
    viewer.add_labels(img_labels, name='labels')
    # Remove small regions and fill small holes
    img_labels_filt = remove_small_objects(img_labels, min_size=min_size_regions)
    viewer.add_labels(img_labels_filt, name='labels_filt')
    # Remove regions touching the borders
    img_labels_filt_no_borders = clear_border(img_labels_filt)
    viewer.add_labels(img_labels_filt_no_borders, name='labels_filt_no_borders')
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
noisy_nuclei_quantification(image1, napari_viewer)

# %%
