#@File image
#@Integer threshold

// open image
run("Close All");
open(image);

// invert
run("Duplicate...", "title=invert");
run("Invert");
run("Enhance Contrast", "saturated=0.35");

// watershed
max = 255 - threshold; // this is because we inverted the 8-bit input image
run("Classic Watershed", "input=invert mask=None use min=0 max="+max);
