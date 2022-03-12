Perform skeletonization and skeleton analysis on this image: [xy_8bit_glialcells2.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_glialcells2.tif).

Try to answer the following questions:

1. which cell has the largest number of branches?

2. which cells has the longest "longest shortest path"?

3. which cells has the highest average branch length?

> ## Solution
> ```
>// Open binary image and perform skeletonization
>
>// Open image
>open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_glialcells2.tif");
>
>// Duplicate the image
>run("Duplicate...", " ");
>
>// Perform skeletonization
>run("Skeletonize");
>
>// Obtain branch properties
>run("Analyze Skeleton (2D/3D)", "prune=none calculate show display");
>
>run("Tile")
>// check the data in the results window to answer the questions.
> ```
{: .solution}
