<h4 id='measure_act1'><a href="#measure_act1">Measure object shapes in a digital image</a></h4>

- Using a drawing board discuss some shape features and concepts, e.g.,
  - Area
  - Perimeter: Like all surface measurements, this is tricky, e.g., 
    - Counting the number of perimeter pixels approximates the bounding box!
    - TODO: get reference from David
    - [England's coastline paradox](https://en.wikipedia.org/wiki/Coastline_paradox)
  - Circularity = ( 4 * Pi * Area ) / Perimeter^2: Designed to be 1.0 for a perfect circle
  - Solidity = Convexity = Area / Convex_hull_area: Useful to find "spiky" objects
  - Ellipse fit: Useful to measure object elongation
  - Discuss issues with small object in digital images, e.g., by exploring a square (=circle?!) of 2x2 pixels.
- Open an image with objects, e.g.,
  - Label image: [xy_8bit_labels__four_objects](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__four_objects.tif)
    - Contains objects with different shapes
  - Label image: [xy_8bit_labels__circles_different_size.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__circles_different_size.tif) 
    - Contains circles of different sizes, useful to check perimeter measurement implementations
- Perform shape features such as area, perimeter, circularity, and solidity
- Discuss how objects can be distiguished by various features
