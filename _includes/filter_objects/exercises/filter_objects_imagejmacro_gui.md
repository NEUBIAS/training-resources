- Open [xy_8bit_labels__nuclei_touchborder_2.tif]("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__nuclei_touchborder_2.tif")
- Remove objects touching the border
- Create a label mask that contains only the smallest object (metaphase cell)

> ## Solution
> ```
> // File > Open
> open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__nuclei_touchborder_2.tif")
> //  Plugins › MorphoLibJ › Label Images › Remove Border Labels
> run("Remove Border Labels", "left right top bottom");
>// Plugins › MorphoLibJ › Analyze › Analyze Regions
> run("Analyze Regions", "area")
> // Plugins › MorphoLibJ › Label Images › Label Size Filtering
> run("Label Size Filtering", "operation=Lower_Than size=4000");
> ```
{: .solution}
