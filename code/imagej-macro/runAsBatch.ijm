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
