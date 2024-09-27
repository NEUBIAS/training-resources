<h4 id="lazy_tiff"><a href="#lazy_tiff">Lazy load from a TIFF stack</a></h4>

- Download [TODO: Large TIFF stack]()
- Inspect the size of the file on disk and compare to your computer's memory
- Open the whole file
    - Observe that this takes some time
    - Observe that your memory fills up
- Lazy-access the file
    - Observe that TIFF chunking is plane-wise, which means that  slicing "at an angle" requires loading everything.