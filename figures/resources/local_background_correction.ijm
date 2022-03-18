run("Close All");
newImage("Untitled", "16-bit black", 512, 512, 1);
makeOval(102, 201, 194, 196);
setForegroundColor(255, 255, 255);
run("Fill", "slice");
run("Select None");
run("Gaussian Blur...", "sigma=150");


value=2000;
makeOval(402, 61, 12, 14);
run("Add...", "value=&value");
makeOval(166, 149, 12, 12);
run("Add...", "value=&value");
makeOval(158, 196, 12, 12);
run("Add...", "value=&value");
makeOval(169, 299, 12, 12);
run("Add...", "value=&value");
run("Select None");

run("Gaussian Blur...", "sigma=5");

setMinAndMax(0, 15000);
run("8-bit");
run("Add Specified Noise...", "standard=4");
run("Scale...", "x=0.5 y=0.5 width=256 height=256 interpolation=Bilinear average create");