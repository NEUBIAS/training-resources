Record a script to produce a maximum, median and sum projection of this image: [xyz_8bit__nucleus.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__nucleus.tif).

> ## Solution
> - **[Plugins › Macros › Record...]** (Select 'macro' in the first dropdown menu of the Recorder)
> - Open the image [xyz_8bit__nucleus.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__nucleus.tif) either via **[File > Open...]** if you have it saved locally, or through dragging and dropping of the link into the FIJI window.
> - Select the original image and go to **[Image › Stacks › Z Project...]** and choose maximum intensity projection.
> - Select the original image and go to **[Image › Stacks › Z Project...]** and choose median projection.
> - Select the original image and go to **[Image › Stacks › Z Project...]** and choose sum slices.
> - Output recorded script should look like this:
> ```java
>open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__nucleus.tif");
>selectWindow("xyz_8bit__nucleus.tif");
>run("Z Project...", "projection=[Max Intensity]");
>selectWindow("xyz_8bit__nucleus.tif");
>run("Z Project...", "projection=Median");
>selectWindow("xyz_8bit__nucleus.tif");
>run("Z Project...", "projection=[Sum Slices]");
>```
{: .solution}
