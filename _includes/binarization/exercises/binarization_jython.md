Use imageJMacro to create 3 binary images from *xy_8bit_PCNA.tif* where 
1. 2 foreground nuclei.
2. only the boundary of the 2 nuclei
3. only the bright dots remain

> ## Solution
> ```python
> from ij import IJ, ImagePlus
> from ij.plugin import Thresholder
> # image is xy_8bit__two_cells.tif
> inputImage = IJ.getImage() #get Current open Image
> IJ.setRawThreshold(inputImage, 5, 255, None)
> binaryImage = ImagePlus('Binary image 2 nuclei', Thresholder.createMask(inputImage))
> binaryImage.show()
> IJ.setRawThreshold(inputImage, 4, 4, None)
> binaryImage_boundary = ImagePlus('Binary boundary', Thresholder.createMask(inputImage))
> binaryImage_boundary.show()
> IJ.setRawThreshold(inputImage, 44, 255, None)
> binaryImage_brightdots = ImagePlus('Binary bright dots', Thresholder.createMask(inputImage))
> binaryImage_brightdots.show()
> ```
{: .solution}

> ## Solution with input parameters
> ```python
> #@ Integer
> from ij import IJ, ImagePlus
> from ij.plugin import Thresholder
> # image is xy_8bit__two_cells.tif
> inputImage = IJ.getImage() #get Current open Image
> IJ.setRawThreshold(inputImage, 5, 255, None)
> binaryImage = ImagePlus('Binary image 2 nuclei', Thresholder.createMask(inputImage))
> binaryImage.show()
> IJ.setRawThreshold(inputImage, 4, 4, None)
> binaryImage_boundary = ImagePlus('Binary boundary', Thresholder.createMask(inputImage))
> binaryImage_boundary.show()
> IJ.setRawThreshold(inputImage, 44, 255, None)
> binaryImage_brightdots = ImagePlus('Binary bright dots', Thresholder.createMask(inputImage))
> binaryImage_brightdots.show()
> ```
{: .solution}