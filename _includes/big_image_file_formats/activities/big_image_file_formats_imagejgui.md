Currently, no explicit images are provided, because we don't know yet where to provide them. Until we found a solution, please find some appropriate image data for your course.

### Open a big TIFF image

- Open Fiji
- Check big TIFF image file size on disk 
  - Compare to your computer's RAM
- Open image using
  - File › Open...
    - This takes some time, because it needs to load the whole image.
    - Image › Stacks › Orthogonal Views
      - This is fast, because everything is in memory.
  - Plugins › Bio-Formats › Bio-Formats Importer
    - [X] Use virtual stack
      - This enables plane-wise lazy-loading.
    - This is faster, due to lazy-loading.
      - Changing z-slices takes some time, because it needs to lazy-load the corresponding chunk (i.e. plane).
      - Image › Stacks › Orthogonal Views
      - This takes time, because it needs to load everything.

### Open a big XML/HDF5 image

- Open Fiji
- Check XML/HDF5 image file size on disk.
  - Compare to your computer's RAM.
- Open image using
  - Plugins › BigDataViewer › Open XML/HDF5
    - This is fast, because of lazy-loading and resolution pyramids.
    - Zoom in (it will fetch higher resolution levels).
    - Inspect data at different angles.
      - This is fast, because of 3D chunking.
  - Plugins › Bio-Formats › Bio-Formats Importer
    - [X] Use virtual stack
      - This enables plane-wise lazy-loading.
    - Choose a resolution level.
      - Inspect data (now we are at the same situation as if this were a TIFF image with plane-wise chunking, s.a.).
  - HDFView
    - Inspect the .h5 file to see the resolution pyramids and chunking.
