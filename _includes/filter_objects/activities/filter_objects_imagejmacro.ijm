run("Close All")

// File > Open
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__noisy_nuclei.tif")


//  Plugins › MorphoLibJ › Label Images › Remove Border Labels
run("Remove Border Labels", "left right top bottom");

// Plugins › MorphoLibJ › Analyze › Analyze Regions
run("Analyze Regions", "area");

// Plugins › MorphoLibJ › Label Images › Label Size Filtering
run("Label Size Filtering", "operation=Lower_Than size=100");
