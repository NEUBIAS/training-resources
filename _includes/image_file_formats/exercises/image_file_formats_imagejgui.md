### Image inspection

- Open [xyz__multiple_images.czi](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz__multiple_images.czi)
  - How many images are contained?
  - What are the dimensions of the images?
  - What are the voxel sizes of the images? 

> ## Solution
> - There are two images 
> - [ Image > Show Info ] reveals that both have SizeC = 1, SizeT = 1, SizeX = 251, SizeY = 251, SizeZ = 2
> - [ Image > Properties ] shows that dx = dy = 0.195 micrometer and dz = 0.3 micrometer
{: .solution}

### Image saving

- Open [xyzct_16bit__mitosis.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzct_16bit__mitosis.tif) 
- Enable the view of all channels by selecting `Composite` in [Image > Color > Channels Tools ...]
- Save as PNG
- Open the saved image: What has changed as compared to the original image?

> ## Solution
> - The original image looks like the image in the viewer when loaded in ImageJ or the OS viewer
> - Pixel calibration and intensities have been lost. 
{: .solution}

