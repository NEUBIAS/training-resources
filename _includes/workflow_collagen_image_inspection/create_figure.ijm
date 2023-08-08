/*
 * This macro opens images where tissue culture cells are secreting collagen for different amounts of time.
 * The aim is to display the images such that one can appreciate that after 96 h there is more collagen 
 * secreted than after 0 h. The aim is to make this display as quantitative as possible without doing an actual
 * image analysis.
 */
 
run("Close All");

viewImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/workflow_collagen_image_inspection/xy_16bit__0h_dapi.ome.tif", "https://github.com/NEUBIAS/training-resources/raw/master/image_data/workflow_collagen_image_inspection/xy_16bit__0h_collagen.ome.tif", "0h", 1655, 958, 1928, 961);
viewImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/workflow_collagen_image_inspection/xy_16bit__96h_dapi.ome.tif", "https://github.com/NEUBIAS/training-resources/raw/master/image_data/workflow_collagen_image_inspection/xy_16bit__96h_collagen.ome.tif", "96h", 945, 1446, 1218, 1449);


function viewImage(dapiPath, collagenPath, treatment, px0, py0, px1, py1) { 
	// Open collagen image
	open(collagenPath);
	rename(treatment+"_collagen");
	
	// Adjust and display LUT
	setMinAndMax(0, 3500);
	run("Calibration Bar...", "location=[Upper Left] fill=White label=Black number=5 decimal=0 font=12 zoom=4 overlay");
	
	// Adjust and display spatial calibration
	// - in this case the pixel calibration is missing from the image metadata, thus we need to add it here
	cameraPixelSize = 6.45 // micrometer
	magnification = 20
	imagePixelSize = cameraPixelSize / magnification
	run("Properties...", "pixel_width=imagePixelSize pixel_height=imagePixelSize");
	Stack.setXUnit("micrometer");
	Stack.setYUnit("micrometer");
	run("Scale Bar...", "width=100 height=1 thickness=20 font=50 background=Black location=[Lower Left] overlay");
	
	// Create zoom 
	makeRectangle(921, 1278, 337, 337);
	run("Duplicate...", treatment+"_collagen_zoom");
	run("Scale Bar...", "width=20 height=0 thickness=5 location=[Lower Left] overlay");

	// Create line profile in the middle of the zoom
	makeLine(20, getHeight()/2, getWidth()-20, getHeight()/2);
	run("Plot Profile");
	Plot.setLimits(0.0,95.8,0,9000);
	
	// Open DAPI image	
	open(dapiPath);
	rename(treatment+"_dapi");
	setMinAndMax(0, 4000);  

	// Create merged image
	run("Merge Channels...", "c2="+treatment+"_collagen c3="+treatment+"_dapi create keep ignore");
	rename(treatment+"_composite");	// run("Calibration Bar...", "location=[Upper Left] fill=White label=Black number=5 decimal=0 font=12 zoom=4 overlay"); // ERROR
	run("Scale Bar...", "width=100 height=1 thickness=20 font=50 background=Black location=[Lower Left] overlay");
	
	// Close images that are not needed
	selectImage(treatment+"_dapi");
	close();
}


