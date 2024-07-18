# %% 
# Batch analysis of 2D nuclei shape measurements

# %%
# Import python modules
from OpenIJTIFF import open_ij_tiff
from skimage.measure import label, regionprops_table
from skimage.filters import threshold_otsu
from skimage.io import imsave
import pandas as pd
import pathlib
from pathlib import Path

# %%
# Create a function that analyses one image
# Below, this function will be called several times, for all images
def analyse(image_path, output_folder):
    image, axes, scales, units = open_ij_tiff(image_path)

    # Binarize the image using auto-thresholding
    threshold = threshold_otsu(image)
    print("Threshold:", threshold)
    binary_image = image > threshold
    
    # Perform connected components analysis (i.e create labels)
    label_image = label(binary_image)
   
    # Measure calibrated (scaled) nuclei shapes
    df = pd.DataFrame( regionprops_table(
        label_image,
        properties = {'label', 'area'},
        spacing = scales ) )
    
    # Round all measurements to 2 decimal places.
    # This increases the readability a lot,
    # but depending on your scientific question,
    # you may not want to round that much!
    df = df.round(2)

    # Save the results to disk

    # Convert the image_path String to a Path,
    # which is more convenient to create the output files
    image_path = pathlib.Path(image_path)

    # Save the labels
    label_image_path = output_folder / f"{image_path.stem}_labels.tif" 
    imsave(label_image_path, label_image)

    # Save the measurements table
    # to a tab delimited text file (sep='\t')
    # without row numbers (index=False)
    table_path = output_folder / f"{image_path.stem}_measurements.csv"
    df.to_csv(table_path, sep='\t', index=False)
    

# %%
# Assign an output folder 
# Note: This uses your current working directory; you may want to change this to another folder on your computer
output_dir = Path.cwd()

# %%
# Create a list of the paths to all data
image_paths = ["https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t1.tif", 
               "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t70.tif"]

for image_path in image_paths:
    print("Analyzing:", image_path)
    analyse(image_path, output_dir)
