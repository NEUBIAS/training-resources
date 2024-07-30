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

    # Convert the image_filepath String to a Path,
    # which is more convenient to create the output files
    image_filepath = pathlib.Path(image_filepath)

    image, axes, scales, units = open_ij_tiff(image_filepath)

    # Binarize the image using auto-thresholding
    threshold = threshold_otsu(image)
    print("Threshold:", threshold)
    binary_image = image > threshold

    # Perform connected components analysis (i.e create labels)
    # Note that label returns 32 bit data which save_ij_tif below can't handle.
    # We can safely convert to 16 bit as we know that we don't have too many objects
    label_image = label(binary_image).astype('uint16')

    # Save the labels
    label_image_filepath = output_folder / f"{image_filepath.stem}_labels.tif"
    save_ij_tiff(label_image_filepath, label_image, axes, scales, units)

    # Measure calibrated (scaled) nuclei shapes
    df = pd.DataFrame(regionprops_table(
        label_image,
        properties={'label', 'area', 'centroid'},
        spacing=scales))

    # Round all measurements to 2 decimal places.
    # This increases the readability a lot,
    # but depending on your scientific question,
    # you may not want to round that much!
    df = df.round(2)

    # Add the image and label filepaths to the data-frame
    df['image'] = image_filepath
    df['labels'] = label_image_filepath

    # Return the data-frame
    return df
    

# %%
# Assign an output folder 
# Note: This uses your current working directory; you may want to change this to another folder on your computer
output_dir = Path.cwd()


# %%
# Create a list of the paths to all data
image_paths = [output_dir / "xy_8bit__mitocheck_incenp_t1.tif",
               output_dir / "xy_8bit__mitocheck_incenp_t70.tif"]
# Create an empty list for the measurement results
result_dfs = []


# %%
# The loop which performs the analysis
for image_path in image_paths:

    # Computes the analysis and returns a data-frame with the resulting measurements
    result_df = analyse(image_path, output_dir)

    # Append the label image path to the list initialized before the loop
    result_dfs.append(result_df)


# %%
# Concatenate the result data-frames to a single one which contains all results
final_df = pd.concat(result_dfs, ignore_index=True)
# Save the final results to disk
final_df.to_csv(output_dir / 'batch_processing_results.csv', sep='\t', index=False)

