  - Open the 3D multi-channel image [xyzc_8bit_beads_p_open.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit_beads_p_open.tif) by dragging and dropping it in the Napari viewer.
  - Note that the channel and z-dimension both appear as sliders.
  - In order to see the different channels of the image simultaneously, the two channels have to be on different layers. One way to achieve this is the following:
    1. Open the Napari console.
    2. Observe the 'shape' of the data by typing `viewer.layers[0].data.shape`. You should get `(41, 2, 297, 284)`. This means that the dimensions in the data are in the order ZCYX since we have two channels.
    3. Swap the Z and C dimension with numpy:
          - `import numpy as np`
          - `viewer.layers[0].data = np.transpose(viewer.layers[0].data, (1, 0, 2, 3))`
          - You can now split the stack by right-mouse clicking on the image layer and selecting 'Split Stack'.
          - Observe that you now have two layers, one for each channel, that have distinct colors in the Napari viewer.
    4. The image is not calibrated. To take the calibration into account, you can specify it like this: `viewer.layers[0].scale = (0.1000000, 0.0222057, 0.0222057)` and `viewer.layers[1].scale = (0.1000000, 0.0222057, 0.0222057)`. It is also possible to use the AICSImage plugin to read in the calibration metadata (see the Spatial Calibration module).
