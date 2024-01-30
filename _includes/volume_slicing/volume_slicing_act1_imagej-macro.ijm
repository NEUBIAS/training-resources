// open image stack
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit_calibrated__dna_metaphase.tif");

// explore the dimensions
width = getWidth();
height = getHeight();
depth = nSlices();
print("Original Image Dimensions: Width = " + width + ", Height = " + height + ", Depth = " + depth);

// reslice YZ with interpolation
run("Reslice [/]...", "output=0.300 start=Left flip rotate");
rename("YZ view");
width = getWidth();
height = getHeight();
depth = nSlices();
print("Image Dimensions YZ view: Width = " + width + ", Height = " + height + ", Depth = " + depth);

// reslice XZ with interpolation
selectImage("xyz_16bit_calibrated__dna_metaphase.tif");
run("Reslice [/]...", "output=0.300 start=Top");
rename("XZ view");
width = getWidth();
height = getHeight();
depth = nSlices();
print("Image Dimensions XZ view: Width = " + width + ", Height = " + height + ", Depth = " + depth);

// reslice YZ without interpolation
selectImage("xyz_16bit_calibrated__dna_metaphase.tif");
run("Reslice [/]...", "output=0.300 start=Left flip rotate avoid");
rename("YZ view");
width = getWidth();
height = getHeight();
depth = nSlices();
print("Image Dimensions YZ view WITHOUT interpolation: Width = " + width + ", Height = " + height + ", Depth = " + depth);

// reslice XZ with interpolation
selectImage("xyz_16bit_calibrated__dna_metaphase.tif");
run("Reslice [/]...", "output=0.300 start=Top avoid");
rename("XZ view");
width = getWidth();
height = getHeight();
depth = nSlices();
print("Image Dimensions XZ view WITHOUT interpolation: Width = " + width + ", Height = " + height + ", Depth = " + depth);

run("Tile")
