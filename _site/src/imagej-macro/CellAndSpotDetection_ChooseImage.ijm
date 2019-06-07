closeEverything(); // close all windows

////////////////
// load image //
////////////////

// get, open and rename the input file
path = File.openDialog("Select a File");
open(path);
rename("inputImage"); 

// hide windows during run (much faster!!)
//setBatchMode(true);

////////////////
// find cells //
////////////////

// removed: open("/Users/tischi/Dropbox/Presentations_Courses/2015--Tischi--Kopenhagen/0000--PracticalImagej/data/autophagosomes/autophagosomes_raw.tif");
selectWindow("inputImage"); // added
run("Duplicate...", "title=GaussianBlur"); // added (to avoid that input image is 'lost' as we need it later)		
run("Gaussian Blur...", "sigma=10");
run("Find Maxima...", "noise=50 output=[Segmented Particles]");
rename("Cells");
selectWindow("GaussianBlur");
setThreshold(230, 100000); // changed: set upper threshold super high
setOption("BlackBackground", false);
run("Convert to Mask");
rename("Foreground");
imageCalculator("AND create", "Foreground","Cells");
run("Analyze Particles...", "size=100-Infinity exclude add");


////////////////
// find spots //
////////////////

// removed: open("/Users/tischi/Dropbox/Presentations_Courses/2015--Tischi--Kopenhagen/0000--PracticalImagej/data/autophagosomes/autophagosomes_raw.tif");
selectWindow("inputImage");
run("Duplicate...", "title=median_bg");
run("Median...", "radius=5");
imageCalculator("Subtract create", "inputImage", "median_bg");
run("Find Maxima...", "noise=70 output=[Single Points]");
run("Divide...", "value=255");
rename("spots.tif");

////////////////////////////
// measure and save spots //
////////////////////////////

selectWindow("spots.tif");
roiManager("Measure");
// removed: saveAs("Results", "/Users/tischi/Dropbox/Presentations_Courses/2015--Tischi--Kopenhagen/0000--PracticalImagej/data/autophagosomes/spot_count.csv");
saveAs("Results", path+"--spot_count.csv"); // added (to have a flexible output filename)


///////////////
// functions //
///////////////

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