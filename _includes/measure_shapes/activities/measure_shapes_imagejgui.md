- Open image [xy_8bit_labels__four_objects.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__four_objects.tif)
- Perform shape measurements and discuss their meanings **[Plugins > MorphoLibJ > Analyze > Analyze Regions]**
- Discuss (using a white board) some shape features and concepts (see also [MorphoLibJ Documentation](https://imagej.net/MorphoLibJ#Region_analysis)). For example:
  - Area
  - Perimeter
  - Circularity = ( 4 Pi Area ) / Perimeter^2
  - Solidity = Convexity = Area / Area-Convex-Hull
  - Ellipse fit
- Explore results visualisation **[Plugins > MorphoLibJ > Label Images > Assign Measure to Label]**
- Add a calibration of 2 micrometer to the image and check which shape measurements are affected.
- Perform a shape analysis for 3D image [xyz_16bit_labels__spindle_spots.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit_labels__spindle_spots.tif) and **[Plugins > MorphoLibJ > Analyze > Analyze Regions 3D]**
- (Optional) Draw a square (=circle) of different size 2x2 pixels (paper, whiteboard, ...)
  - Measure area, perimeter and circularity
  - Discuss the results
- (Optional) To show effect of small sized objects use
[xy_8bit_labels__circles_different_size.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__circles_different_size.tif). Discuss how discrete nature of image may give mathematically unprecise results for small objects

    diameter-circle (px)	| Area (theory) | Perimeter (theory) | Area (MLJ) | Perimeter (MLJ)
    1	| 0.78	 | 3.141	| 1 |	2.68
    3	| 7.06	| 9.42	| 5 |	8.04
    5	| 19.63	| 15.70	| 21 |	15.62
    11	| 95.03 |	34.55 |	97 |	33.94
    51	| 2042.82	| 160.22 | 	2053 |	161.19

* (Optional) Discuss the England's coastline paradox [Wiki](https://en.wikipedia.org/wiki/Coastline_paradox)
