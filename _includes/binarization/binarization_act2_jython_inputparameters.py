#@ Integer (label="Lower threshold") thr1
#@ Integer (label="Upper threshold") thr2

from ij import IJ, ImagePlus
from ij.plugin import Thresholder
nputImage = IJ.openImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__PCNA.tif")
IJ.setRawThreshold(inputImage, thr1, thr2, None)
binaryImage = ImagePlus('Thresholded image', Thresholder.createMask(inputImage))
binaryImage.show()
