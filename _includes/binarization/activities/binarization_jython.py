from ij import IJ, ImagePlus
from ij.plugin import Thresholder
# image is xy_8bit__two_cells.tif
inputImage = IJ.getImage() #get Current open Image
IJ.setRawThreshold(inputImage, 44, 255, None)
binaryImage = ImagePlus('Binary image 2 nuclei', Thresholder.createMask(inputImage))
binaryImage.show()
IJ.setRawThreshold(inputImage, 88, 255, None)
binaryImage_1 = ImagePlus('Binary image 1 nuclei', Thresholder.createMask(inputImage))
binaryImage_1.show()
