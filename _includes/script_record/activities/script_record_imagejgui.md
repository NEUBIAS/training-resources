- In FIJI, enable the script recorder: **[ Plugins › Macros › Record...]**
- Open the image [xy_8bit__small_noisy_nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__small_noisy_nuclei.tif).
- Duplicate the image: **[ Image › Duplicate...]**
- Perform a gaussian blur operation with sigma = 7 on the duplicated image: **[ Process › Filters › Gaussian Blur...]**
- Duplicate the non-blurred image once more: **[ Image › Duplicate...]**
- Perform a gaussian blur operation with sigma = 2 on the second duplicated image: **[ Process › Filters › Gaussian Blur...]**
- Inspect (and clean up) the recorded script
- Recorded script should look like this:

```java
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__small_noisy_nuclei.tif");
selectWindow("xy_8bit__small_noisy_nuclei.tif");
run("Duplicate...", " ");
run("Gaussian Blur...", "sigma=7");
selectWindow("xy_8bit__small_noisy_nuclei.tif");
run("Duplicate...", " ");
run("Gaussian Blur...", "sigma=2");
```
- Run the script
- What happens if you remove the second selectWindow command? 
