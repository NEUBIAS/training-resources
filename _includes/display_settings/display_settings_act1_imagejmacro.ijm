// File › Close All
run("Close All");

// File › Open...
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_high_dynamic_range.tif");

// Image › Rename...
rename("gray_0_255"); 

// Analyze › Tools › Calibration Bar...
run("Calibration Bar...", "location=[Upper Left] fill=None label=White number=5 decimal=0 font=5 zoom=0.7 overlay");

// Image › Duplicate...
run("Duplicate...", "title=gray_0_43");

// Image › Adjust › Brightness/Contrast..
setMinAndMax(0, 43);

run("Calibration Bar...", "location=[Upper Left] fill=None label=White number=5 decimal=0 font=5 zoom=0.7 overlay");
run("Duplicate...", "title=blue_0_255");
run("Blue");
setMinAndMax(0, 255);

run("Calibration Bar...", "location=[Upper Left] fill=None label=White number=5 decimal=0 font=5 zoom=0.7 overlay");
run("Duplicate...", "title=fire_0_255");
run("Fire");

run("Calibration Bar...", "location=[Upper Left] fill=None label=White number=5 decimal=0 font=5 zoom=0.7 overlay");
run("Duplicate...", "title=hilo_0_255");
run("HiLo");

run("Calibration Bar...", "location=[Upper Left] fill=None label=White number=5 decimal=0 font=5 zoom=0.7 overlay");
run("Duplicate...", "title=hilo_20_100");
setMinAndMax(20, 100);

run("Calibration Bar...", "location=[Upper Left] fill=None label=White number=5 decimal=0 font=5 zoom=0.7 overlay");
run("Tile");
