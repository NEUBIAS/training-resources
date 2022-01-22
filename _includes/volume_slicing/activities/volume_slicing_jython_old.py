""" Open a multidimensional image and inspect its dimensions using orthogonal views """

# import packages
from ij import IJ
from ij.plugin import Orthogonal_Views

# Close other open images
IJ.run("Close All")

# open image
IJ.openImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit_beads_p_open.tif")
beads.show()

# run orthogonal views command
ov = Orthogonal_Views()
ov.imageOpened(beads)
ov.run("beads")
xz = ov.getXZImage()
yz = ov.getYZImage()
xz.show()
yz.show()
