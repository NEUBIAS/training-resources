open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__PCNA.tif")
selectWindow("xy_8bit__PCNA.tif");
run("Duplicate...", "title=[2 nuclei]");
selectWindow("xy_8bit__PCNA.tif");
run("Duplicate...", "title=[boundary]");
selectWindow("xy_8bit__PCNA.tif");
run("Duplicate...", "title=[dots]");
selectWindow("2 nuclei");
setThreshold(5, 255);
setOption("BlackBackground", true);
run("Convert to Mask");
selectWindow("boundary");
setThreshold(4, 4);
setOption("BlackBackground", true);
run("Convert to Mask");
selectWindow("dots");
setThreshold(44, 255);
setOption("BlackBackground", true);
run("Convert to Mask");