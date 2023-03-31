# Import modules
import napari
from skimage.io import imread
from skimage.measure import label, regionprops

# Instantiate the napari viewer
viewer = napari.Viewer()

# Read and inspect the image:
image_t1 = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t1.tif')
viewer.add_image(image_t1, name='frame 1')

threshold = 25

def nuclei_quantification(image):
    # Binarize the image:
    image = image > threshold
    viewer.add_labels(image, name='binary')
    # Find labels:
    img_labels = label(image)
    viewer.add_labels(img_labels, name='labels')
    # Obtain cell properties:
    properties = regionprops(img_labels)
    # Print areas for each cell:
    for cellid, region in enumerate(r):
        print(f"Cell nr. {cellid}, area: {region.area}")
    
# Run workflow on each image:
nuclei_quantification(image_t1)

# Now try running the workflow using the second image!
