run("Close All");
// File › Open...
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_calibrated_16bit__nuclear_protein_control.tif");
// [Image › Lookup Tables › Grays ]
run("Grays");
// [ Image › Adjust › Brightness/Contrast... ]
setMinAndMax(8, 3804);
// Analyze › Tools › Calibration Bar...
run("Calibration Bar...", "location=[Upper Left] fill=[Dark Gray] label=White number=5 decimal=0 font=10 zoom=2 overlay");

open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_calibrated_16bit__nuclear_protein_treated.tif");
run("Grays");
setMinAndMax(8, 3804);
run("Calibration Bar...", "location=[Upper Left] fill=[Dark Gray] label=White number=5 decimal=0 font=10 zoom=2 overlay");
// Window › Tile
run("Tile");
