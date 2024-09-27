### Install CLIJ2
In ImageJ one can project along the z axis (e.g. [Image > Stacks > Z Project ...]), but there is no easy way to project 
along the x or y axis. Thus let's install the very useful [update site](https://imagej.net/update-sites/following): [CLIJ2](https://clij.github.io/).

- [Help > Update...]
- [Manage update sites]
- [X]  clij
- [X]  clij2

### Open example image

- Open [xyz_calibrated_16bit__golgi_bfa.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_calibrated_16bit__golgi_bfa.tif)

### Z axis projection

- Sum projection: [Plugins > ImageJ on GPU (CLIJ2) > Projections > Sum-Z-projection on GPU]
- What is the highest pixel value in the z sum projection? (use e.g. [Analyze > Histogram])

### Y axis projection
- Sum projection: [Plugins > ImageJ on GPU (CLIJ2) > Projections > Max-Y-projeciton on GPU]
- What is the highest pixel value in the y sum projection?
- You should find that the value for the y axis is higher, explain why this could be expected from the morphology of the golgi in the original image.
- What would you expect for doing above steps with maximum projections? Also two different values or two times the same value?

### Answers
- The highest value in the z sum projection is 94558.
- The highest value in the y sum projection is 165401.
- The Golgi is elongated along the y axis, thus a sum projection adds up a lot of high values along this axis.
- For maximum projections you would expect the same value.
