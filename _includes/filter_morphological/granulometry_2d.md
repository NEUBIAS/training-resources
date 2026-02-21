<h4 id="granulometry2d"><a href="#granulometry2d">Workflow to perform 2-D granulometry using opening filters</a></h4>

[Morphological granulometry](https://en.wikipedia.org/wiki/Granulometry_(morphology)) is an image analysis technique to compute a size distribution of objects in an image. There are various implementations. Here we will use a technique that applies a sequence of opening filters. This approach has the advantage that we don't need instance segmentations of the objects, but a binary foreground segmentation suffices. 

- Open the example images:
    - [xy_16bit__bacteria_cords_thick.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__bacteria_cords_thick.tif)
    - [xy_16bit__bacteria_cords_thin.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__bacteria_cords_thin.tif)
- Observe that the structures in one image are relatively thicker than in the other one.  
- Perform an opening filter based granulometry analysis to quantify this difference.
