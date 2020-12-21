from ij import IJ, ImagePlus
from ij.plugin import Thresholder

inputImage=IJ.getImage()
IJ.setRawThreshold(inputImage, 60, 255, None)
binaryImage=ImagePlus('Binary image',Thresholder.createMask(inputImage))
binaryImage.show()
