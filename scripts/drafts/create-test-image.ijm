// create empty image
newImage("test", "8-bit black", 400, 400, 1);

// add offset
run("Add...", "value=25");

// draw object
setForegroundColor(164, 164, 164);
makeOval(72, 88, 14, 14);
run("Fill", "slice");

// draw object
setForegroundColor(210, 210, 210);
makeOval(168, 90, 14, 13);
run("Fill", "slice");

// remove selection (otherwise all following actions will only be executed in the selected region)
run("Select None");

// blur
run("Gaussian Blur...", "sigma=5");

// add noise
run("Add Specified Noise...", "standard=5");
