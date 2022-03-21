# import classes
from ij import IJ, ImagePlus, WindowManager
from ij.io import FileSaver
from ij.plugin.filter import ParticleAnalyzer
from ij.plugin.frame import RoiManager
from ij.measure import ResultsTable, Measurements
from ij.process import ImageProcessor
import os

# Specify an output directory
outputDir = FIXME

# Specify size parameters for object selection 
min_size = 0
max_size = 2000

# Initialize Roi Manager and empty results table, close other open images
rm = RoiManager().getInstance()
rm.reset()
IJ.run("Close All")

# Open binary shapes image
shapes = IJ.openImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary_randomshapes.tif")

# Configure and run particle analyzer
results = ResultsTable() # construct empty resultstable
pa = ParticleAnalyzer((ParticleAnalyzer.ADD_TO_MANAGER + ParticleAnalyzer.SHOW_ROI_MASKS),(Measurements.AREA + Measurements.CENTROID + Measurements.CENTER_OF_MASS + Measurements.PERIMETER + Measurements.RECT), results, min_size, max_size, 0, 1)
pa.analyze(shapes) # run the particle analyzer on the image
results.show("Results")

# Save results, label mask, and ROIs
results.save(os.path.join(outputDir, "shapes_results_jython.txt")) # save results table

labelMask = WindowManager.getImage("Count Masks of xy_8bit_binary_randomshapes.tif")
IJ.run(labelMask, "Glasbey", "") # set glasbey LUT
FileSaver(labelMask).saveAsTiff(os.path.join(outputDir, "shapes_labels_jython.tif")) # save the label mask

rm.runCommand("Save", os.path.join(outputDir, "shapes_ROIset_jython.zip")) # save the ROIs
