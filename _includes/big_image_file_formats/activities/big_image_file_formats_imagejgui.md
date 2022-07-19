Please note that currently, no explicit images are mentioned, because we don't know yet where to provide big image data. Until we found a solution, please find some appropriate image data for your course.

#### Open a big TIFF image

- Check big TIFF image file size on disk 
  - Compare to your computer's RAM
- Open Fiji
  - [ Plugins › Utilities › Monitor Memory... ]
- Load TIFF as a whole: [ File › Open... ]
  - Observe that this is slow, because it needs to load the whole image.
  - Observe how the memory fills up.
  - Slice in x,y,z: [ Image › Stacks › Orthogonal Views ]
    - Observe that this is relatively fast, because all data is in memory already.
- Lazy load: [ Plugins › Bio-Formats › Bio-Formats Importer ]
  - [X] Use virtual stack
    - This enables plane-wise lazy-loading.
  - This is faster, due to lazy-loading.
    - Changing z-slices takes some time, because it needs to lazy-load the corresponding chunk (i.e. plane).
    - Slice in x,y,z: [ Image › Stacks › Orthogonal Views ]
      - This takes more time now, because all data needs to be loaded.
      - Check the memory while it is taking the time.

#### Open a big XML/HDF5 image

- Check XML/HDF5 image file size on disk.
  - Compare to your computer's RAM.
- Open Fiji
  - [ Plugins › Utilities › Monitor Memory... ]
- Lazy load XML/HDF5 using [ Plugins › BigDataViewer › Open XML/HDF5 ]
  - This is fast, because of lazy-loading and resolution pyramids.
  - Zoom in (it will fetch higher resolution levels).
  - Inspect the data at different angles [ Left button drag ]
    - This is fast, because of 3D chunking.
- Lazy load XML/HDF5 using [ Plugins › Bio-Formats › Bio-Formats Importer ]
    - [X] Use virtual stack
      - This enables plane-wise lazy-loading.
    - Choose a resolution level.
      - Inspect data (now we are at the same situation as if this were a TIFF image with plane-wise chunking, s.a.).
  - HDFView
    - Inspect the .h5 file to see the resolution pyramids and chunking.
