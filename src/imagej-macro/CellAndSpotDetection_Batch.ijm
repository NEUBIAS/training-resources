dirIn = getDirectory("Choose input directory!");
imFileExtension = getString("What is the ending of your image files?",".tif");
files = getFileList(dirIn);

setBatchMode(true); 
		
for(i=0; i<lengthOf(files); i++) {

	if(endsWith(files[i],imFileExtension)) { 
		
		closeEverything();
		
		print("Working on: "+dirIn+files[i]);
		
		open(dirIn+files[i]); // opens the image
		rename("inputImage"); 
		
		///////////////////////////////////////////
		// Copy and paste your macro code BELOW! //
		/////////////////////////////////////////// 
		
		// find cells
		selectWindow("inputImage"); 
		run("Duplicate...", "title=GaussianBlur"); 	
		run("Gaussian Blur...", "sigma=10");
		run("Find Maxima...", "noise=50 output=[Segmented Particles]");
		rename("Cells");
		selectWindow("GaussianBlur");
		setThreshold(230, 100000); // changed: set upper threshold super high
		setOption("BlackBackground", false);
		run("Convert to Mask");
		rename("Foreground");
		imageCalculator("AND create", "Foreground","Cells");
		run("Analyze Particles...", "size=500-Infinity exclude add"); // changed: put minimum cell size higher
		
		// find spots
		selectWindow("inputImage"); 
		run("Duplicate...", "title=median_bg");
		run("Median...", "radius=5");
		imageCalculator("Subtract create", "inputImage", "median_bg");
		run("Find Maxima...", "noise=50 output=[Single Points]");
		run("Divide...", "value=255");
		rename("spots.tif");
		
		// measure spots and save results
		selectWindow("spots.tif");
		roiManager("Measure");
		saveAs("Results", dirIn+files[i]+"--spot_count.csv"); // changed: used dirIn to construct path
		
	
		///////////////////////////////////////////
		// Copy and paste your macro code ABOVE! //
		///////////////////////////////////////////
		 	
	}

}

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
