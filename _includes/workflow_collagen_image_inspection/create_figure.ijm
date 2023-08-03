run("Close All");

//ctrlImageColagenPath = "/Users/christiantischer/Downloads/Collagen_imaging/control 0h/P018--B6--B6/NT22-004-14032022-Col1-B--B6--B6--W0018--P018--T00001--Z001--C02.ome.tif";
//treatedImageColagenPath = "/Users/christiantischer/Downloads/Collagen_imaging/control 96h/P008--A1--A1/NT22-004-14032022-Col1-B--A1--A1--W0001--P008--T00001--Z001--C02.ome.tif";

viewImage("/Users/christiantischer/Downloads/Collagen_imaging/control 0h/P018--B6--B6/NT22-004-14032022-Col1-B--B6--B6--W0018--P018--T00001--Z001--C02.ome.tif", "ctrl", 0, 3500);
viewImage("/Users/christiantischer/Downloads/Collagen_imaging/control 96h/P008--A1--A1/NT22-004-14032022-Col1-B--A1--A1--W0001--P008--T00001--Z001--C02.ome.tif", "treated", 0, 3500);


function viewImage(imagePath, imageName, min, max) { 
	// Open image
	open(imagePath);
	rename(imageName);
	
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
}


