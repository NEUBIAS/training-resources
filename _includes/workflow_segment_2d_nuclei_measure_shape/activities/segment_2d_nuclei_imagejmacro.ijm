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
	open(filePath);
	rename(name);
	setMinAndMax(0, 100);
	run("Duplicate...", "title=" + name + "_binary" );
	setThreshold(25, 255);
	run("Convert to Mask");
	run("Connected Components Labeling", "connectivity=4 type=[8 bits]");
	run("glasbey_on_dark");
	run("Analyze Regions", "area");
}
