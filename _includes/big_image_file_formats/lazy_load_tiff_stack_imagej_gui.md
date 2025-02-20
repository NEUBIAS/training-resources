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
    - Observe that now it needs to load all data

#### TIFF chunking and layout on disk

The above acitivity demonstrated that one can efficiently lazy load XY planes from a TIFF file. However lazy loading YZ planes efficiently is not possible. The reason is that for all current storage systems (e.g., hard disks) data that resides close together can be read in **one read** operation; however, data that is distributed must be read in a **sequence of seek and read** operations, which is much slower. Note that often it is actually faster to just read everything in one go, even if not all data is needed.

![Lazy load from 3D TIFF](../figures/lazy_load_from_3d_tiff.png)


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

- "Bio-Formats Importer" with the "Open virtual" option allows you to lazy load image data into Fiji
- "Bio-Formats Importer" only supports plane-wise lazy loading from a single resolution level
- TIFF stacks are internally plane-wise chunked
