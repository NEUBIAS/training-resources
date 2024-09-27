""" Open a multidimensional image and crop out the green bead. Then reslice it from the top """

# import packages
from ij import IJ
from ij.plugin import Duplicator

# Close other open images
IJ.run("Close All")

# open image
spheres = IJ.openImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit_spheres.tif")
spheres.show()

# crop out the green sphere
spheres.setRoi(23,7,18,18)
green_sphere = Duplicator().run(spheres, 2, 2, 3, 11, 1, 1) # int firstC, int lastC, int firstZ, int lastZ, int firstT, int lastT)
green_sphere.setTitle("Green sphere")
green_sphere.show()

# Reslice green sphere from the top, WITH interpolation
IJ.run(green_sphere, "Reslice [/]...", "output=2.000 start=Top rotate");
green_sphere_top = IJ.getImage()
green_sphere_top.setTitle("Green sphere viewed from the top, WITH interpolation")
green_sphere_YZ_interpolated = Duplicator().run(green_sphere_top, 5, 5) # first Z, last Z
green_sphere_YZ_interpolated.setTitle("green_sphere_YZ_interpolated")
green_sphere_YZ_interpolated.show()

# Reslice green sphere from the top, WITHOUT interpolation
green_sphere_top2 = IJ.run(green_sphere, "Reslice [/]...", "output=2.000 start=Top rotate avoid")
green_sphere_top2 = IJ.getImage()
green_sphere_top2.setTitle("Green sphere viewed from the top, WITHOUT interpolation")
green_sphere_YZ_NOTinterpolated = Duplicator().run(green_sphere_top2, 10, 10) # first Z, last Z
green_sphere_YZ_NOTinterpolated.setTitle("green_sphere_YZ_NOTinterpolated")
green_sphere_YZ_NOTinterpolated.show()

IJ.run("Tile")