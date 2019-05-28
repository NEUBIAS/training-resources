// some options:
// selectWindow("Results"); 
// run("Close"); 
// selectWindow("ROI Manager"); 
// run("Close"); 

// closes all image windows (found on: http://rsb.info.nih.gov/ij/developer/macro/functions.html) 
close("*");

// closes all non-image windows (found on:http://imagej.1557.x6.nabble.com/closing-non-picture-windows-from-a-macro-td3693084.html)
list = getList("window.titles"); 
for (i=0; i<list.length; i++) { 
	winame = list[i]; 
    selectWindow(winame); 
    run("Close"); 
} 

// make one function of it:
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
