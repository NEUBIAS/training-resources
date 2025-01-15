- Inspect the ImageJ-TIFF image
  - Open by drag and drop into the FIJI window:
    - Inspect the image
    - Inspect the metadata via [Image > Show info...]
  - Close the image and open it again via Bio-Formats Importer:
    - [Plugins > Bio-Formats > Bio-Formats Importer]
    - Select your image
    - [X] Display metadata
    - Click [OK]
  - Both options should yield the same pixel calibration
- Inspect the Molecular Devices TIFF image
  - Repeat the above steps and observe that the pixel calibration is only read by the Bio-Formats importer

#### Key points

- There are different TIFF variants
- There are different TIFF openers in Fiji 
- Typically, the Bio-Formats plugin does the best job in terms of reading all metadata


