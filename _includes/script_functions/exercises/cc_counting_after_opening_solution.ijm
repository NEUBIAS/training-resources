// Open a sample 2D particles image and apply morphological opening with different radius and compare the number of resulting connected components
// Task: 1) Figure out the repetitive part of the code, and 
//       2) Apply a function to perform the repetitive task

// SOLUTION:

run("Close All"); // close all opened windows
run("Particles"); // open sample particles image
radiusOpeningFilter = 3; // set the opening filter size
applyOpeningCountCC(radiusOpeningFilter); // call the function

selectWindow("particles.gif"); // select the original image window to repeat the task
radiusOpeningFilter = 5; // set the opening filter size
applyOpeningCountCC(radiusOpeningFilter); // call the function



function applyOpeningCountCC(radiusOpeningFilter) // Function to perform the repititive task, this function duplicates image, apply morphological opening, CC analysis and display total number of CC found
{
	run("Duplicate...", "particles-1"); //duplicate the image
	run("Invert LUT"); //invert the lookup table as background has value of 255 and foreground (particles) has a value of 0
	run("Morphological Filters", "operation=Opening element=Disk radius="+ radiusOpeningFilter); // Apply morphological opening
	run("Connected Components Labeling", "connectivity=4 type=[16 bits]"); // Run connected component (CC) analysis
	getStatistics(area, mean, min, max, std, histogram); // calculate the maximum value of image
	highestLabelNumber = max;
	print("Number of particles detected: " + highestLabelNumber); // Print the maximum value of th image
}

