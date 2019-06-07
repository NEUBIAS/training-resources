#@File reference
#@File objects

run("Close All");

open(reference);
rename("reference");

open(objects);
rename("objects");

// select the binary image with the reference structure to which we want to compute the distances to 
selectWindow("reference");
run("Duplicate...", "title=invert");

// we need to invert this, because the distance map measures distances to background pixels
run("Invert");

// run the distance map computation
run("Chamfer Distance Map", "distances=[Chessknight (5,7,11)] output=[32 bits] normalize");
rename("distances");

// measure "intensity" ( = distance ) of objects in the distance map image 
run("Intensity Measurements 2D/3D", "input=distances labels=objects mean");

// show reference and objects as composite image
run("Merge Channels...", "c2=reference c4=objects create ignore");



