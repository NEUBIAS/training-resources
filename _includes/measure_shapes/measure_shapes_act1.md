<h4 id='measure_act1'><a href="#measure_act1">Measure object shapes in a digital image</a></h4>

- Using a drawing board discuss some shape features and concepts, e.g.,
  - Area
  - Perimeter: Like all surface measurements, this is tricky, e.g.,
    - Counting the number of perimeter pixels approximates the bounding box
    - See the famous [england's coastline paradox](https://en.wikipedia.org/wiki/Coastline_paradox)
  - Circularity = ( 4 * Pi * Area ) / Perimeter^2: Designed to be 1.0 for a perfect circle
  - Aspect ratio: Major ellipse axis length / Minor ellipse axis length
  - Solidity = Convexity = Area / Convex_hull_area: Useful to find objects with spikes or indentations
  - Ellipse fit parameters or Elongation: Useful to measure object elongation
  - Discuss issues with small object in digital images, e.g., by exploring a square (=circle?!) of 2x2 pixels.
- Open an image with objects, e.g.,
  - Fluorescence image with nuclei of different shapes: [xy_16bit_calibrated__nuclei_various_shapes.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit_calibrated__nuclei_various_shapes.tif)
  - Label image with objects of different shapes: [xy_8bit_labels__four_objects.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__four_objects.tif)
  - Label image with circles of different sizes: [xy_8bit_labels__circles_different_size.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__circles_different_size.tif)
- Perform shape features such as area, perimeter, circularity, and solidity
- Discuss how objects can be distiguished by various shape measurements
