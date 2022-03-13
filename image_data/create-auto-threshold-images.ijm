run("Close All");

image = createImage("xy_8bit__two_bright_one_dark", 200, 75);
threshold(image);

image = createImage("xy_8bit__two_bright", 200, 0);
threshold(image);

image = createImage("xy_8bit__just_noise", 0, 0);
threshold(image);

function threshold(image) 
{
	run("Histogram");
	selectWindow(image);
	run("Duplicate...", " ");
	run("Auto Threshold", "method=Huang white");
	rename(image + "_Huang");
	selectImage(image);
	run("Duplicate...", " ");
	run("Auto Threshold", "method=Otsu white");
	rename(image + "_Otsu");
	//IJ.log(getTitle());
	//run("Auto Threshold", "method=[Try all] white show");	
}

function createImage( name, bright, dark )
{
	background = 10;
	size = 80;
	
	newImage(name, "8-bit black", 4 * size, 1.5 * size, 1);
	run("Add...", "value=&background");

	makeOval(20, 20, size, size);
	run("Add...", "value=&bright");
	
	makeOval(1.5 * size, 20, size, size);
	run("Add...", "value=&bright");
	
	makeOval(2.7 * size, 20, size, size);
	run("Add...", "value=&dark");
	
	run("Select None");
	
	run("Gaussian Blur...", "sigma=5");
	
	run("Add Specified Noise...", "standard=5");
	
	return getTitle();
}
