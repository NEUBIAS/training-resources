```
open("/image-analysis-training-resources/image_data/xy_8bit__two_cells.tif");
input = getTitle();

// Init GPU
run("CLIJ2 Macro Extensions", "cl_device=");
Ext.CLIJ2_clear();

// push data to GPU
Ext.CLIJ2_push(input);

// cleanup ImageJ
run("Close All");

// create a mask using a fixed threshold
threshold = 30;
Ext.CLIJ2_threshold(input, mask, threshold);

// show result
Ext.CLIJ2_pullBinary(mask);
```
