<h4 id="bdv_hdf5"><a href="#bdv_hdf5">Lazy load from an BDV HDF5 image</a></h4>

- Download [TODO: Large BDV stack]()
- Inspect the size of the file on disk and compare to your computer's memory
- Open the whole file
    - Observe that this takes some time
    - Observe that your memory fills up
- Lazy-access the file
    - Observe that TIFF chunking is plane-wise, which means that  slicing "at an angle" requires loading everything.