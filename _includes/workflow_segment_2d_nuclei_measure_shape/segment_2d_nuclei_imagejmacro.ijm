/**
 * 2D Nuclei segmentation (simple workflow)
 * 
 * Requirements:
 *   - Update site: IJPB-Plugins (MorpholibJ)
 * 
 */

// Threshold parameter
threshold = 25;

// Code
run("Close All");
run("Options...", "iterations=1 count=1 black do=Nothing");

analyseNuclei( "INCENP_T1", "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t1.tif", threshold );
analyseNuclei( "INCENP_T70", "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t70.tif", threshold );

run("Tile");

function analyseNuclei( name, filePath, threshold )
{
	open(filePath);
	rename(name);
	setMinAndMax(0, 100);
	run("Duplicate...", "title=" + name + "_binary" );
	setThreshold(threshold, 65535);
	run("Convert to Mask");
	run("Connected Components Labeling", "connectivity=4 type=[8 bits]");
	run("glasbey_on_dark");
	run("Analyze Regions", "area");
}
