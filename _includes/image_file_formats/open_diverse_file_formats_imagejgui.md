- Open the files mentioned in the activity:
  - [Plugins > Bio-Formats > Bio-Format Importer]. 
    - [X] Display metadata
    - [X] Display OME-XML Metadata
      - Should be the same information as above but in XML (sometimes it is more correct than the above)
- For ICS/IDS and XML/HDF5:
  - The ICS and XML file are the entry points that should be opened (the respective other file will be read automatically).
  - Also inspect the ICS and XML files in a simple text editor.

- Saving 8 bit single channel image as TIFF: 
  - Open [xy_8bit__nuclei_PLK1_control.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_PLK1_control.tif) 
  - [Image > Adjust > Brightness/Contrast] such that cells appear saturated
  - [File > Save As > TIFF...] 
    - Open with Fiji 
      - LUT metadata has changed, but pixel values and calibration metadata are preserved
    - Open with a web browser
      - It may not open at all

- Saving 8 bit single channel image as JPEG: 
  - Open [xy_8bit__nuclei_PLK1_control.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_PLK1_control.tif) 
  - [Image > Adjust > Brightness/Contrast] such that cells appear saturated
  - [File > Save As > JPEG...] 
    - Open with Fiji
      - Pixel values have changed
      - Calibration metadata is gone
    - Open with a web browser
      - It should look the same as when you saved it

- Saving 16 bit two channel movie as JPEG: [xyzct_16bit__mitosis.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzct_16bit__mitosis.tif)
  - Select a timepoint in the middle of the movie 
  - [File > Save As > JPEG...] 
    - Open JPEG with Fiji
    - Image dimensions, data type, pixel values, and metadata have changed  
  
- Saving 8 bit single channel movie as GIF: [xyt_8bit__mitocheck_incenp.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyt_8bit__mitocheck_incenp.tif)
  - [Image > Adjust > Brightness/Contrast] such that cells appear saturated
  - [File > Save As > GIF...] 
    - Open with Fiji
      - Pixel values have changed
    - Open with a web browser
      - Movie plays and looks as when you saved it 
 

