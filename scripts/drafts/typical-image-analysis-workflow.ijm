#@File image

run("Close All");
open(image);
rename("raw");

// measure background (could be manual or, like here, automated)
List.setMeasurements();
background = List.get("Mode");

// create bg subtracted image
run("Duplicate...", "title=bg-corr");
run("32-bit");
run("Subtract...", "value=" + background);

// filter 
selectWindow("raw");
run("Duplicate...", "title=filtered");
run("Gaussian Blur...", "radius=4");

// threshold
run("Duplicate...", "title=binary");
setThreshold(72, 255);
run("Convert to Mask");

// remove border touching objects
run("Kill Borders");

// connected components labeling
run("Connected Components Labeling", "connectivity=4 type=[16 bits]");
rename("labels");

// measure
run("Region Morphometry");
run("Intensity Measurements 2D/3D", "input=bg-corr labels=labels mean max numberofvoxels");

