run("Close All"); // close all images

// get file from user (see: https://imagej.net/Script_Parameters)
#@File (label="Please select file") file

// open file
open(file);
rename("input");

// threshold
run("Duplicate...", "duplicate title=binary");
setThreshold(21, 255);
run("Convert to Mask", "method=Default background=Dark black");

// connected components labeling
run("Connected Components Labeling", "type=[8 bits]");
rename("labels");

// TODO: remove very small objects
// Hint: Record [ Plugins > MorphoLibJ > Label images > Label Size Opening ]

// TODO: remove objects touching image boundary
// Hint: Record [ Plugins > MorphoLibJ > Label images > Remove Border Labels ]

// display labels on input
run("Merge Channels...", "c2=labels c4=input create ignore keep");
run("glasbey_inverted"); // change LUT
rename("overlay");

// clean up
selectWindow("binary");
close();
