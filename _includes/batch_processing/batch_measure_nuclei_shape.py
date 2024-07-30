# %% 
# Batch analysis of 2D nuclei shape measurements

# %%
# Import python modules
from OpenIJTIFF import open_ij_tiff, save_ij_tiff
from skimage.measure import label, regionprops_table
from skimage.filters import threshold_otsu
import pandas as pd
import pathlib
from pathlib import Path


# %%
# Create a function that analyses one image
# Below, this function will be called several times, for all images
def analyse(image_filepath, output_folder):

    # This prints which image is currently analysed
    print("Analyzing:", image_filepath)

    image, axes, scales, units = open_ij_tiff(image_filepath)

    # Binarize the image using auto-thresholding
    threshold = threshold_otsu(image)
    print("Threshold:", threshold)
    binary_image = image > threshold

    # Perform connected components analysis (i.e create labels)
    # Note that label returns 32 bit data which save_ij_tif below can't handle.
    # We can safely convert to 16 bit as we know that we don't have too many objects
    label_image = label(binary_image).astype('uint16')

    # Measure calibrated (scaled) nuclei shapes
    df = pd.DataFrame(regionprops_table(
        label_image,
        properties={'label', 'area'},
        spacing=scales))

    # Round all measurements to 2 decimal places.
    # This increases the readability a lot,
    # but depending on your scientific question,
    # you may not want to round that much!
    df = df.round(2)

    # Save the results to disk

    # Convert the image_filepath String to a Path,
    # which is more convenient to create the output files
    image_filepath = pathlib.Path(image_filepath)

    # Save the labels
    label_image_filepath = output_folder / f"{image_filepath.stem}_labels.tif"
    save_ij_tiff(label_image_filepath, label_image, axes, scales, units)

    # Save the measurements table
    # to a tab delimited text file (sep='\t')
    # without row numbers (index=False)
    table_path = output_folder / f"{image_filepath.stem}_measurements.csv"
    df.to_csv(table_path, sep='\t', index=False)

    return label_image_filepath
    

# %%
# Assign an output folder 
# Note: This uses your current working directory; you may want to change this to another folder on your computer
output_dir = Path.cwd()


# %%
# Create a list of the paths to all data
image_paths = [output_dir / "xy_8bit__mitocheck_incenp_t1.tif",
               output_dir / "xy_8bit__mitocheck_incenp_t70.tif"]
# Create an empty list for the result label images
label_image_paths = []


# %%
# The loop which performs the analysis
for image_path in image_paths:

    # Computes the analysis and returns the path of the resulting label image
    label_image_path = analyse(image_path, output_dir)

    # Append the label image path to the list initialized before the loop
    label_image_paths.append(label_image_path)


# %%
# Create a table to view the results in MoBIE
df = pd.DataFrame(data={'image': image_paths, 'labels': label_image_paths})
mobie_table_path = output_dir + Path('mobie_table.csv')
df.to_csv(mobie_table_path, sep='\t', index=False)
