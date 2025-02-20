<h4 id="tiff"><a href="#tiff">Lazy load from a 3D TIFF</a></h4>

- Download a 3D [TIFF stack (4.0 GB)](https://zenodo.org/records/14591118/files/xyz_uint8__em_platy_raw_s4.tif?download=1)
- Inspect the size of the file on disk and compare to your computer's memory
- Open the whole file
    - Observe that this takes some time
    - Observe that the memory fills up in one go
- Lazy-access XY planes
    - Observe that the memory fills up gradually each time you access a new plane
- Try to lazy-access YZ plane 
    - Observe that this likely causes all data being loaded, because TIFF file chunking is not suited for efficiently accessing YZ planes