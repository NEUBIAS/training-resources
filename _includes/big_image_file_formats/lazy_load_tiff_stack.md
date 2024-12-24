<h4 id="tiff"><a href="#tiff">Lazy load from a TIFF stack</a></h4>

- Download [TODO: Large TIFF]()
- Inspect the size of the file on disk and compare to your computer's memory
- Open the whole file
    - Observe that this takes some time
    - Observe that the memory fills up in one go
- Lazy-access XY planes
    - Observe that the memory fills up gradually each time you access a new plane
- Try to lazy-access an XZ plane 
    - Observe that this causes the whole file being loaded, because TIFF files are chunked in XY but not in XZ