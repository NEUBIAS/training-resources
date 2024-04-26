---
title: Digital image basics
layout: module
prerequisites:

objectives:
  - Understand that a digital image is typically stored as an N-dimensional array.
  - Learn that the image array elements are called pixels (2D) or voxels (3D).
  - Examine the values and locations of pixels/voxels in an image.

motivation: >
  Digital images are a very important subset of the more general [mathematical definition](https://mathworld.wolfram.com/Image.html) of an image. The vast majority of available algorithms and visualisation tools operate on digital images and all (as far as we know) scientific microscopes output digital images. Thus, for microscopy based science, it is crucial to understand the basic properties of digitial images and how to effectively inspect their content.


concept_map: >
  graph TD
    Im("Digital image") --- A("N-D array")
    A --- E("Elements/Pixels/Voxels")
    A --- DT("Data type")
    A --- D("Shape/Size/Dimensions")
    E --- V("Value")
    E --- I("Indices")

figure: /figures/pixels.jpg
figure_legend:  Digital image pixel array and gray-scale rendering. This array (image) has two dimensions with 21 x 21 elements (pixels). The pixel values (black numbers) can be addressed by their respective pixel indices (green numbers).


multiactivities:
  - ["pixels/pixels_act1.md", [["ImageJ GUI", "pixels/pixels_act1_imagejgui.md"], ["skimage napari", "pixels/pixels_act1_skimage_napari.py"], ["MATLAB", "pixels/pixels_act1_matlab.m"]]]
  - ["pixels/collagen_inspection.md", [["ImageJ GUI", "pixels/collagen_inspection_imagejgui.md"]]]
  
assessment: |

  ### Answer the question

  1. If someome gives you a 2D image file and tells you to measure the value of the pixel at the indices `(7,8)` without telling you which programming language to use. Is that a precise enough instruction? If not, how many different pixels could that actually refer to?  

  > ## Solution
  > 1. Unfortunately this instruction is not precise enough and, in practice it could refer to four different pixels, depending on whether this is meant to be zero or one-based indexing and depending whether this is row or column-major ordering. See [here for more details](https://en.wikipedia.org/wiki/Row-_and_column-major_order).
  {: .solution} 

learn_next:
   - "[Lookup tables](../lut)"
   - "[Spatial calibration](../spatial_calibration)"
   - "[N-dimensional images](../multidimensional_image_basics)"
   - "[Data types](../datatypes)"

external_links:
   - "[Wikipedia: Digital images](https://en.wikipedia.org/wiki/Digital_image)"
   - "[Images in ImageJ: ImagePlus](https://imagej.nih.gov/ij/developer/api/ij/ij/ImagePlus.html)"
   - "[Images in ImgLib2: Accessible](https://imagej.net/libs/imglib2/accessibles)"
   - "[Images in skimage: numpy arrays](https://scikit-image.org/docs/dev/user_guide/numpy_images.html)"
---

### Digital image dimensions

There are several ways to describe the size of a digital image. For example, the following sentences describe the same image.

- The image has 2 dimensions, the length of dimension 0 is 200 and the length of dimension 1 is 100.
- The image has 2 dimensions, the length of dimension 1 is 200 and the length of dimension 2 is 100.
- The image has a size/shape of (200, 100).
- The image has 200 x 100 pixels.

Note that "images" in bioimaging can also have more than two dimensions and one typically specifies how to map those dimensions to the physical space (x,y,z, and t). For example, if you acquire a 2-D movie with 100 time points and each movie frame consisting of 256 x 256 pixels it is quite common to represent this as a 3-D array with a shape of ( 256, 256, 100 ) accompanied with metadata such as ( ("x", 100 nm), ("y", 100 nm), ("t", 1 s) ); check out the module on [spatial calibration](../spatial_calibration) for more details on this.

