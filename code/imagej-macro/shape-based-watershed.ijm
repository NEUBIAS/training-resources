#@File binary

// open image
run("Close All");
open(binary);
rename("binary");

// compute distance map
run("Chamfer Distance Map", "distances=[Chessknight (5,7,11)] output=[32 bits] normalize");

// invert
run("Invert");

// smooth
run("Gaussian Blur...", "sigma=10");
rename("inverted_distances");

// watershed
run("Classic Watershed", "input=inverted_distances mask=binary use min=0 max=255");
rename("split_objects");
