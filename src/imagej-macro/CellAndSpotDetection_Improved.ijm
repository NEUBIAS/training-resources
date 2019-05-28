// close all windows
closeEverything();

// hide windows during run (much faster!!)
//setBatchMode(true);

// find cells
open("/Users/tischi/Dropbox/Presentations_Courses/2015--Tischi--Kopenhagen/0000--PracticalImagej/data/autophagosomes/autophagosomes_raw.tif");
run("Gaussian Blur...", "sigma=10");
rename("blurredImage");
run("Find Maxima...", "noise=50 output=[Segmented Particles]");
rename("cells");
selectWindow("blurredImage");
setThreshold(230, 714);
setOption("BlackBackground", false);
run("Convert to Mask");
rename("foreground");
imageCalculator("AND create", "foreground","cells");
run("Analyze Particles...", "size=100-Infinity exclude add");

// find spots
open("/Users/tischi/Dropbox/Presentations_Courses/2015--Tischi--Kopenhagen/0000--PracticalImagej/data/autophagosomes/autophagosomes_raw.tif");
rename("raw");
run("Duplicate...", "title=median_bg");
run("Median...", "radius=5");
imageCalculator("Subtract create", "raw","median_bg");
run("Find Maxima...", "noise=70 output=[Single Points]");
run("Divide...", "value=255");
rename("spots.tif");

// measure spots and save results
selectWindow("spots.tif");
roiManager("Measure");
saveAs("Results", "/Users/tischi/Dropbox/Presentations_Courses/2015--Tischi--Kopenhagen/0000--PracticalImagej/data/autophagosomes/spot_count.csv");


// functions ////////////////////////////////////////////////

function closeEverything() {
	
  // closes all image windows 
  close("*");

  // closes all non-image windows
  list = getList("window.titles"); 
  for (i=0; i<list.length; i++) { 
	winame = list[i]; 
    selectWindow(winame); 
    run("Close"); 
  } 
	
}