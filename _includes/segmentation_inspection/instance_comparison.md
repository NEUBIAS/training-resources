<h4 id="instance_comparison"><a href="#instance_comparison">Instance comparison using object count and mean object area</a></h4>

 - Open the reference and candidate segmentation masks
 - Treat non-zero pixels as foreground and label connected components as instances
 - Compute the number of objects in each segmentation
 - Compute the mean object area in each segmentation
 - Compare differences to the reference and interpret whether a segmentation tends to over-segment or under-segment
