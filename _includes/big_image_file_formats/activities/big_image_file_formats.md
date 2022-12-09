### Inspect big image files
- Inspect the size of a (big) several GB TIFF file on disk.
- Compare the file size to the size of your computer's memory.
- Open this file in an image viewer.
- Observe that this takes some time.
- Observe that your memory fills up.
- Open a big image (several GB) from a TIFF file.
- Lazy-load a big image (several GB) from a TIFF file.
- Observe that TIFF chunking is plane-wise.
- Observe that slicing "at an angle" requires loading everything.
- Lazy-load from a file format with resolution pyramid and 3-D chunking (e.g. OME-Zarr, BDV/XML/HDF5)
- Observe that it opens very quickly (thanks to resolution pyramid and chunking).
- Observe that one can swiftly slice the data at all angles (thanks to 3-D chunking).
- Inspect the file format to see the resolution pyramid and chunks.
- Only load one specific resolution level.
- This is useful as most software does not support multi-resolution data for computations.

