// Open a sample 2D particles image and apply morphological opening with different radius and compare the number of resulting connected components
// Task: 1) Figure out the repetitive part of the code, and 
//       2) Apply a function to perform the repetitive task

run("Close All"); // close all opened windows
run("Particles"); // open sample particles image
imageName = getTitle(); //get the image title 
run("Duplicate...", "particles-1"); //duplicate the image
run("Invert LUT"); //invert the lookup table as background has value of 255 and foreground (particles) has a value of 0
radiusOpeningFilter = 3; // select the size of opening filter you want to apply 
run("Morphological Filters", "operation=Opening element=Disk radius="+ radiusOpeningFilter); // Apply morphological opening
run("Connected Components Labeling", "connectivity=4 type=[16 bits]"); // Run connected component (CC) analysis
getStatistics(area, mean, min, max, std, histogram); // calculate the maximum value of image
highestLabelNumber = max;
print("Number of particles detected: " + highestLabelNumber); // Print the maximum value of th image
selectWindow("particles.gif"); 
run("Close All"); // close all opened windows
run("Particles");
imageName = getTitle(); //get the image title 
run("Duplicate...", "particles-1"); //duplicate the image
run("Invert LUT"); //invert the lookup table as background has value of 255 and foreground (particles) has a value of 0
radiusOpeningFilter = 5; // select the size of opening filter you want to apply 
run("Morphological Filters", "operation=Opening element=Disk radius="+ radiusOpeningFilter); // Apply morphological opening
run("Connected Components Labeling", "connectivity=4 type=[16 bits]"); // Run connected component (CC) analysis
getStatistics(area, mean, min, max, std, histogram); // calculate the maximum value of image
highestLabelNumber = max;
print("Number of particles detected: " + highestLabelNumber); // Print the maximum value of the image

