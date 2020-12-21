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
> IJ.setRawThreshold(inputImage, 44, 255, None)
> binaryImage = ImagePlus('Binary image 2 nuclei', Thresholder.createMask(inputImage))
> binaryImage.show()
> IJ.setRawThreshold(inputImage, 88, 255, None)
> binaryImage_1 = ImagePlus('Binary image 1 nuclei', Thresholder.createMask(inputImage))
> binaryImage_1.show()
> ```
{: .solution}


#### Exercise 2

What is the solution to the second exercise?

<details>
<summary>Solution</summary>
This is the solution to the second exercise.
</details>
