<h4 id="tiff"><a href="#tiff">Lazy load from a multi-plane TIFF file</a></h4>

- Download a [TIFF stack (4.0 GB)](https://zenodo.org/records/14591118/files/xyz_uint8__em_platy_raw_s4.tif?download=1)
- Inspect the size of the file on disk and compare to your computer's memory
- Open the whole file
    - Observe that this takes some time
    - Observe that the memory fills up in one go
- Lazy-access XY planes
    - Observe that the memory fills up gradually each time you access a new plane
- Try to lazy-access an XZ plane 
    - Observe that this causes the whole file being loaded, because TIFF files are chunked in XY but not in XZ