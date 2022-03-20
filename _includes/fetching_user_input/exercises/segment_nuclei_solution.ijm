/**
 * 2D nuclei segmentation, including
 *  - image denoising by a mean filter
 *  - removal of small and boundary objects
 *  
 * Requirements:
 *   - Update site: IJPB-Plugins (MorpholibJ)
 * 
 */

//#@ File (label="Input image") filePath
//#@ String (label="Treatment") treatment
//#@ Integer (label="Median filter radius", value=5) medianFilterRadius
//#@ Integer (label="Minimum object size", value=50) minObjectSize
//#@ Integer (label="Treshold", value=25) threshold

// Parameters
treatment = "ctrl"; 
filePath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_small.tif"
medianFilterRadius = 3;
threshold = 25;
minObjectSizeminObjectSize = 100;

run("Close All");
run("Options...", "iterations=1 count=1 black do=Nothing");
open(filePath);
rename(treatment);
run("Duplicate...", "title="+treatment+"_denoise" );
run("Mean...", "radius="+medianFilterRadius);
run("Duplicate...", "title="+treatment+"_binary" );
setThreshold(threshold, 255); // Note: Be careful with the upper threshold!!
run("Convert to Mask");
run("Connected Components Labeling", "connectivity=4 type=[8 bits]");
run("glasbey_on_dark");
run("Label Size Opening", "min="+minObjectSize);
run("Remove Border Labels", "left right top bottom");
run("Analyze Regions", "area");
run("Tile");

