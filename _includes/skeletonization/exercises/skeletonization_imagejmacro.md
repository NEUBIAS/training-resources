```java
// Open binary image and perform skeletonization

// Open image
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_glialcells2.tif");

// Duplicate the image
run("Duplicate...", " ");

// Perform skeletonization
run("Skeletonize");

// Obtain branch properties
run("Analyze Skeleton (2D/3D)", "prune=none calculate show display");

run("Tile")
// check the data in the results window to answer the questions.
```
