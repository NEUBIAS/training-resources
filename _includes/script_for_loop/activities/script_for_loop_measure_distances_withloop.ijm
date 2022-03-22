// Macro to measure closest, furthest and mean distance of labels to each other
// This is a version with a loop
run("Close All");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit_labels__nuclei.tif");
rename("labels");
// Explain how to find maximal value of loop
getRawStatistics(nPixels, mean, min, max, std, histogram);

for (i = 0; i < max; i++) {
	run("Duplicate...", "title=binary");
	labelID = i+1;
	run("Manual Threshold...", "min="+labelID+ " max="+ labelID);
	run("Convert to Mask");
	run("Invert");
	run("Chamfer Distance Map", "distances=[Chessknight (5,7,11)] output=[16 bits] normalize");
	run("Intensity Measurements 2D/3D", "input=binary-dist labels=labels mean max min");
	close("binary");
	close("binary-dist");
	Table.rename("binary-dist-intensity-measurements", "dist_label"+labelID);
}
