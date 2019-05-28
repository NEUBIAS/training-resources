directory = getDirectory("Choose Input Directory");
outputDirectory = getDirectory("Choose Output Directory");
threshold = getNumber("Please enter threshold", 10);

// clean up
run("Close All");
close("*.csv");


// configure output
outputTablePath = outputDirectory + "results_threshold=" + threshold + ".csv";

fileList = getFileList(directory);

setBatchMode( true );

for (i = 0; i < fileList.length; i = i + 1) {
    
    if ( endsWith(fileList[i], ".tif") ) {
      
		filePath = directory + fileList[i];
		
		// clean up
		run("Close All");
		
		// open data
		open( filePath );
		
		// segment nuclei
		segmentNuclei( threshold );
		
		// measure nuclei properties
		run("Set Measurements...", "area display redirect=None decimal=3");
		run("Analyze Particles...", "summarize");    
    }
}


// save results table
print( "Saving: " + outputTablePath );
saveAs("Results", outputTablePath );
close("*.csv");

setBatchMode( true );

// FUNCTIONS

function segmentNuclei( threshold ) {
	setThreshold( threshold, 255);
	setOption("BlackBackground", true);
	run("Convert to Mask");
}
