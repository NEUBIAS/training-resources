---
title:     Data types
layout:    module

prerequisites:
  - "[Basic properties of images and pixels](../pixels)"

objectives:
  - "Understand that images have a data type which limits the values that the pixels in the image can have."
  - "Understand common data types such as 8-bit and 16-bit unsigned integer."

motivation: |
  Images contain numerical values that must be somehow stored on the hard disc or within the computer memory. To do so, for each pixel a certain amount of space (memory) must be allocated (usually measure in bits). Generally, the more bits you allocated the bigger are the numbers that you can store, however you also need more space. Thus chosing the right data type usually is a balance between what you can represent and how much space you want to afford for this. Especially for large image data such as volume EM and light-sheet data the choice of the data type can have quite some impact on your purse. In addition, certain operations on images can yield results that yield values outside of the original data type; this is a serious and frequently occurring source of mistakes when handling image data and thus must be well understood!

concept_map: >
  graph TD
    DT("Data type") -->|limits|PV("Pixel values")
    DT -->|has|BD("Bit depth / interpretation")
    BD -->|e.g.|8("8-bit / unsigned integer")
    BD -->|e.g.|16a("16-bit / unsigned integer")
    BD -->|e.g.|16b("16-bit / signed integer")
    BD -->|e.g.|16c("16-bit / half-precising floating-point")


figure: /figures/data_types.png
figure_legend: Examples for data types of different bit depths.

activity_preface: |

  Open the following images and discuss (i) their data type, and (ii) whether there are any signs of intensity clipping.
  - [xy_8bit__nuclei_noisy_different_intensity.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif)
  - [xy_8bit__nuclei_clipping_issue_a.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_clipping_issue_a.tif)
  - [xy_8bit__nuclei_clipping_issue_b.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_clipping_issue_b.tif)
  - [xy_16bit__autophagosomes.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif)
  - [xy_8bit__two_spots_noisy_uneven_background.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_spots_noisy_uneven_background.tif)
  - [xy_8bit_binary__two_objects.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_spots_noisy_uneven_background.tif)
  - [xy_16bit__scanR_datatype_issue.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__scanR_datatype_issue.tif)


activities:

exercises:

assessment: >

  ### True or false? Discuss with your neighbor!

    1. Changing pixel data type never changes pixel values.
    2. Converting from 16-bit unsigned integer to 32-bit floating point never changes the pixel values.
    3. Changing from 32-bit floating point to 16-bit unsigned integer never changes the pixel values.
    4. There is only one correct way to convert from 16-bit to 8-bit.
    5. If the highest value in an image is 255 I can conclude that it is an 8-bit unsigned integer image.
    6. If the highest value in an image is 1034 I can conclude that it is not an 8-bit unsigned integer image.
    7. If the bit-depth is 16 and there are a lot of neighboring pixels with the value 4095 and no pixels with a higher value, most likely this image was acquired with 12 bit camera. 

    > ## Solution
    > 1. False
    > 2. True
    > 3. False
    > 4. False
    > 5. False
    > 6. True
    > 7. True
    {: .solution}

learn_next:

external_links:
  - "[Bit depth](https://petebankhead.gitbooks.io/imagej-intro/content/chapters/bit_depths/bit_depths.html)"
  - "[Wikipedia: Integer data type](https://en.wikipedia.org/wiki/Integer_(computer_science))"
  - "[Floating points in binary notation](http://www.davdata.nl/math/floatingpoint.html)"
  - "[Floating points explained](https://en.wikibooks.org/wiki/A-level_Computing/AQA/Paper_2/Fundamentals_of_data_representation/Floating_point_numbers)" 
  - "[Wikipedia: Half-precision floating-point format](https://en.wikipedia.org/wiki/Half-precision_floating-point_format)"

---

### Image data types

The image data type limits the values that pixels can take. 

For unsigned N-bit integer images, the range is 0 to 2^(N-1).

Important examples are:
  - 8-bit unsigned integer: 0 - 255
  - 12-bit unsigned integer: 0 - 4095
  - 16-bit unsigned integer: 0 - 65535

### Intensity clipping (saturation)

If pixels take on values on the edges of those ranges you cannot know for sure whether you lost information at some point in the process of the microscopy or data transfer and storage. For example, if there is a pixel with the value 255 in an unsigned integer 8-bit image, it may be that the actual intensity "was higher", e.g. would have corresponded to a gray value of 302. One speaks of "saturation" or "intensity clipping" in such cases. It is important to realise that there can be also clipping at the lower end of the range (some microscopes have an unfortunate "offset" slider that can be set to negative values, which can cause this).