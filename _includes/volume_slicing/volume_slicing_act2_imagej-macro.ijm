// Close other open images
run("Close All");

// open image
openImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit_spheres.tif")

// crop out the green sphere
makeRectangle(23,7,18,18);
run("Duplicate...", "duplicate channels=2 slices=3-11");
rename("Green sphere");

// Reslice green sphere from the top, WITH interpolation
selectWindow("Green sphere")
run("Reslice [/]...", "output=2.000 start=Top rotate");
rename("Green sphere viewed from the top, WITH interpolation")
run("Duplicate...", "duplicate range=5-5");
rename("Green sphere YZ slice WITH interpolation")

// Reslice green sphere from the top, WITHOUT interpolation
selectWindow("Green sphere")
run("Reslice [/]...", "output=2.000 start=Top avoid");
rename("Green sphere viewed from the top, WITHOUT interpolation")
run("Duplicate...", "duplicate range=10-10");
rename("Green sphere YZ slice WITHOUT interpolation")

run("Tile")
