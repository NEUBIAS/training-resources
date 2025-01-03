This activity uses the `bfconvert` tool to convert a czi image data set to the OME-TIFF format; 
and it uses Fiji to inspect the content of the OME-TIFF data.

Note that bfconvert is capable of generating a variety of other formats (in addition to OME-TIFF)
such as tiff, png, jpeg, OME-XML, etc., although we will focus on the OME-TIFF in this activity.

**Basic conversion**

```bash 
bfconvert \
~/ome_zarr_course/data/czi/xyz__multiple_images.czi \
~/ome_zarr_course/data/OME-TIFF/xyz__multiple_images.ome.tiff
```
This will create an OME-TIFF containing two images. Often, this is not convenient, and we would
prefer to specify a single series for conversion.

**Select one series and convert**

```bash
bfconvert \
-series 1 \
~/ome_zarr_course/data/czi/xyz__multiple_images.czi \
~/ome_zarr_course/data/OME-TIFF/xyz__multiple_images_s1.ome.tiff
```

**Specify compression**
```bash
bfconvert \
-series 1 \
-compression "JPEG-2000 Lossy" \
~/ome_zarr_course/data/czi/xyz__multiple_images.czi \
~/ome_zarr_course/data/OME-TIFF/xyz__multiple_images_s1_compressed.ome.tiff
```
**Check output size**
```bash
du -sh ~/ome_zarr_course/data/OME-TIFF/*
```
**Select one series and specify z-range**
```bash 
bfconvert \
-series 0 \
 -range 0 0 \
~/ome_zarr_course/data/czi/xyz__multiple_images.czi \
~/ome_zarr_course/data/OME-TIFF/xyz__multiple_images_s0_range0-1.ome.tiff
```
**Crop in 3-D**
```bash 
bfconvert \
-series 0 \
-range 0 0 \
-crop 20,30,100,100 \
~/ome_zarr_course/data/czi/xyz__multiple_images.czi \
~/ome_zarr_course/data/OME-TIFF/xyz__multiple_images_s0_crop3D.ome.tiff
```

Inspect the output OME-TIFFs using Fiji:
- Drag and drop the created OME-TIFFs onto Fiji
- Repeat the same steps as for the original czi file
- Check whether all image data and metadata have been preserved
