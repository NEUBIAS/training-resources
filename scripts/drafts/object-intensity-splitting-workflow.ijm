#@File image
#@Integer threshold
#@Double blurHalfWidth

// Notes
// - this only works for 8-bit images, because of 'max = 255 - threshold'

// open image
run("Close All");
open(image);

// smooth
run("Duplicate...", "title=blur");
run("Gaussian Blur...", "sigma="+blurHalfWidth);

// invert
run("Duplicate...", "title=invert");
run("Invert");
run("Enhance Contrast", "saturated=0.35");

// watershed
max = 255 - threshold; // this is because we inverted the 8-bit input image
run("Classic Watershed", "input=invert mask=None use min=0 max="+max);
run("16_colors");
