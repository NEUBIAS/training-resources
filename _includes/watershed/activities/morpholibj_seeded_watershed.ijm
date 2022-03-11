/*
 * Seeded watershed (with distance transform)  in Fiji
 * 
 * Requirements: 
 * - IJPB-Plugins update site
 */

run("Close All");
setOption("BlackBackground", true);

open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__noisy_touching_objects.tif");
rename("input");
run("Duplicate...", "title=invert");
run("Invert");
run("Enhance Contrast", "saturated=0.35");

// watershed
run("Classic Watershed", "input=invert mask=None use min=0 max=255");

// seeded watershed
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__touching_objects_markers.tif");
rename("seeds");
run("Marker-controlled Watershed", "input=invert marker=seeds mask=None compactness=0 binary calculate use");
