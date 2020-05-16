```
// make a pointlist of random coordinates in the GPU
number_of_points = 200;
number_of_dimensions = 2;
bit_depth = 32;
Ext.CLIJ2_create2D(pointlist, number_of_points, number_of_dimensions, bit_depth);
random_min = 0;
random_max = 400;
seed = getTime();
Ext.<a href="https://clij.github.io/clij2-docs/reference_setRandom">CLIJ2_setRandom</a>(pointlist, random_min, random_max, seed);

// draw labelled spots (1, 2, 3, ...) in 2D space
Ext.<a href="https://clij.github.io/clij2-docs/reference_pointlistToLabelledSpots">CLIJ2_pointlistToLabelledSpots</a>(pointlist, spots_image);

// partition the space between points
Ext.<a href="https://clij.github.io/clij2-docs/reference_labelVoronoiOctagon">CLIJ2_labelVoronoiOctagon</a>(spots_image, label_map);
Ext.CLIJ2_pull(label_map);
run("glasbey_on_dark");
```
