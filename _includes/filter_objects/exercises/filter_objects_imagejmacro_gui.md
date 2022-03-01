- Open [xyz_16bit__unfiltered_cells_labelmask.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit__unfiltered_cells_labelmask.tif)
- See if you have objects touching the borders, if yes, count them manually
- Automatically remove the border objects
- Check how many objects have been removed (Hint: generate measurement tables before and after border removal operation)

> ## Solution
> ```
> run("Close All")
> // File > Open
> open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit__unfiltered_cells_labelmask.tif")
>
> // Scroll to the last slice of the image and check how many distinct labels you can find there (i.e. count = 13)
>// Plugins › MorphoLibJ › Analyze › Analyze Regions 3D (Note: [X] Voxel Count)
> run("Analyze Regions 3D", "voxel_count surface_area_method=[Crofton (13 dirs.)] euler_connectivity=6");
> // Plugins › MorphoLibJ › Label Images › Remove Border Labels
> run("Remove Border Labels", "left right top bottom front back");
>// Plugins › MorphoLibJ › Analyze › Analyze Regions 3D (Note: [X] Voxel Count)
> run("Analyze Regions 3D", "voxel_count surface_area_method=[Crofton (13 dirs.)] euler_connectivity=6");
>
> // Compare the first columns of both the tables and count the entries. In the second table, there should be exactly 13 entries less than total number of entries in first table
> ```
{: .solution}
