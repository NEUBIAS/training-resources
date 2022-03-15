run("Close All");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nup_nuclei/xy_8bit_binary__nuclei_noisy.tif");
run("Morphological Filters", "operation=Opening element=Square radius=1");
run("Morphological Filters", "operation=Closing element=Square radius=16");
run("Connected Components Labeling", "connectivity=4 type=[8 bits]");
run("glasbey_on_dark");