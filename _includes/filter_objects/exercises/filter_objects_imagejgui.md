- Open [xyz_16bit_labels_nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit_labels_nuclei.tif)
- See if you have objects touching the borders, if yes, count them manually
- Automatically remove the border objects
- Check how many objects have been removed (Hint: generate measurement tables before and after border removal operation)

> ## Solution
>
>
>
> - Scroll to the last slice of the image and check how many distinct labels you can find there (i.e. count = 13)
> - **[Plugins › MorphoLibJ › Analyze › Analyze Regions 3D]** (Note: [X] Voxel Count)
> - **[Plugins › MorphoLibJ › Label Images › Remove Border Labels]**
> - **[Plugins › MorphoLibJ › Analyze › Analyze Regions 3D]** (Note: [X] Voxel Count)
> - Compare the first columns of both the tables and count the entries. In the second table, there should be exactly 13 entries less than total number of entries in first table
>
{: .solution}
