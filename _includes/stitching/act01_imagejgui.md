We will use the [basic stitching plugin](https://imagej.net/plugins/image-stitching) in ImageJ 
- Start the stitching plugin [Plugins › Stitching › Grid/Collection stitching]
- Set `Type` to **Grid: snake by rows** and `Order` to **Right & Down**
- We have 4 tiles set `Grid size x:` and `Grid size y` to **2**
- Set the § `Tile overlap [%]` to **5**
- Set `First file index` to  **1** 
- Set the directory where the zip file has been unpacked
- Set `names for tiles` to  **xyc_16bit__hoechst_phalloidin_tile_{ii}.tif**
- Set `Fusion method` to **Max. Intensity**
- Uncheck all the options
- Press `OK`

Repeat the procedure with different overlaps. When you have found the optimal overlap enable `[x] Compute overlap ..`
