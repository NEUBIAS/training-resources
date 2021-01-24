from ij import IJ, ImagePlus
from ij.plugin import Thresholder

inputImage = IJ.openImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_two_cells.tif")
IJ.setRawThreshold(inputImage, 44, 255, None)
binaryImage = ImagePlus('Binary image 2 nuclei', Thresholder.createMask(inputImage))
binaryImage.show()
IJ.setRawThreshold(inputImage, 88, 255, None)
binaryImage_1 = ImagePlus('Binary image 1 nuclei', Thresholder.createMask(inputImage))
binaryImage_1.show()
