Adapt the below code to change the following:
1. Save the results table as comma-separated data table instead of text-delimited data.
2. Save the output label image in a different image format (e.g. PNG, JPEG).
3. When running the code, try to specify different output directories.

> ## Solution
> ```
># import classes
>from ij import IJ, ImagePlus, WindowManager
>from ij.io import FileSaver
>from ij.plugin.filter import ParticleAnalyzer
>from ij.plugin.frame import RoiManager
>from ij.measure import ResultsTable, Measurements
>from ij.process import ImageProcessor
>import os
>
>#@String outputdir
>
># specify settings
>min_size = 100
>max_size = 500
>min_circ = 0.5
>max_circ = 1
>
># Initialize Roi Manager and empty results table, close other open images
>rm = RoiManager().getInstance()
>rm.reset()
>IJ.run("Close All")
>
># create blob mask
>blobs = IJ.openImage("http://imagej.net/images/blobs.gif")
>blobs.getProcessor().setAutoThreshold("Default", 1, 1)
>blobs_mask = ImagePlus("blobs mask", blobs.getProcessor().createMask())
>blobs_mask.show()
>
># Configure and run particle analyzer
>results = ResultsTable() # construct empty resultstable
>pa = ParticleAnalyzer((ParticleAnalyzer.ADD_TO_MANAGER + ParticleAnalyzer.SHOW_ROI_MASKS),(Measurements.AREA >+ Measurements.CENTROID + Measurements.CENTER_OF_MASS + Measurements.PERIMETER + Measurements.RECT), >results, min_size, max_size, 0.5, 1)
>pa.analyze(blobs_mask) # run the particle analyzer on the image
>results.show("Results")
>
># Save results, label mask, and ROIs
>results.save(os.path.join(outputdir, "blob_results_jython.csv")) # save results table
>
>labelmask = WindowManager.getImage("Count Masks of blobs mask")
>IJ.run(labelmask, "Glasbey", "") # set glasbey LUT
>FileSaver(labelmask).saveAsPng(os.path.join(outputdir, "blob_labels_jython.png")) # save the label mask
>
>rm.runCommand("Select All")
>rm.runCommand("Save", os.path.join(outputdir, "blob_ROIset_jython.zip")) # save the ROIs
> ```
{: .solution}
