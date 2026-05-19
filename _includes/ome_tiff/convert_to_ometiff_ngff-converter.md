This activity uses the NGFF Converter to convert a LIF image data set into an OME-TIFF image data set; and it uses Fiji to inspect the content of both the LIF and the OME-TIFF.

- Inspect LIF using Fiji:
    - Drag and drop the LIF image onto Fiji
    - The Bio-Formats Importer will open
        - `[X]` Display OME-XML metadata
        - [ OK ]
        - Select all images
        - [ OK ]
    - Take note of
        - Number of images
        - For each image note its dimensions and spatial calibration
    - Inspect the OME-XML metadata and note down some values that you deem important
- Convert LIF to OME-TIFF using the NGFF converter: 
    - Open the NGFF converter; [tool website](https://www.glencoesoftware.com/products/ngff-converter/) 
    - Drag and drop the LIF file onto it
    - A dialog will open:
        - Output format: OME-TIFF
        - Output location: As you wish
        - [ Apply ]
    - [ Run Jobs ]
- Inspect OME-TIFF using Fiji:
    - Drag and drop the created OME-TIFF onto Fiji
    - Repeat the same steps as for the original LIF file
    - Check whether all image data and metadata has been preserved

#### Key points

- The NGFF converter is a nice tool to create OME-TIFF
- OME-TIFF can contain multiple image data sets
- OME-TIFF can contain resolution pyramids
