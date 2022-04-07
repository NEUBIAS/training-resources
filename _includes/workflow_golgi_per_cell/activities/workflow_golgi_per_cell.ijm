// boilerplate
//
run("Close All");
run("Options...", "iterations=1 count=1 black");

// parameters
//
runInteractive = false;
closeIntermediateImages=true;
nucleusDilationPixels = 30;

nucleusMinimalSizePixels = 2000;
nucleusMaximalSizePixels = 7000;

minGolgiCount = 1;
maxGolgiCount = 200;


// open image (could be commented for adaptive feedback)
//imagePath = "/Users/tischer/Documents/joanna-zukowska-golgi-morphology/src/test/resources/image-data/frag.czi";
//run("Bio-Formats Importer", "open=[&imagePath] color_mode=Default rois_import=[ROI manager] view=Hyperstack stack_order=XYCZT");

run("Set Scale...", "distance=0 known=0 unit=pixel");
// store calibration
getPixelSize(unit, pixelWidth, pixelHeight);
distance = 1 / pixelWidth
rename("origin");

closeAllExceptOrigin()
run("Duplicate...", "duplicate");
rename("raw");



run("Split Channels");
selectWindow("C1-raw");
rename("nuclei");
selectWindow("C2-raw");
rename("golgiChannel");
selectWindow("C3-raw");
close();

// segment nuclei 
selectWindow("nuclei");
//run("Command From Macro", "command=[de.csbdresden.stardist.StarDist2D], args=['input':'nuclei', 'modelChoice':'DSB 2018 (from StarDist 2D paper)', 'normalizeInput':'true', 'percentileBottom':'1.0', 'percentileTop':'99.8', 'probThresh':'0.479071', 'nmsThresh':'0.3', 'outputType':'Label Image', 'nTiles':'1', 'excludeBoundary':'2', 'roiPosition':'Automatic', 'verbose':'false', 'showCsbdeepProgress':'false', 'showProbAndDist':'false'], process=[false]");
//workaround for Stardist issue in batch mode
//run("Command From Macro", "command=[de.csbdresden.stardist.StarDist2D], args=['input':'nuclei', 'modelChoice':'DSB 2018 (from StarDist 2D paper)', 'normalizeInput':'true', 'percentileBottom':'1.0', 'percentileTop':'99.8', 'probThresh':'0.479071', 'nmsThresh':'0.3', 'outputType':'ROI Manager', 'nTiles':'1', 'excludeBoundary':'2', 'roiPosition':'Automatic', 'verbose':'false', 'showCsbdeepProgress':'false', 'showProbAndDist':'false'], process=[false]");



setOption("ScaleConversions", true);
run("8-bit");
run("Enhance Contrast...", "saturated=1");
run("Smooth");
run("Auto Threshold", "method=Otsu white");
run("Fill Holes");
run("Dilate");
run("Fill Holes");
run("Dilate Labels", "radius=5");
//run("Watershed");
run("Analyze Particles...", "size=100-10000 show=Masks display exclude add");

Table.rename("Results", "111");

newImage("Labeling", "16-bit black", getWidth(), getHeight(), 1);

for (index = 0; index < roiManager("count"); index++) {
    roiManager("select", index);
    setColor(index+1);
    fill();
}

resetMinAndMax();
run("glasbey");
//saveAs("Tiff", savename + ".tif");


//

run("Label Size Filtering", "operation=Greater_Than size=&nucleusMinimalSizePixels");
//run("Label Size Filtering", "operation=Greater_Than size=500");

run("Label Size Filtering", "operation=Lower_Than size=&nucleusMaximalSizePixels");
//run("Label Size Filtering", "operation=Greater_Than size=500");

rename("nuclei-labels");
//run("Set Scale...", "distance=&distance known=1 unit=&unit"); // https://github.com/stardist/stardist-imagej/issues/10

// segment cells
run("Dilate Labels", "radius=&nucleusDilationPixels");
run("Remove Border Labels", "left right top bottom");
rename("cells-labels");
//run("Set Scale...", "distance=&distance known=1 unit=&unit"); // https://github.com/ijpb/MorphoLibJ/issues/55
run("Analyze Regions", "area centroid");

// segment golgi
selectWindow("golgiChannel");
run("Duplicate...", "golgi-binary");
run("Gaussian Blur...", "sigma=1");
run("Auto Threshold", "method=Otsu white");
run("Connected Components Labeling", "connectivity=4 type=[16 bits]");
run("glasbey_on_dark");
rename("golgi-labels");

// measure golgi shape features
selectWindow("golgi-labels");
run("Analyze Regions", "area perimeter circularity euler_number equivalent_ellipse ellipse_elong. convexity max._feret geodesic tortuosity max._inscribed_disc average_thickness geodesic_elong.");
Table.rename("golgi-labels-Morphometry", "golgi-shapes");

// measure golgi parent cell index
run("Intensity Measurements 2D/3D", "input=cells-labels labels=golgi-labels max");
Table.rename("cells-labels-intensity-measurements", "golgi-parent-labels");

// merge golgi "intensity" and shape measurement tables
run("Merge Results Tables Columns", "tablenamea=golgi-shapes tablenameb=golgi-parent-labels outputtablename=golgi");

// measure mean golgi features for each cell and create new cell based table
run("Merge Child and Parent Results Tables", "parenttablename=cells-labels-Morphometry childtablename=golgi childname=Golgi parentlabelcolumn=Max aggregationmode=Mean outputtablename=cells-with-mean-golgi-features");

// inteactively inspect the output
if ( runInteractive )
{
	run("Open Intensity and Label Mask Image and MorpholibJ Results Table...", "intensityimage=golgi labelimage=cells-labels resultstabletitle=cells-with-mean-golgi-features");
}

// TODO: add derived table column: total golgi area
// TODO: what to save?

//filter rows based on Golgi Counts
Table.rename("cells-with-mean-golgi-features", "Results");
nCells=Table.size;
for (i = (nCells-1); i >=0; i--) {
    nFragments=parseInt(Table.get("Golgi_Count", i));
    if((nFragments<minGolgiCount)||(nFragments>maxGolgiCount)){
    	
        Table.deleteRows(i, i)
    }
}

//add filtered rois to RoiManager
roiManager("reset");
selectWindow("cells-labels");

nCells
 = Table.size;
for (i = 0; i < nCells; i++) {
    label=parseInt(Table.getString("Label", i));
    setThreshold(label, label);
    run("Create Selection");
    roiManager("Add");
}
resetThreshold();

selectWindow("origin");
roiManager("Show All");
//saveAs("Tiff", resultname + ".tif");

if(closeIntermediateImages){
    closeAllImagesExceptOrigin();
}
function closeAllExceptOrigin()
{
    //run("Close All");
    images=getList("image.titles");
    for (i = 0; i < images.length; i++) 
    {
        
        if(images[ i ]!="origin"){
            close( images[ i ] );
        }
    }

    roiManager("reset");
    windows = getList("window.titles");
    for (i = 0; i < windows.length; i++) 
    { 
    
         if(windows[ i ]!="ROI Manager"){
            close( windows[ i ] );
         }
    }
}

function closeAllImagesExceptOrigin()
{
    //run("Close All");
    images=getList("image.titles");
    for (i = 0; i < images.length; i++) 
    {
        
        if(images[ i ]!="origin"){
            close( images[ i ] );
        }
    }
}
