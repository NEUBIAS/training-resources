- Open [xy_8bit_glialcells2.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_glialcells2.tif)
- Perform skeletonization: **[ Process › Binary › Skeletonize]**
- Obtain branch information by analyzing the skeleton: **[Analyze › Skeleton › Analyze Skeleton (2D/3D)]**
    - [ ] 'Prune ends'
    - [X] 'Calculate largest shortest path', 'Show detailed info', 'Display labeled skeletons'.
- In the results window you can find that cell 3 has the largest number of branches, cell 1 has the longest "longest shortest path" and cell 2 has the highest average branch length.
