Open image [xy_8bit__PCNA.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__PCNA.tif) and 
1. Find a threshold value so that there are 2 foreground nuclei.
2. Find a threshold value so that only the bright dots remain
3. Find threshold interval so that only the boundary of the nuclei remains.


> ## Solution
> ```python
> from ij import IJ, ImagePlus
> from ij.plugin import Thresholder
> # image is xy_8bit_PCNA.tif
> inputImage = IJ.openImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__PCNA.tif")
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
> #@ Integer (label="Lower threshold") thr1
> #@ Integer (label="Upper threshold") thr2
>
> from ij import IJ, ImagePlus
> from ij.plugin import Thresholder
> # image is xy_8bit_PCNA.tif should be already open
> inputImage = IJ.openImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__PCNA.tif")
> IJ.setRawThreshold(inputImage, thr1, thr2, None)
> binaryImage = ImagePlus('Thresholded image', Thresholder.createMask(inputImage))
> binaryImage.show()
> ```
{: .solution}