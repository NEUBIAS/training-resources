
run("Close All"); // close all opened windows
run("MRI Stack"); // load the example MRI image stack
imageName = getTitle(); //get the image title 

//select first slice,calculate its mean intensity and display it
selectWindow(imageName);
sliceNumber = 1;	
calculateSliceMeanIntensity(sliceNumber);

//select last slice,calculate its mean intensity and display it
selectWindow(imageName);
sliceNumber = nSlices;
calculateSliceMeanIntensity(sliceNumber);
	

// a function that calculates mean intensity of a specified slice in a stack and displays it
function calculateSliceMeanIntensity(sliceNumber)
{
	setSlice(sliceNumber);
	run("Duplicate...", "title=slice"+sliceNumber);
	sliceName = "slice"+sliceNumber;
	selectWindow(sliceName);
	run("8-bit");
	getStatistics(area, mean);
	print("Slice#"+ sliceNumber + " has mean intensity: " + mean);
}


