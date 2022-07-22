- Skeletonize a binary imgae and obtain branch information.
  - Open
[xy_8bit_glialcells.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_glialcells.tif)
  - Perform skeletonization: **[ Process › Binary › Skeletonize]**
  - Obtain branch information by analyzing the skeleton: **[Analyze › Skeleton › Analyze Skeleton (2D/3D)]**
    - [ ] 'Prune ends'
    - [X] 'Calculate largest shortest path', 'Show detailed info', 'Display labeled skeletons'.
    - In the results window, you can find information about the different skeletons and their branches, such as the number of branches and junctions, the longest shortest path, and the average branch length.
