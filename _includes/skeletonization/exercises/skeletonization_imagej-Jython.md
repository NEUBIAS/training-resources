Perform skeletonization and skeleton analysis on this image: [xy_8bit_glialcells2.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_glialcells2.tif).

Try to answer the following questions:

1. which cell has the largest number of branches?

2. which cells has the longest "longest shortest path"?

3. which cells has the highest average branch length?

> ## Solution
> ```python
># Open image and perform skeletonization
>
># import classes
>from ij import IJ
>
># open image
>imp = IJ.openImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_glialcells2.tif")
>imp.show()
>
># perform skeletonization
>skeleton = imp.duplicate()
>IJ.run(skeleton, "Skeletonize", "")
>skeleton.show()
>
># analyze the skeleton
>IJ.run(skeleton, "Analyze Skeleton (2D/3D)", "prune=none calculate show display");
>
>IJ.run("Tile")
># check the data in the results window to answer the questions. 
> ```
{: .solution}
