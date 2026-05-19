### Open 3-D chunked data directly with BigDataViewer

- Open Fiji
- Use [ Plugins > Utilities > Monitor Memory... ] to keep an eye on the memory
- Open `xyz_uint8__em_platy__3d_chunk.xml` via [ Plugins › BigDataViewer › Open XML/HDF5 ]
- Use `Shift X, Y, Z` to view orthogonal planes
- Use the mouse wheel to move along the current axis
- Use the arrow keys to zoom
- Key observations:
    - Chunks are **lazy-loaded** on demand
    - BDV is **non-blocking**: One can move around even while data is being loaded

### Open 3-D chunked data through Bio-Formats with BigDataViewer

- Open Fiji
- Open `xyz_uint8__em_platy__3d_chunk.xml` via drag & drop on Fiji menu bar
- The Bio-Format UI will open, select `use virtual stack`
- Use [ Plugins › BigDataViewer › Open Current Image ]
- Use `Shift X, Y, Z` to view orthogonal planes
- Key observations:
    - Compared to abvove, the loading performance is very slow, because Bio-Formats can only lazy load planes, which does not match the 3-D chunking of the data

### Open 3-D chunked data multi-resolution data directly with BigDataViewer

- Open Fiji
- Use [ Plugins > Utilities > Monitor Memory... ] to keep an eye on the memory
- Open `xyz_uint8__em_platy__3d_chunk_multires.xml` via [ Plugins › BigDataViewer › Open XML/HDF5 ]
- Key observations:
    - The viewing performance is improved compared with the above 3-D chunked data that did not have multi-resolution

### Open 3-D chunked data multi-resolution data with Bio-Formats

- Open `xyz_uint8__em_platy__3d_chunk_multires.xml` via drag & drop on Fiji menu bar
- Key observations:
    - Since the normal ImageJ viewer does not support multi-resolution data, Bio-Formats asks you to choose one resolution layer

