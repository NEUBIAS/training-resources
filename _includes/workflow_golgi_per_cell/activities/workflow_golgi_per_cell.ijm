/**
 * ImageJ/Fiji Macro
 * 
 * Required update sites:
 *   - IJPB-Plugins (MorpholibJ)
 **/


// boilerplate
//
run("Close All");
run("Options...", "iterations=1 count=1 black");

// parameters
//
nucleusDilationPixels = 30;

// open image
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nuclei_golgi.tif");
rename("input");

// split channels
run("Split Channels");
selectWindow("C1-input");
rename("nuclei");
selectWindow("C2-input");
rename("golgi");

// segment nuclei 
selectWindow("nuclei");
run("Duplicate...", "nuclei-binary");
run("Median...", "radius=5");
run("Auto Threshold", "method=Huang white");
run("Fill Holes");
run("Connected Components Labeling", "connectivity=4 type=[16 bits]");
rename("nuclei-labels");
run("glasbey_on_dark");

// approximate cells by dilation of nuclei
run("Dilate Labels", "radius="+nucleusDilationPixels);
// run("Remove Border Labels", "left right top bottom");
rename("cells-labels");
run("glasbey_on_dark");

// segment golgi 
selectWindow("golgi");
run("Duplicate...", "golgi-binary");
run("Gaussian Blur...", "sigma=0.5");
run("Auto Threshold", "method=Huang white");
run("Connected Components Labeling", "connectivity=4 type=[16 bits]");
rename("golgi-labels");
run("glasbey_on_dark");

// measure golgi parent cell index
run("Intensity Measurements 2D/3D", "input=cells-labels labels=golgi-labels max min mode");
Table.rename("cells-labels-intensity-measurements", "golgi-parent-labels");

// create image where golgi objects are coloured as parent cells
// https://github.com/ijpb/MorphoLibJ/issues/26
// run("Assign Measure to Label");

// measure golgi shape features
selectWindow("golgi-labels");
run("Analyze Regions", "area perimeter circularity euler_number equivalent_ellipse ellipse_elong. convexity max._feret geodesic tortuosity max._inscribed_disc average_thickness geodesic_elong.");
Table.rename("golgi-labels-Morphometry", "golgi-shapes");


run("Tile");
