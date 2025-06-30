---
title:  Image data integrity
layout: module
tags: ["draft"]
---

#### Prerequisites

- A computer with an image analysis software (e.g. [Fiji](www.fiji.sc)) already installed.
- Basic knowledge of how to use above software, e.g.
    - open and save images
    - change image display settings
    - subtract a value from every pixel in an image
- Please download the training [material](https://git.embl.de/grp-bio-it/image-analysis-training-resources/-/archive/master/image-analysis-training-resources-master.zip)
- Please make sure you can access to this [document](https://git.embl.de/grp-bio-it/image-analysis-training-resources/blob/master/workshops/image-ethics-and-data-integrity.md#image-ethics-and-data-integrity).

#### Duration

1.5 hours

#### Learn more about image data integrity

- http://www.imagedataintegrity.com/about.html
- http://jcb.rupress.org/content/166/1/11.full
- Douglas W. Cromey
	- Digital Images Are Data: And Should be Treated as Such
	- ...and follow up publications...

## Image data integrity

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    image_data_integrity -> image_content [label="  preserving"];
    image_content -> pixel_values;
    image_content -> pixel_coordinates;
    pixel_coordinates -> array_indices;
    pixel_coordinates -> physical_coordinates;
 }
'/>


## Image data saving

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    saving_images -> image_content [label="  can change"];
  }
'/>

### Motivation

Sometimes it can be necessary to save your images in a different formats.
It needs some training to know how to do this properly.

What could be good reasons to resave your data in a different format (multiple answers)?

1. I want to share my scientific findings on twitter, thus I need to convert an image to a twitter compatible format.
2. I want to import images in PowerPoint, only some formats will work.
3. I need to save disk space, thus I need to find a format that makes the images smaller.
4. I want to use a special software that only accepts certain image data formats.
5. The journal I want to publish in, only accepts certain image formats.
6. I want to have everything in Tiff format, because this is the standard.
7. My boss says that (s)he cannot open .lif (Leica) or .czi (Zeiss) images, thus I should save them in a different format.


### Activity: Save an image

- Open image: `xy_calibrated_16bit__cells_eres_noisy.tif`
- Note down the value and coordinate of the pixel at [218, 332]
- Save the image in **jpg** format
- Reopen the image
- Compare the value and coordinate of the pixel at [218, 332] to your notes, did it change?

Repeat above workflow, but

- adjust the image display before saving
- save as **png**
- open `xy_float__nuclei_probability.tif` and save as **png**

### Formative assessment

What can I do to preserve image integrity during image saving (multiple answers)?

1. I always save in Tiff format, this is safe.
2. I always check pixel values and coordinates before and after saving.
3. I ask my colleagues in the lab and do what they recommend..
4. I keep a copy of the raw data.


## Image display adjustment

### Motivation

Images are a collection of numbers. To visualise those numbers one needs to decide how to map them onto a color and a brightness. There is no default way of doing this. Thus one has be educated and thoughful about this topic. In fact, it is one of the great responsibilties of a microscopist to ajust the image display settings proplery.

### Image display concept map

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    image_content -> numbers [label="  contains"];
    numbers -> image_display [label="  lookup table (LUT)"];
  }
'/>

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    lookup_table_settings -> scientific_message [label="  affects"];;
    lookup_table_settings -> no_default;
  }
'/>

### Activity: Quantitative image display

- Open image: `xy_calibrated_16bit__nuclear_protein_control.tif`
    - This image shows a nuclear protein in control cells.
- Open image: `xy_calibrated_16bit__nuclear_protein_treated.tif`
    - The cells in this image have been subjected to a drug.
- Inspect the images:
    - Did the drug affect the amount of the nuclear protein?
- Adjust the lookup-tables (LUTs) of both images to be the same
- Add a LUT calibration to both images

### Formative Assessment

What helps to scientifically convey image intensity information (multiple answers)?

1. Adjust the LUT to the image's full bit-depth.
2. Add a LUT calibration bar.
3. Use the same LUT for images acquired with same settings..
4. Never change the LUT of images! Always keep as in raw data.

## High dynamic range image display

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    biological_images -> high_dynamic_range [label="  "];
    paper_reflectance -> low_dynamic_range [label="  "];
    computer_monitors -> low_dynamic_range [label="  "];
  }
'/>

### Motivation

The number range in images of biological samples can cover large ranges.
For example, a GFP tagged protein could occur in the same cell at different locations either 1 or 10000 times. This means that the dynamic range can be 10^4 or more. Due to limitations of image display and image preception such large dynamics ranges are difficult to display.


### Activity: High dynamic range image display

- Open image: `xy_16bit__nuclei_high_dynamic_range.tif`
- Try to adjust the grayscale LUT such that everything can be seen...
- Try finding other LUTs that help showing all data
- Add LUT calibration to image

### Formative Assessment

What can you do to show images with a high dynamic range (multiple answers)?

1. Adjust the LUT such that only the scientifically relevant information can be seen.
2. Adjust the LUT such that only the scientifically relevant information can be seen
	* and state that the LUT has been adjusted in the figure legend
	* and show the same image with other LUT settings in the supplemental material.
3. Try to find a LUT that shows all data.
4. Never use multi color LUTs, they are confusing.
5. Already on the  microscope change the settings such that only relevant structures are visible, e.g. lower the gain such that dark irrelevant objects have zero pixel values.
6. Adjust LUT settings such that background noise is not visible, because this is distracting.
7. Add a LUT calibration to the image, such that readers can see that not all information might be visible.


## Image math

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    image_math -> pixel_values [label="  changes"];
    image_math -> pixel_data_type [label="  does not change"];
    image_math -> wrong_pixel_values [label = "  can yield"]
  }
'/>

### Motivation

It sometimes is necessary to change numberic content of images. It is important to understand how to do this properly in order to avoid uncontrolled artifacts.

What are good reasons to change the pixel values in an image?

1. For intensity measurements, the image background (e.g. camera based offset) should be subtracted from all pixels.
2. For threshold based image segmentation (object detection), it helps to first filter noise in the image.
3. For intensity measurements, it helps to filter noise in the image.
4. The image appears to dark, multiplication of all pixels by a constant number is a means to make it brighter.
5. For uneven illumination (e.g. occuring in wide-field microscopy with large camera chips), one should do flat-field correction, which makes the intensity values even across the image.
6. Our microscope was broken. We took images on a replacement microscope. The pixel values were consistently higher than on our usual microscope. We multiplied the pixels on all images from the replacement microscope by a constant factor to make them comparable to our usual data.


### Activity: Perform pixel based background subtraction

- Open image: `xy_8bit__nuclei_noisy_different_intensity.tif`
- Appreciate the significant background intensity
- Measure pixel value at `[ 28, 35 ]` and `[ 28, 39 ]`
- Measure background intensity in below region:
	- upper left corner at `[ 20, 35 ]`
	- width = 10
	- height = 10
- Subtract the measured background intensity from each pixel
- Measure pixel values again at above coordinates ( `[ 28, 35 ]` and `[ 28, 39 ]` )
- Discuss how the pixel values changed during background subtraction

Repeat above activity, but:

- After opening the image, convert its pixel data type to floating point

### Formative Assessment

Considering image math operations, which of below statements is correct
(multiple answers)?

1. Never change the pixel data type, because it violates image integrity.
2. Changing the pixel data type does not change pixel values.
3. It is scientifically unethical to perform mathematical operations on images, because it changes the pixel values.
4. When performing mathematical operations on images, it should be documented (e.g. by a script of code)


## Display of 3-D images

Biological images are often 3D. However paper and monitors can only show 2D images. It is thus important to understand how to show 3D images in 2D without compromising the scientific message.

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    _3D_data -> visualisation [label="  multiple options"];
    visualisation -> scientific_message [label="  affects"];
  }
'/>


<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    _3D_visualisation -> sum_projection;
    _3D_visualisation -> max_projection;
    _3D_visualisation -> slice_animation;
    _3D_visualisation -> slice_gallery;
    _3D_visualisation -> ...;
  }
'/>


### Activity: Explore 3D visualisations

- Open image: `xyzt_calibrated_16bit__golgi_bfa.zip`
- Explore and discuss different options how to present this data
    - slice gallery
    - sum projection
    - max projection
    - slice animation

### Formative Assessment

Which statements about visualisation and quantification of 3D images are correct (multiple answers)?

1. Always use maximum intensity projection, it is by far the most commonly used.
2. Any visualisation can make sense, you just have scientifically justify it.
3. Intensity quanitifcations ideally should be done in 3D, not in projections.
4. It is impossible to quantify intensities in projections.
