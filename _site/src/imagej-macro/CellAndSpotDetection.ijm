open("/Users/tischi/Dropbox/Presentations_Courses/2015--Tischi--Kopenhagen/0000--PracticalImagej/data/autophagosomes/autophagosomes_raw.tif");
run("Gaussian Blur...", "sigma=15");
run("Find Maxima...", "noise=50 output=[Segmented Particles]");
run("Analyze Particles...", "exclude add");
open("/Users/tischi/Dropbox/Presentations_Courses/2015--Tischi--Kopenhagen/0000--PracticalImagej/data/autophagosomes/autophagosomes_raw.tif");
rename("raw");
run("Duplicate...", "title=median_bg");
run("Median...", "radius=5");
imageCalculator("Subtract", "raw","median_bg");
run("Find Maxima...", "noise=50 output=[Single Points]");
run("Divide...", "value=255");
rename("spots.tif")
selectWindow("spots.tif");
roiManager("Measure");
saveAs("Results", "/Users/tischi/Dropbox/Presentations_Courses/2015--Tischi--Kopenhagen/0000--PracticalImagej/data/autophagosomes/spot_count.csv");

close("*");

list = getList("window.titles"); 
for (i=0; i<list.length; i++) { 
	winame = list[i]; 
    selectWindow(winame); 
    run("Close"); 
} 