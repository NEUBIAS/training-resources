''' This jython script opens the head image stack and reslices it to view it from different angles 
(side, top, front, and diagonal view), and then selects slices corresponding to Z=60, X=135, and Y=160. '''

# import classes
from ij import IJ, ImagePlus

# Close other open images
IJ.run("Close All")

# open head image stack
head = IJ.openImage("http://imagej.net/images/t1-head.zip")
head.show() # shows head from the side
head.setTitle("Head viewed from the side")

# get an image of the slice at Z=60
head_z60 = ImagePlus('head Z=60', head.getImageStack().getProcessor(60))
head_z60.show()

# Reslice the head image stack to view the head from the front
IJ.run(head, "Reslice [/]...", "output=1.500 start=Left rotate") # view head from the front
head_front = IJ.getImage()
head_front.setTitle("Head viewed from the front")

# get an image of the slice at original X=135
head_x135 = ImagePlus('head X=135', head_front.getImageStack().getProcessor(135))
head_x135.show()

# Reslice the head image stack to view the head from the top and from the side
IJ.run(head, "Reslice [/]...", "output=1.500 start=Top rotate") # view head from the top
head_top = IJ.getImage()
head_top.setTitle("Head viewed from the top")

# get an image of the slice at original Y=160
head_y160 = ImagePlus('head Y=160', head_top.getImageStack().getProcessor(160))
head_y160.show()

# Rotate the head stack by 45 degrees and reslice to obtain a diagonal slice
head_diagonal = head.duplicate()
IJ.run(head_diagonal, "Rotate... ", "angle=45 grid=1 interpolation=None enlarge stack") # rotate the stack
IJ.run(head_diagonal, "Reslice [/]...", "output=1.500 start=Top rotate")
head_diagonal = IJ.getImage()
head_diagonal.setTitle("Head in diagonal view")
head_diagonal.show()
head_diagonal = ImagePlus('head diagonal slice', head_diagonal.getImageStack().getProcessor(170))
head_diagonal.show()
IJ.run("Tile")
