radius = 3;
rename("input");
run("Duplicate...", "title=opened");
run("Minimum...", "radius="+radius);
run("Maximum...", "radius="+radius);
imageCalculator("Subtract create", "input","opened");
selectWindow("Result of input");
rename("tophat");
