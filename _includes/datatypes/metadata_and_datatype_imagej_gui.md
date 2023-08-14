
For each image perform the below tasks.

- Open the image using `[ Plugins > Bio-Formats > Bio-Formats Importer ]`
    - `[X] Display metadata`
    - `[ OK ]`
- Check whether the image data type mentioned in the image header is the same as the one mentioned in the metadata text.
- Check the maximum value in the image, e.g. using `[ Analyze > Histogram ]`
- How does this maximum value compare the image's datatype?
    - For example, you may find a value of 4095, which is the maximum of an unsigned integer 12 bit image, which may be the datatype mentioned in the image metadata, however ImageJ may represent this image as a 16 bit image. Appreciate that this can be confusing.

