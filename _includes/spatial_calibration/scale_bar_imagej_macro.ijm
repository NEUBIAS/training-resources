// Open image using Bio-Formats
run("Bio-Formats Importer", "open=[Path_to_your_image] display_metadata");

// As macros cannot directly read the text from the metadata window, 
// We skip the part about reading from the metadata text window,
// which has to be done manually.

// Get pixel width and height from properties
getPixelSize(unit, pixelWidth, pixelHeight);
print("Unit =", unit);
print("pixelHeight= ", pixelHeight);
print("pixelWidth", pixelWidth);


// Add scale bar to the image
run("Scale Bar...", "width=100 height=5 font=12 color=White background=None location=[Lower Right] overlay");



