// Open image using Bio-Formats
//
// Unfortunately, Bio-Formats cannot read commercial file formats from an URL: https://forum.image.sc/t/open-url-with-bio-formats/85074
// Thus, please download any image specified in the activity and replace "Path_to_your_image" in the below code

run("Bio-Formats Importer", "open=[Path_to_your_image] display_metadata display_ome-xml");

// As macros cannot directly read the text from the metadata window, 
// We skip the part about reading from the metadata text window,
// which has to be done manually.

// Get pixel width and height from properties

getPixelSize(unit, pixelWidth, pixelHeight);
print("Unit =", unit);
print("pixelHeight= ", pixelHeight);
print("pixelWidth", pixelWidth);

// Add scale bar to the image
//
// Please experiment with the parameters to change the scale bar overlay

run("Scale Bar...", "width=100 height=5 font=12 color=White background=None location=[Lower Right] overlay");
