run("Close All");
newImage("test", "8-bit black", 512, 512, 1);
run("Properties...", "pixel_width=5 pixel_height=5 voxel_depth=5");
run("Add...", "value=25"); // offset

pixelWidth = 5; // nm
Stack.setXUnit("nanometer");
Stack.setYUnit("nanometer");

factor = 1;
w = 50 * factor;
b = 200 / factor;
setWidthAndBrightness( w, b );
drawLine(63, 70, 439, 70);

factor = 2;
w = 50 * factor;
b = 200 / factor;
setWidthAndBrightness( w, b );
drawLine(63, 200, 439, 200);

factor = 4;
w = 50 * factor;
b = 200 / factor;
setWidthAndBrightness( w, b );
drawLine(63, 350, 439, 350);

rename("truth");
run("Duplicate...", "title=image");

run("32-bit");
run("Gaussian Blur...", "sigma=100 scaled");
run("Enhance Contrast", "saturated=0.35");

// downsample to 50 nm pixel size
run("Scale...", "x=0.25 y=0.25 interpolation=Bilinear average create");
run("Add Specified Noise...", "standard=1");

function setWidthAndBrightness( w, b )
{
	setLineWidth(w  / pixelWidth );
	setForegroundColor( b, b, b);
}