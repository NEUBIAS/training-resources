#### Fully load TIFF stack into memory

- Check the image file size on disk
- Compare this to your computer's memory
- Open Fiji
- Use [ Edit > Options > Memory & Threads... ] to see how much  memory is accessible to Fiji
- Use [ Plugins > Utilities > Monitor Memory... ] to monitor how much memory is currently used
- Use [ File > Open ] to open the entire TIFF stack
    - Observe that this takes time and that the memory fills up
- Close the image and observe whether memory is freed
- Use [ Plugins > Utilities > Collect Garbage ] to enforce freeing the memory

#### Lazy load TIFF into standard ImageJ Viewer

- Use [ Plugins > Bio-Formats > Bio-Formats Importer ] to lazy open the TIFF stack 
    - [X] Open virtual (<= this is key!) 
    - Observe that initial opening is faster and your memory is not filling up as much
- Move up and down along the z-axis
    - Observe that this is a bit slow because it needs to fetch the data
    - Observe that your memory fills up while you move
- Use [ Image > Stacks > Orthogonal Views ] to look at the data from the side
    - Observe that now it needs to load all data, because efficiently lazy loading YZ planes from TIFF is not possible, because TIFF files are chunked as XY planes

#### Lazy load TIFF into BigDataViewer (BDV)

- Close all images
- Use [ Plugins > Utilities > Collect Garbage ] to free all memory
- Make sure to still monitor the memory, using [ Plugins > Utilities > Monitor Memory... ]
- Again, use [ Plugins > Bio-Formats > Bio-Formats Importer ] to lazy open the TIFF stack 
    - [X] Open virtual
- Now, use [ Plugins > BigDataViewer > Open Current Image ] to view the TIFF stack in BDV
- In BDV, use the down arrow key to zoom out (this is necessary for the following   )
- In BDV, use [ Shift + Y ] to view a XZ plane of the image 
    - Observe that you immediately see something and how the planes are lazy loaded
    - Observe that not all planes are loaded, but just as many as needed for the current number of pixels of the viewer window and the current zoom level
    - Use the up arrow keys to zoom in and observe how additional data is being loaded

#### Key points

- "Bio-Formats Importer" with the **open virtual** option allows you to **lazy load XY planes** from image data into Fiji
- **TIFF stacks are chunked as XY planes** and within the planes as Y strips; lazy loading planes is typically supported by reader libraries, lazy-loading strips is less supported (and may not be efficient because it may be faster to just load the whole plane anyway).
- The ImageJ viewer is **blocking**; BigDataViewer is **not blocking**, i.e. you can move around while data is being loaded.
