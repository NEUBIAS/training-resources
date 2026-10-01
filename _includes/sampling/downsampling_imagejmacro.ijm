run("Close All")

// Open the image
//open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__DNA_sampling_35nm.tif")
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__MT_sampling_35nm.tif")
rename("scaling_1");
//Down scale with a factor of 2
selectImage("scaling_1");
run("Scale...", "x=0.5 y=0.5 interpolation=Bilinear average create title=scaling_2.tif");

//Down scale with a factor of 4
selectImage("scaling_1"); // Make sure you always start from the original image
factor = 4
downsample = 1/factor
run("Scale...", "x="+downsample+" y="+downsample+" interpolation=Bilinear average create title=scaling_"+factor+".tif");

//Down scale with a factor of 16
selectImage("scaling_1");
factor = 16
downsample = 1/factor
run("Scale...", "x="+downsample+" y="+downsample+" interpolation=Bilinear average create title=scaling_"+factor+".tif");

