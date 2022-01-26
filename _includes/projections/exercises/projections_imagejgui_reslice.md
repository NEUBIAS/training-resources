- Open [xyz_calibrated_16bit__golgi_bfa.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_calibrated_16bit__golgi_bfa.tif)
- Perform a z axis sum projection
  - What is the highest pixel value in the z sum projection? (use e.g. [Analyze > Histogram])
- Perform a y axis sum projection
  - What is the highest pixel value in the y sum projection?
- You should find that the value for the y axis is higher, explain why this could be expected from the morphology of the golgi in the original image.
- What would you expect for doing above exercise with maximum projections? Also two different values or two times the same value?

> ## Solution
> - Sum projection along the z axis:
>   - `run("Z Project...", "projection=[Sum Intensity]");`
>   - The highest value is 94558.
> - Sum projection along the y axis:
>   - `run("Reslice [/]...", "start=Top avoid");`
>   - `run("Z Project...", "projection=[Sum Intensity]");`
>   - The highest value is 165401.
> - The Golgi is elongated along the y axis, thus a sum projection adds up a lot of high values along this axis.
> - For maximum projections you would expect the same value; in fact, here, in both cases you simply get the highest value in the whole volume.
{: .solution}
