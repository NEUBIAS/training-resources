Perform skeletonization and skeleton analysis on this image: [xy_8bit_glialcells2.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_glialcells2.tif).

Try to answer the following questions:

1. which cell has the largest number of branches?

2. which cells has the longest "longest shortest path"?

3. which cells has the highest average branch length?


> ## Solution
> Open [xy_8bit_glialcells.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_glialcells2.tif)
>
> Perform skeletonization: **[ Process › Binary › Skeletonize]**
>
> Obtain branch information by analyzing the skeleton: **[Analyze › Skeleton › Analyze Skeleton (2D/3D)]**
>
> Deselect 'Prune ends'
>
> Select: 'Calculate largest shortest path', 'Show detailed info', 'Display labeled skeletons'.
>
> In the results window you can find that cell 3 has the largest number of branches, cell 1 has the longest "longest shortest path" and cell 2 has the highest average branch length.
{: .solution}
