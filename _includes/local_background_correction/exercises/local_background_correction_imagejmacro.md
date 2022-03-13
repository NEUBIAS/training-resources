### Spots in a cell

- Open [xy_16bit__autophagosomes_crop.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes_crop.tif)
- Duplicate the image and apply a median filter in order to create the background image
  - Choose the radius of the median filter just large enough such that the bright spots dissappear
- Subtract the resulting background image from the input image
  - You should see an image with the bright spots, but now without the uneven background

> ## Solution
> ```
> run("Close All");
> // File › Open...
> open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes_crop.tif");
> // Image › Rename...
> rename("input");
> // Image › Duplicate...
> run("Duplicate...", "title=median");
> // Process › Filters › Median...
> run("Median...", "radius=7");
> // Image › Rename...
> rename("background");
> // Process › Image Calculator...
> imageCalculator("Subtract create 32-bit", "input", "background");
> // Image › Rename...
> rename("foreground");
> // Window › Tile
> run("Tile");
> ```
{: .solution}
