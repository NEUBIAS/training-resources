
run("Close All"); // close all opened windows
run("MRI Stack"); // load the example MRI image stack
imageName = getTitle(); //get the image title 

//select first slice, calculate its mean intensity and display it
selectWindow(imageName);
sliceNumber = 1;	
meanIntensitySlice1 = calculateSliceMeanIntensity(sliceNumber);
print("Slice#"+ sliceNumber + " has mean intensity: " + meanIntensitySlice1);

//select last slice, calculate its mean intensity and display it
selectWindow(imageName);
sliceNumber = nSlices;
meanIntensitySlice2 = calculateSliceMeanIntensity(sliceNumber);
print("Slice#"+ sliceNumber + " has mean intensity: " + meanIntensitySlice2);
	

// a function that calculates mean intensity of a specified slice in a stack and displays it
function calculateSliceMeanIntensity(sliceNumber)
{
	setSlice(sliceNumber);
	run("Duplicate...", "title=slice"+sliceNumber);
	sliceName = "slice"+sliceNumber;
	selectWindow(sliceName);
	getStatistics(area, mean);
	return mean;	
}




