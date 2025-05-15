// File > Close All
run("Close All");
// File > Open...
open("C:/Users/akhan/training-resources/image_data/xy_8bit__em_mitochondria_er.tif");

// Image › Duplicate...
run("Duplicate...", "title=variance_5");

// Image > Type > 16-bit (since in variance calculation values can exceed 255 which is current bit depth of input image)
run("16-bit");

// Process › Filters › Variance...
run("Variance...", "radius=5");

// Image › Adjust › Threshold...   ([x] Dark Background)
setAutoThreshold("Default dark");

//Press `Set` button (example upper and lower threshold values are (113, 255))
setThreshold(113, 255);

// Press `Apply` button
run("Convert to Mask");

// Image › Lookup Tables › InvertLUT... (if highest values are darker and lowest brighter)
run("Invert LUT");
