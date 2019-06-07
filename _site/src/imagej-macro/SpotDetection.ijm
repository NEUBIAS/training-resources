open("/Users/tischi/Dropbox/Presentations_Courses/2015--Tischi--Kopenhagen/0000--PracticalImagej/data/autophagosomes/autophagosomes_raw.tif");
rename("raw");
run("Duplicate...", "title=median_bg");
run("Median...", "radius=5");
imageCalculator("Subtract create", "raw","median_bg");
run("Find Maxima...", "noise=100 output=[Single Points]");
run("Divide...", "value=255");
rename("spots.tif")
