<h4 id="scanr_12bit><a href="#scanr_12bit>Inspect a ScanR 12-bit image</a></h4> 

This activity shows that correctly handling 12-bit data can be tricky, becuause typically neither on disk nor in memory there is a 12-bit datatype.
 
- Open [xy_16bit__scanR_datatype_issue.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__scanR_datatype_issue.tif)
- For all software that we tested this image is opened as an unsigned integer 16-bit image with a value range from 32963 to 36863
- In fact, this image is a 12-bit image that has an offset of 2^15, probably due to a misinterpretation of the first bit
  - `2^15 = 32768` (minimal possible value, which does not occur in this particular image because there is some background)
  - `2^15 + 2^12 - 1 = 36863` (maximal value possible in this image/datatype)
- Check how many saturated pixels there are
