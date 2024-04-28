- Open collagen images [0h_collagen_secretion](https://github.com/NEUBIAS/training-resources/raw/master/image_data/image_inspection_and_presentation/xy_16bit__0h_collagen.ome.tif) and [96h_collagen_secretion](https://github.com/NEUBIAS/training-resources/raw/master/image_data/image_inspection_and_presentation/xy_16bit__96h_collagen.ome.tif)
- Adjust the display range of both images using `Image > Adjust > Brightness/Contrast...`
  - Try to select an intensity range for control image and then use the same `min` and `max` values for the treatment image
    - This can be done using the `Set` button of the `B&C` window. This will open another window `Set Display Range`. As an example, set `Minimum displayed value` and `Maximum displayed value` to `0` and `3500` respectively and select `[x] Propagate to all other open images` and press `OK`
- If metadata is missing, add it manually to both images
  - Open `Image > Properties...`
    - Set `Pixel width` and `Pixel height` to `0.324` `micron`
- Add  calibration bar to both images using `Analyze > Tools > Calibration Bar...`
  - `Location` - `Upper Left`
  - `Fill color` - `White`
  - `Label color` -  `Black`
  - `Font size` - `12`
  -  `Zoom factor` - `4`
  - `[x] Overlay`
- Open dapi images [0h_dapi](https://github.com/NEUBIAS/training-resources/raw/master/image_data/image_inspection_and_presentation/xy_16bit__0h_dapi.ome.tif) and [96h_dapi](https://github.com/NEUBIAS/training-resources/raw/master/image_data/image_inspection_and_presentation/xy_16bit__96h_dapi.ome.tif)
- Adjust the display range of both images using `Image > Adjust > Brightness/Contrast...`
  - Use `Set` button of `B&C` and set `Minimum displayed value` and `Maximum displayed value` to `0` and `4000` respectively and select `[x] Propagate to all other open images` and press `OK`
- Merge channels belonging to the same image (e.g. "_*_0h_collagen.ome.tif_" belongs to "_*_0h_dapi.ome.tif_") using `Image > Color > Merge Channels...`. and in the settings:
  - Set collagen channel as `C2(green)`
  - Set dapi channel as `C3(blue)`
  - `[x] Create composite`
  - `[x] Keep source images`
- Add scale bar to each image using `Analyze > Tools > Scale Bar...` and increase `Thickness in pixels` and `Font size` to suit your needs
  - `Thickness in pixels` - `20`
  - `Width in um` - `100`
  - `Font size` - `50`
  - `Location` - `Lower left`
  - `[x] Overlay`
- Close `dapi` single channel image windows
- Select `Rectangle` tool from Fiji GUI, and select an ROI on `0h_collagen` image (grayscale)
  - Add it as overlay on the image using `Image > Overlay > Add Selection...`
  - Duplicate the selection to create an ROI image using `Image > Duplicate...`
    - `[] Ignore selection`
    - _Note:_ The overlay box stays on the original image even if you click elsewhere
  - Add scale bar to ROI image using `Analyze > Tools > Scale Bar...` and reduce `Thickness in pixels` and `Font size` to suit your needs
  - Select a `Line` tool from Fiji GUI, and draw a line in the middle of ROI image
  - Add it as an overlay on the image using `Image > Overlay > Add Selection...`
  - Plot intensity profile along this line using `Analyze > Plot Profile`
    - Set the y-axis range using `Set>> Set Range...`
      - Set `YFrom` to `0` and `YTo` to `whatever number` and press `OK`
- Select `Rectangle` tool from Fiji GUI, and select an ROI on `96h_collagen` image (grayscale) and repeat the procedure above
  - _Note:_ You can use the same ROI as above by selecting the ROI rectangular box on `0h_collagen` image and then selecting `96h_collagen` image and doing `Edit > Selection > Restore Selection`
- To save all the images in the high quality, go to `Plugins > BioVoxxel Figure Toolbox > Export all images as SVG`
  - `Target folder` - folder of your choice to save all `SVG` images
  - `Export channels` - `Color`
  - `Lock critical ROIs [x]`  