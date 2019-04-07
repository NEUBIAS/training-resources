# Bioimage analysis fundamentals

## Pixel values, coordinates, and data types

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    image -> pixel [label="  has many"];
    pixel -> value;
    pixel -> indices;
    pixel -> coordinates;
    indices -> calibration;
    calibration -> coordinates;
    image -> calibration [label="  can have"];
    pixel -> voxel [label="  3D"];   
  }
'/>

### Activity

* Open image: xy_8bit__nuclei_noisy_different_intensity.tif
	* Explore different ways to inspect pixel values and indices
	* Add image calibration
	* Check where the calibration is visible
	
### Formative assessment

True or false?

* Pixel coordinates are always integer values.
* Changing the image calibration changes the pixel values.
* Pixel coordinates depend on image calibration.
* Pixel indices are always positive integer values.
* The lowest pixel index of a 2D image always is `[1,1]`.
* When looking at a 2D image, the lowest pixel index is in the lower left corner.

&nbsp;

&nbsp;

&nbsp;

<div style="page-break-after: always;"></div>

## Image display

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    LUT -> color;
    LUT -> brightness;
    min -> LUT;
    max -> LUT;
    value -> LUT;
  }
'/>

```
brightness = ( value - min ) / ( max - min )

0 <= brightness <= 1 

contrast = max - min 
``` 

### Activity

* Open image: xy_8bit__nuclei_noisy_different_intensity.tif
* Explore different LUTs and LUT settings
	* Appreciate that LUT settings do not affect image content.


### Formative Assessment

Fill in the blanks, using those words: decrease, larger_than, increase, smaller_than 

* Pixels with values _____ `max` will appear saturated. 
* Decreasing `max` while keeping `min` constant will _____ the contrast.
* Decreasing both `max` and `min` will _____ the overall brightness.
* Pixels with values _____ the `min` will appear black, when using a grayscale LUT.


&nbsp;

&nbsp;

&nbsp;



## Image math and pixel data types

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    "data type" -> "pixel values" [label="  restricts"];
    "image math" -> "pixel values" [label="  changes"];
    "N-bit unsigned integer" -> "0, 1, ..., 2^N-1";
    "data type" -> float -> "..., -1031.0, ..., 10.5, ...";
    "data type" -> "...";
    "data type" -> "N-bit unsigned integer";
  }
'/>

### Activity: Pixel based background subtraction

* Open image: xy_8bit__nuclei_noisy_different_intensity.tif
* Appreciate the significant background intensity
* Measure pixel values at `[ 28, 35 ]` and `[ 28, 39 ]`
* Measure the image background intensity in this region:
    * upper left corner at `[ 20, 35 ]`
    * width = 10
    * height = 10
* Subtract the measured background intensity from each pixel.
* Measure the pixel values again. 
* Observe that the resuls are incorrect.

Repeat above activity, but:

* After opening the image, convert its data type to floating point.

### Activity: Explore the limitations of `float` data type

* Create an empty image
* Set all pixel values to 1000000000.0
* Add 1.0 to all pixel values
* Be shocked...

...it turns out that from 16777216 on you cannot represent all integers anymore within a float. 

### Formative Assessment

True or false?

* Subtracting 100 from 50 in a 8-bit image will result in -50.
* Adding 1 to 255 in a 8-bit image will result in 256.
* Subtracting 10.1 from 10.0 in a float image will result in -0.1
* Adding 1.0 to 255.0 in a float image will result in 256.0
* Adding 1000.0 to 1000000000.0 in a float image will result in 1000001000.0

### Learn more

* [Limitations of float](https://randomascii.wordpress.com/2012/02/13/dont-store-that-in-a-float/)

&nbsp;

&nbsp;

&nbsp;

## Pixel data type conversions

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    "data type conversion" -> "values" [label="  can change"];
    "data type conversion" -> "value range" [label="  changes"];
  }
'/>

### Activity: 16-bit to 8-bit conversion

* Open image: xy_16bit__two_values.tif
* Convert to 8-bit
* Understand the mathematics underlying the conversion from 16-bit to 8-bit.

### Activity: 16-bit to float conversion

* Open image: xy_16bit__two_values.tif
* Convert to float

### Formative Assessment

True or false? Discuss with your neighbor!

1. Changing pixel data type never changes pixel values.
2. Converting from 16-bit unsigned integer to float never changes the pixel values.
3. Changing from float to 16-bit unsigned integer never changes the pixel values.
4. There is only one correct way to convert from 16-bit to 8-bit.

&nbsp;

&nbsp;

&nbsp;

## Thresholding

In order to find objects in a image, the first step often is to determine whether a pixel is part of an object (foreground) or of the image background. In fluorescence microscopy this often can be achieved by thresholding.

<img src='https://g.gravizo.com/svg?
 digraph G {
	shift [fontcolor=white,color=white];
	"intensity image" -> threshold;
	threshold -> "binary image";
	"binary image" -> "mask" [label="  aka"];
	"binary image" -> "background value";
	"binary image" -> "foreground value";
	"background value" -> "0";
	"foreground value" -> "1";
	"foreground value" -> "255";
	"pixel value" -> ">= threshold" -> foreground;
	"pixel value" -> "< threshold" -> background;
 }
'/>

### Activity: Threshold an image

* Open image: xy_8bit__two_cells.tif
* Convert the image to a binary image by means of thresholding.

### Formative assessment

True or false? Discuss with your neighbour!

* For each image there is only one correct threshold value.
* The result of thresholding is a binary image.
* A binary image can have three values: `-1, 0, +1`
* Values below the threshold are always set to `1`.

&nbsp;

&nbsp;

&nbsp;


## Connected components analysis

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    "intensity image" -> "connected component analysis" -> "label image";
    connectivity -> "connected component analysis"; 
  }
'/>


### Activity: 2D connected components analysis

* Open image: xy_8bit_binary__nuclei.tif
* Perform connected components analysis
* Explore multi-color LUTs for object labelling
* Explore removing and joining labels


### Activity: 3D connected components analysis

Repeat above activity but use a 3D image:

* Open image: xyz_8bit_binary__spots.tif

### Formative assessment

Fill in the blanks, using these words: less, more, 8, 255, 4, more.

* For a given input image there is only one correct connectivity.
* In 3D, pixels have _____ neighbors than in 2D.
* 8-connected connectivity results in _____ objects than 4-connected connectivity.
* In 3D, pixels have ____ non-diagonal neighbors.
* In 2D, pixels have ____ non-diagonal neighbors.
* A 8-bit label image can maximally have _____ objects.
* The maximum value in a label image is equal to or _____ than the number of objects.


&nbsp;

&nbsp;

&nbsp;


## Shape measurements

<img src='https://g.gravizo.com/svg?
 digraph G {
	shift [fontcolor=white,color=white];
	"label image" -> shape_analysis -> table;
	table -> object_rows;
	table -> feature_columns;
	table -> visualisation;  
}
'/>


### Activity: Measure object shape parameters

* Open image: xy_8bit_labels__four_objects.tif
* Perform shape measurements and discuss their meanings.
* Explore results visualisation
	* Color objects by their measurement values.
* Add a calibration to the image and check which shape measurements are affected.
* Draw a test image to understand the shape measurements even better.

### Formative assessment

True or false? Discuss with your neighbour!

* Circularity is independent of image calibration.
* Area is independent of image calibration.
* Perimeter can strongly depend on spatial sampling.
* Volume can strongly depend on spatial sampling.
* Drawing test images to check how certain shape parameters behave is a good idea.

### Learn more

* Especially surface and perimeter measurements are affected by sampling and resolution, see for example:
	* https://en.wikipedia.org/wiki/Coastline_paradox).
* Results visualisation:
	* https://imagej.net/MorphoLibJ#Grayscale_morphological_filters: **Label visualization in 3D viewer**


&nbsp;

&nbsp;

&nbsp;


## Object shape measurement workflow

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    "intensity image" -> "binary image" [label="  threshold"];
    "binary image" -> "label image" [label="  connected components"];
    "label image" -> table [label="  measure_shape"];
}
'/>

### Activity: Segment objects and measure shapes

* Open image: xy_8bit__two_cells.tif
* Segment the cells and measure their shapes.
	* Devise code to automate the workflow.

### Formative assessment

Fill in below blanks, using these words: equal_to, larger_than, smaller_than, binary, connected_component_analysis, thresholding

* A label image is the result of _____ .
* The number of pixels in a binary image is typically _____ the number of connected components. 
* The number of distinct values in a label image is _____ the number of objects (minus one).
* Converting an intensity image to a _____ image can be achieved by _____ .
* The number of connected components can be _____ the maximal label.

&nbsp;

&nbsp;

&nbsp;


## Intensity measurements

### Activity: Measure intensities in image regions

* Open image: xy_float__h2b_bg_corr.tif
* Measure for both nuclei:
	* Maximum intensity
	* Average intensity
	* Median intensity
	* Sum intensity
* Discuss the interpretation!
* Discuss where to measure!


### Activity: Intensity measurements without pixel based background correction

#### Motivation

There are several good reasons not to subtract the background from each pixel in an image: 

* It is a bit tricky to do it right, because one has to convert to float to accomodate floting point and negative values.
* If one has really big image data (TB) one would need (at least) another TB storage for the background corrected version of the image.

#### Workflow

* Open image: xy_calibrated_8bit__two_nuclei_high_background.tif
* Measure for both nuclei and a background region:
	* Maximum intensity
	* Average intensity
	* Median intensity
	* Sum intensity
* Discuss how to correct the intensities for the background
	* Appreciate that you also need the region areas for this task
	* Measure the region areas
		* Watch out: the image is calibrated!
		* Use the area for the correction.

### Formative assessment: Intensity measurements

Fill in the blanks, using these words: integrated, mean, number_of_pixels, decrease, increase, sum

* Average intensity is just another word for _____ intensity.
* The _____ intensity is equal to the mean intensity times the _____ in the measured region.
* In an 8-bit image, increasing the size of the measurement region can only _____ the sum intensity.
* In a float image, increasing the size of the measurement region can _____ the sum intensity. 

&nbsp;

&nbsp;

&nbsp;


## Convolution filters

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    "intensity image" -> "convolution" -> "filtered image";
    "small image" -> size;
    "small image" -> "pixel values";
    "kernel" -> "small image" [label="  is"]; 
    "kernel" -> "convolution";
}
'/>

### Activity: Explore convolution filters

* Open image: xy_8bit__nuclei_noisy_different_intensity.tif
* Try the result of different convolution filters, e.g.
	* https://en.wikipedia.org/wiki/Kernel_(image_processing)
	* Mean filter
	* Gaussian blur
	* Edge detection
* Appreciate that the results are (slightly) wrong within the 8-bit range of the input image.

### Activity: Use mean filter to facilitate image segmentation

* Open image: xy_8bit__nuclei_noisy_different_intensity.tif
* Appreciate that you cannot readily threshold the image
* Apply a mean filter
* Threshold the filtered image

### Formative assessment

* Draw the kernel of a 3x3 mean filter.
* Draw three different kernels that enhance edges.
 
### Learn more

* https://en.wikipedia.org/wiki/Kernel_(image_processing)


&nbsp;

&nbsp;

&nbsp;


## Typical image analysis workflow

![image](/uploads/b4bdce17515908f40d858b35d5e9256e/image.png)

&nbsp;

&nbsp;

&nbsp;




