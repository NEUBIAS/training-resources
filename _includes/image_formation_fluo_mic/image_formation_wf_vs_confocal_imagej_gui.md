- Open the example image
- Place a ROI around the object in the image
- Use `Image › Stacks › Plot Z-axis Profile` to measure the mean intensity at each z-position
- Compute the change in intensity in percent from the brightest to the dimmest plane: `%change = 100% * (max - min) / (max - bg)`
  - Do this for both the confocal and the wide-field channel and compare the results
- Repeat, now using a much larger ROI such that all the blurred wide-field signal is always included in all z-planes
