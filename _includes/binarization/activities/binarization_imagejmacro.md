```
open("/image-analysis-training-resources/image_data/xy_8bit__two_cells.tif");
setThreshold(30, 255);
setOption("BlackBackground", true);
run("Convert to Mask");
```
