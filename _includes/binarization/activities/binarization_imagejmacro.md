```
open(); //image is xy_8bit__two_cells.tif
setThreshold(49, 255);
setOption("BlackBackground", true);
run("Convert to Mask");
```
