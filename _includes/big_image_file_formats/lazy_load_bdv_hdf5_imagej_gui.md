- Open Fiji
- [ Plugins > Utilities > Monitor Memory... ]
- Use [ File > Open ] to open the entire TIFF stack
    - Observe that this takes time and that your computer's memory fills up
- Close the image and observe whether memory is freed
    - Use [ Plugins > Utilities > Collect Garbage ] to enforce freeing the memory
- Use [ Plugins > Bio-Formats > Bio-Formats Importer ] to lazy open the TIFF stack 
    - [X] Open virtual (<= this is key!) 
    - Observe that initial opening is faster and your memory is not filling up as much
- Move up and down along the z-axis
    - Observe that this is a bit slow because it needs to fetch the data
    - Observe that your memory fills up while you move
- Use [ Image > Stacks > Orthogonal Views ] to look at the data from the side
    - Observe that now it needs to load all data 

#### Key points

- "Bio-Formats Importer" with the "Open virtual" option allows you to lazy load image data into Fiji
- "Bio-Formats Importer" only supports plane-wise lazy loading from a single resolution level
- TIFF stacks are internally plane-wise chunked