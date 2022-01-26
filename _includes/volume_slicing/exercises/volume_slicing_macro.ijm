""" Open the head image stack and reslice it to view it from different angles (side, top, and front) """

// Close other open images
run("Close All");

// open head image stack
open("http://imagej.net/images/t1-head.zip");
rename("Head viewed from the side");

// Reslice the head image stack to view the head from the top and from the side
run("Reslice [/]...", "output=1.500 start=Top"); // view head from the top 
rename("Head viewed from the top");
run("Reslice [/]...", "output=1.500 start=Left"); // view head from the front
rename("Head viewed from the front");

run("Tile");