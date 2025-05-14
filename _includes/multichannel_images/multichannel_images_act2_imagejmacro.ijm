// Load a multi channel image and save composite images
run("Close All");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__cell_dna_mts_actin.tif");
rename("input");
Stack.setChannel(1);
setMinAndMax(143, 500);

Stack.setChannel(2);
setMinAndMax(100, 509);

Stack.setChannel(3);
setMinAndMax(100, 5055);

//  Image › Type › RGB Color
run("RGB Color");
rename("rgb");
// Eventually save the image
//saveAs("Tiff", "/your_path/rgb.tif");

// Show grayscale 
selectImage("input")
Property.set("CompositeProjection", "null");
Stack.setDisplayMode("grayscale");

// Image › Stacks › Make Montage...
run("Make Montage...", "columns=3 rows=1 scale=1");
rename("Montage");

//  Image › Stacks › Tools  › Combine...
run("Combine...", "stack1=Montage stack2=rgb");
rename("montage_rgb");

// Add a scale bar
run("Scale Bar...", "width=10 height=10 horizontal bold hide");
// Eventually save the image
//saveAs("Tiff", "/your_path/montage_rgb.tif");