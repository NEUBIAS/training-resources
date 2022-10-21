- Download [this two-channel image](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_8bit__membranes_nuclei.tif).
- Open the image in Fiji and measure the typical diameter of one cell.
- Open the image in Cellpose
  - `cell diameter: 60`
  - `chan to segment: red` (membranes)
  - `chan2 (optional): green` (nuclei)
  - Run the cyto model
    - Appreciate that the cell segmentation works well
  - Decrease the `cell diameter` to 1/5 of its correct value
  - Run the cyto model again
    - Appreciate that the segmenation does not work well
  - Put the `cell diameter` back to `60`
  - Run the nuclei model
    - Appreciate that also this does not work well
  - Appreciate that only the correct parameters and model yield a good result

### Debug a tricky case (optional)

- Download a [similar two-channel image](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__membranes_nuclei_hot_pixel.tif).
- Try to segment it in CellPose
- Appreciate that some cells are not segmented
- Try to find out why that could be the casd

### Explore additional parameters (optional)

Explore the `flow_threshold`, `cell_threshold` and `stitch_threshold` parameters


