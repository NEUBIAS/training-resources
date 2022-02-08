""" Open the head image stack and reslice it to view it from different angles (side, top, and front) """

# import classes
from ij import IJ
from ij.plugin import Slicer

# Close other open images
IJ.run("Close All") 

# open head image stack
head = IJ.openImage("http://imagej.net/images/t1-head.zip")
head.show() # shows head from the side
head.setTitle("Head viewed from the side")

# Reslice the head image stack to view the head from the top and from the side
IJ.run(head, "Reslice [/]...", "output=1.500 start=Top") # view head from the top 
head_top = IJ.getImage()
head_top.setTitle("Head viewed from the top")
IJ.run(head, "Reslice [/]...", "output=1.500 start=Left rotate") # view head from the front
head_front = IJ.getImage()
head_front.setTitle("Head viewed from the front")

IJ.run("Tile")