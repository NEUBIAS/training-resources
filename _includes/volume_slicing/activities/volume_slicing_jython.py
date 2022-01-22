""" Open a multidimensional image and inspect its dimensions using orthogonal views """

# import packages
from ij import IJ
from ij.plugin import Duplicator

# Close other open images
IJ.run("Close All")

# open image
beads = IJ.openImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit_beads_p_open.tif")
beads.show()

# crop out the green bead
beads.setRoi(118,142,37,37)
green_bead = Duplicator().run(beads, 1, 1, 15, 25, 1, 1) # int firstC, int lastC, int firstZ, int lastZ, int firstT, int lastT)
green_bead.setTitle("Green bead")
green_bead.show()

# Reslice green bead from the top, WITH interpolation
IJ.run(green_bead, "Reslice [/]...", "output=0.100 start=Top");
green_bead_top = IJ.getImage()
green_bead_top.setTitle("Green bead viewed from the top, WITH interpolation")

# Reslice green bead from the top, WITHOUT interpolation
green_bead_top2 = IJ.run(green_bead, "Reslice [/]...", "output=0.100 start=Top avoid")
green_bead_top2 = IJ.getImage()
green_bead_top2.setTitle("Green bead viewed from the top, WITHOUT interpolation")

IJ.run("Tile")