/*
 * Requirements:
 * - MorpholibJ, Update site: IJPB-Plugins
 *
 **/
// Region selection by Distance gating
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__single_object.tif");
run("Invert");
run("Chamfer Distance Map", "distances=[Chessknight (5,7,11)] output=[16 bits] normalize");
run("Manual Threshold...", "min=100 max=120");
run("Convert to Mask");

