- Drag and drop the .VSI file on Fiji
  - What happens?
  - For us, it seemingly opened the image data wrongly, showing some weird RGB data
- Now open the VSI file using [Plugins > Bio-Formats > Bio-Formats Importer]
  - [X] Display metadata
  - [X] Display OME-XML Metadata
  - Press [OK]
  - In the upcoming dialog select the first image "series", which represents the actual image data
  - Press [OK]
- The image data and metadata will open and can be inspected

Copy the VSI file to a different location and try again opening it. This should NOT work anymore, because the link to actual data, which is in the ETS file, is now broken
