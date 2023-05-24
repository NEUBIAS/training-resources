// This macro opens the head image stack and reslices it to view it from different angles (side, front, top and diagonal view)
// and then selects slices corresponding to Z=60, X=135, and Y=160.
// Close other open images
run("Close All");

// open head image stack
open("http://imagej.net/images/t1-head.zip");
rename("Head viewed from the side");
run("Duplicate...", "duplicate range=60");
rename("Head Z=60");

// Reslice the head image stack to view the head from the front and from the top, and select the slices for X=135 and Y=160 in the orginal view.
selectWindow("Head viewed from the side");
run("Reslice [/]...", "output=1.500 start=Left rotate"); // view head from the front
rename("Head viewed from the front");
run("Duplicate...", "duplicate range=135-135");
rename("Head X=135");

selectWindow("Head viewed from the side");
run("Reslice [/]...", "output=1.500 start=Top rotate"); // view head from the top
rename("Head viewed from the top");
run("Duplicate...", "duplicate range=160-160");
rename("Head Y=160");

// Rotate the head stack that is viewed from the side and reslice to obtain diagonal view
selectWindow("Head viewed from the side");
run("Duplicate...", "duplicate");
run("Rotate... ", "angle=45 grid=1 interpolation=Bilinear enlarge stack"); // rotate the stack
run("Reslice [/]...", "output=1.500 start=Top rotate");
rename("Head in diagonal view");

run("Tile");
