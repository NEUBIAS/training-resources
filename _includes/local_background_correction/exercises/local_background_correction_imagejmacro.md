### Spots in a cell

Note: This module's activity (see above) contains all the ImageJ commands that you need for below exercise.

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


### Motors on microtubules (advanced)

The magic of area openings....

- Open [xy_16bit__motors_on_microtubules.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__motors_on_microtubules.tif)
- The challenge is to automatically segment and measure the intensity of the two spots (motors)
- Try to create a background image only containing the microtubules, using a median filter
- Subtract the resulting background image from the input image
  - You will probably not succeed in getting a clean result that only contains the motors.
  - Why is this the case?
- Try now creating a background image using [ Plugins › MorphoLibJ › Gray Scale Attribute Filtering ]
  - It works, it's magic, isn't it?

> ## Solution
> ```
> run("Close All");
> open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__motors_on_microtubules.tif");
> rename("input")
> run("Duplicate...", "bg");
> run("Gray Scale Attribute Filtering", "operation=Opening attribute=Area minimum=100 connectivity=4");
> rename("bg");
> imageCalculator("Subtract create 32-bit", "input","bg");
> run("Tile")
> ```
{: .solution}
