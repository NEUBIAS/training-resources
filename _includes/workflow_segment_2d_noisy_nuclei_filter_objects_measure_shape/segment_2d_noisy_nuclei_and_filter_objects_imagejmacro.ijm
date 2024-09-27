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

analyseNuclei( "Ctrl", "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_small.tif" );
analyseNuclei( "Treat", "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_large.tif" );
run("Tile");

function analyseNuclei( name, filePath )
{
	// File › Open...
	open(filePath);
	// Image › Rename...
	rename(name);
	// Image › Adjust › Brightness/Contrast...
	setMinAndMax(0, 100);
	// Image › Duplicate...
	run("Duplicate...", "title=" + name + "_denoise" );
	// Process › Filters › Mean...
	run("Mean...", "radius=3");
	// Image › Duplicate...
	run("Duplicate...", "title=" + name + "_binary" );
	// Image › Adjust › Threshold...  [ Apply ]
	setThreshold(25, 255);
	run("Convert to Mask");
	// Plugins › MorphoLibJ › Binary Images › Connected Components Labeling
	run("Connected Components Labeling", "connectivity=4 type=[8 bits]");
	// Image › Lookup Tables › glasbey_on_dark
	run("glasbey_on_dark");
	// Plugins › MorphoLibJ › Label Images › Label Size Opening
	run("Label Size Opening", "min=100");
	// Plugins › MorphoLibJ › Label Images › Remove Border Labels
	run("Remove Border Labels", "left right top bottom");
	// Plugins › MorphoLibJ › Analyze › Analyze Regions
	run("Analyze Regions", "area");
}
