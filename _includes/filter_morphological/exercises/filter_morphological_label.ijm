run("Close All");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nup_nuclei/xy_8bit_labels__nuclei.tif");
run("Morphological Filters", "operation=[Internal Gradient] element=Square radius=3");
rename("rim");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nup_nuclei.tif");
run("Duplicate...", "title=Ch1 duplicate channels=1");
run("Intensity Measurements 2D/3D", "input=Ch1 labels=rim mean stddev max min median  numberofvoxels");

