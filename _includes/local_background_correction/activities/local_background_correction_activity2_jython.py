# Use a maximum intensity projection for background subtraction

# import packages
from ij import IJ
from ij.plugin import ZProjector, ImageCalculator

# open image
imp = IJ.openImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyt_8bit_polyp.tif")

# create maximum intensity projection
maxproj = ZProjector().run(imp, "max all")

# subtract maximum intensity projection from original image
background_subtracted = ImageCalculator().run(imp, maxproj, "Subtract create 32-bit stack")

# show all images
imp.show()
maxproj.show()
background_subtracted.show()
IJ.run("Tile")