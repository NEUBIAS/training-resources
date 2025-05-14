This activity uses the `bfconvert` tool to convert a czi image data set to the OME-TIFF format; 
and it uses Fiji to inspect the content of the OME-TIFF data.

Note that bfconvert is capable of generating a variety of other formats (in addition to OME-TIFF)
such as tiff, png, jpeg, OME-XML, etc., although we will focus on the OME-TIFF in this activity.

Before starting, make sure you have downloaded the `xyz__multiple_images.czi` somewhere convenient.
We refer to this input path as `/path/to/xyz__multiple_images.czi`. 
Also create an output folder for OME-TIFF. We refer to this output folder as `/path/to/OME-TIFFs`


**Basic conversion**

```bash 
bfconvert /path/to/xyz__multiple_images.czi /path/to/OME-TIFFs/xyz__multiple_images.ome.tiff
```
This will create an OME-TIFF containing two images. Often, this is not convenient, and we would
prefer to specify a single series for conversion.

**Select one series and convert**

```bash
bfconvert -series 1 /path/to/xyz__multiple_images.czi /path/to/OME-TIFFs/xyz__multiple_images_s1.ome.tiff
```

**Specify compression**
```bash
bfconvert -series 1 -compression "JPEG-2000 Lossy" /path/to/xyz__multiple_images.czi /path/to/OME-TIFFs/xyz__multiple_images_s1_compressed.ome.tiff
```
**Check output size**
```bash
du -sh /path/to/OME-TIFFs/* # unix
```
**Select one series and specify z-range** \
Use the option `-range START END`
```bash 
bfconvert -series 0 -range 0 0 /path/to/xyz__multiple_images.czi /path/to/OME-TIFFs/xyz__multiple_images_s0_range0-0.ome.tiff
```
**Crop in 3-D** \
Use the option `-crop x,y,WIDTH,HEIGHT`
```bash 
bfconvert -series 0 -range 0 0 -crop 20,30,100,100 /path/to/xyz__multiple_images.czi /path/to/OME-TIFFs/xyz__multiple_images_s0_crop3D.ome.tiff
```

Inspect the output OME-TIFFs using Fiji:
- Drag and drop the created OME-TIFFs onto Fiji
- Repeat the same steps as for the original czi file
- Check whether all image data and metadata have been preserved
