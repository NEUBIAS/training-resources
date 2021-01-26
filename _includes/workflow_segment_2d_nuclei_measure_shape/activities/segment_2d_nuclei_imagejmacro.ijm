/**
 * 2D Nuclei segmentation (simple workflow)
 * 
 * Requirements:
 *   - Update site: IJPB-Plugins (MorpholibJ)
 * 
 */

run("Close All");
run("Options...", "iterations=1 count=1 black do=Nothing");

analyseNuclei( "INCENP_T1", "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t1.tif" );
analyseNuclei( "INCENP_T70", "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t70.tif" );
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
	run("Duplicate...", "title=" + name + "_binary" );
	// Image › Adjust › Threshold...  [ Apply ]
	setThreshold(25, 255);
	run("Convert to Mask");
	// Plugins › MorphoLibJ › Binary Images › Connected Components Labeling
	run("Connected Components Labeling", "connectivity=4 type=[8 bits]");
	// Image › Lookup Tables › glasbey_on_dark
	run("glasbey_on_dark");
	// Plugins › MorphoLibJ › Analyze › Analyze Regions
	run("Analyze Regions", "area");
}
