from ij import IJ, ImagePlus
from ij.plugin import Thresholder
# image is xy_8bit_PCNA.tif
inputImage = IJ.openImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__PCNA.tif")
IJ.setRawThreshold(inputImage, 5, 255, None)
binaryImage = ImagePlus('Binary image 2 nuclei', Thresholder.createMask(inputImage))
binaryImage.show()
IJ.setRawThreshold(inputImage, 4, 4, None)
binaryImage_boundary = ImagePlus('Binary boundary', Thresholder.createMask(inputImage))
binaryImage_boundary.show()
IJ.setRawThreshold(inputImage, 44, 255, None)
binaryImage_brightdots = ImagePlus('Binary bright dots', Thresholder.createMask(inputImage))
binaryImage_brightdots.show()
