/**
 * 2D nuclei segmentation, including
 *  - image denoising by a mean filter
 *  - removal of small and boundary objects
 *  
 * Requirements:
 *   - Update site: IJPB-Plugins (MorpholibJ)
 * 
 */

run("Close All");
run("Options...", "iterations=1 count=1 black do=Nothing");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_small.tif");
rename("ctrl");
run("Duplicate...", "title=ctrl_denoise" );
run("Mean...", "radius=3");
run("Duplicate...", "title=ctrl_binary" );
setThreshold(25, 255);
run("Convert to Mask");
run("Connected Components Labeling", "connectivity=4 type=[8 bits]");
run("glasbey_on_dark");
run("Label Size Opening", "min=100");
run("Remove Border Labels", "left right top bottom");
run("Analyze Regions", "area");
run("Tile");

