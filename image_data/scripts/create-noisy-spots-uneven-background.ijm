// create empty image
newImage("test", "8-bit black", 400, 400, 1);

// add offset
run("Add...", "value=10");

//
// draw uneven background
//

background  = 100;
makeOval(150, 150, 100, 100);
run("Add...", "value=&background");

// remove selection (otherwise all following actions will only be executed in the selected region)
run("Select None");

// blur backgroud
run("Gaussian Blur...", "sigma=20");

//
// draw spots
//

diameter = 5;
spots = 40;

// draw spot
makeOval(170, 170, diameter, diameter);
run("Add...", "value=&spots");

// draw spot
makeOval(350, 350, diameter, diameter);
run("Add...", "value=&spots");

// remove selection (otherwise all following actions will only be executed in the selected region)
run("Select None");

// blur spots
run("Gaussian Blur...", "sigma=2");

//
// add noise
//

// add noise
run("Add Specified Noise...", "standard=5");
