// Create a series of binary masks and then a band of those
// Using for loops generalize the script for multiple erode operations

run("Close All");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nup_nuclei/xy_8bit_binary__nuclei.tif");
rename("input");

// Part 2 of exercise
maxErode = 1;
// Erode once
selectWindow("input");
run("Duplicate...", "title=erode"+maxErode);
for(i = 1; i < maxErode; i++){
	run("Erode");	
}
run("Outline");

// Part 3 of exercise, use a loop in a loop
for (maxErode = 1; maxErode < 51; maxErode++){
	// Erode once
	selectWindow("input");
	run("Duplicate...", "title=erode"+maxErode);
	for(i = 1; i < maxErode; i++){
		run("Erode");	
	}
	run("Outline");
}
run("Images to Stack", "name=Stack title=erode use");

