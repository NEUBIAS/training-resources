// --- Requirements ---

// - Fiji
// - Update sites:
//    - IJPB-plugins

// --- Configuration ---

// Input image paths
imagePaths = newArray(
    "image_data/xy_16bit__bacteria_cords_thick.tif",
    "image_data/xy_16bit__bacteria_cords_thin.tif"
);

// Output directory
outputDir = "FIXME";

// Granulometry radii in SCALED UNITS
radii = newArray(5, 10, 20, 40);

// Thresholding Method
thresholdMethod = "Otsu";


// --- Code ---

if (!File.exists(outputDir)) {
    File.makeDirectory(outputDir);
}

// --- Main Processing ---
setBatchMode(true);
run("Clear Results");
run("Close All");

for (i = 0; i < imagePaths.length; i++) {
    processImage(imagePaths[i], radii);
}

setBatchMode(false);
updateResults();
saveAs("Results", outputDir + File.separator + "Results.csv");

exit("Analysis Complete.\n\nResults saved to " + outputDir);

function processImage(path, radii) {
    open(path);
    originalImg = getTitle();
    setResult("Image", nResults, originalImg);
    
    // Get scaling info
    getVoxelSize(pixelWidth, pixelHeight, depth, unit);
    setResult("Unit", nResults-1, unit);
    
    // Pre-process: Thresholding
    setAutoThreshold(thresholdMethod + " dark");
    run("Convert to Mask");
    saveAs("Tiff", outputDir + File.separator + originalImg + "_Binary.tif");
    rename(originalImg); // NB: Saving changes the image name
    
    // Get total foreground pixels for normalization
    getStatistics(area, mean, min, max, std, histogram);
    totalPixels = histogram[255]; 
    
    // 2. Create Granulometry map image
    labelMap = "Granulometry_" + originalImg;
    newImage(labelMap, "32-bit black", getWidth(), getHeight(), 1);
    
    // 3. Calculate baseline (Radius 0)
    previousCount = totalPixels;

    // 4. Perform Granulometry
    for (r = 0; r < radii.length; r++) {
    	scaledRadius = radii[r];
        radius = scaledRadius / pixelWidth; // Convert to pixels
        
        selectWindow(originalImg);
        
        // MorphoLibJ Opening
        run("Morphological Filters", "operation=Opening element=Disk radius=" + radius);
        openedImg = getTitle();
        
        // Count pixels remaining
        getStatistics(area, mean, min, max, std, histogram);
        currentCount = histogram[255];
        
        // Quantify removed pixels for the table
        removedPixels = previousCount - currentCount;
        setResult("Up_To_" + scaledRadius, nResults-1, (removedPixels / totalPixels));
        
        // UPDATE LABEL MAP: 
        // For every pixel currently white (survived), update the map with this radius value.
        // Since radii increase, the final value in the map is the MAX radius that survived.
        updateSurvivalMap(labelMap, openedImg, radius);
        
        // Cleanup for next step
        previousCount = currentCount;
        selectWindow(openedImg);
        close();
    }
    
    // Add remainder to table
    setResult("Larger_Than_" + radii[radii.length-1], nResults-1, (previousCount / totalPixels));
    
    // Finalize Display
    selectWindow(labelMap);
    run("Fire");
    resetMinAndMax();
    saveAs("Tiff", outputDir + File.separator + originalImg + "_Granulometry.tif");
    
    selectWindow(originalImg);
    run("Close All");
}

// Function to stamp the current radius onto surviving pixels
function updateSurvivalMap(mapName, binaryMask, radiusValue) {
    selectWindow(binaryMask);
    run("Duplicate...", "title=tempMask");
    run("32-bit");
    // Multiply mask (0 or 255) by (radius / 255) to get pixel values = radius
    run("Multiply...", "value=" + (radiusValue / 255));
    
    // Use 'Max' operation: if current radius is larger than what is already there, update it
    imageCalculator("Max", mapName, "tempMask");
    
    selectWindow("tempMask");
    close();
}
