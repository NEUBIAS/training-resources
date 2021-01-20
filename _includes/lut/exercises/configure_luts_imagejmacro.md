Open those two files:
- "xy_calibrated_16bit__nuclear_protein_control.tif"
- "xy_calibrated_16bit__nuclear_protein_treated.tif"

Display them with the same gray scale LUT and the same LUT settings (this is what you should do for a presentation).

> ## Solution
> ```
> run("Close All");
> open("/Users/tischer/Documents/training-resources/image_data/xy_calibrated_16bit__nuclear_protein_control.tif");
> run("Grays");
> setMinAndMax(8, 3804);
> open("/Users/tischer/Documents/training-resources/image_data/xy_calibrated_16bit__nuclear_protein_treated.tif");
> run("Grays");
> setMinAndMax(8, 3804);
> run("Tile");
> ```
{: .solution}
