filePath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_small.tif"

// init
run("Close All");
run("Options...", "iterations=1 count=1 black do=Nothing");

// open
open(filePath);

// draw background ROI
waitForUser("Please draw a background ROI");
getStatistics(area, mean, min, max, std, histogram);

// log background intensity
print("Mean background intensity: " + mean );

