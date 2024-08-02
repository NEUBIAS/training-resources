<h4 id='measure_2d_shapes'><a href="#measure_2d_shapes">Measure 2-D shapes in an image</a></h4>

- Using a drawing board, discuss important shape features and concepts, such as,
  - Area
  - Perimeter: Like all surface measurements, this is tricky, e.g.,
    - Counting the number of perimeter pixels actually "only" approximates the bounding box
    - See the famous [england's coastline paradox](https://en.wikipedia.org/wiki/Coastline_paradox)
  - Circularity = ( 4 * Pi * Area ) / Perimeter^2: Designed to be 1.0 for a perfect circle
  - Aspect ratio: Major ellipse axis length / Minor ellipse axis length
  - Solidity = Convexity = Area / Convex_hull_area: Useful to find objects with spikes or indentations
  - Ellipse fit parameters or Elongation: Useful to measure object elongation
  - Discuss issues with small object in digital images, e.g., by exploring a square (=circle?!) of 2x2 pixels.
- Perform shape measurements of objects in an image
- Discuss how objects can be distiguished by various shape measurements
- Perform shape measurements in pixel or calibrated units

##### Example data

- Fluorescence image with nuclei of different shapes: [xy_16bit_calibrated__nuclei_various_shapes.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit_calibrated__nuclei_various_shapes.tif)
  - Useful for manual delineation of objects and subsequent measurements
- Label image with objects of different shapes: [xy_8bit_labels__four_objects.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__four_objects.tif)
- Label image with circles of different sizes: [xy_8bit_labels__circles_different_size.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__circles_different_size.tif)
