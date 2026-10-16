#### The GUI reacts to your code

Keep the napari window from the previous activity open. In the same Python session, run these one at a time and watch the GUI while each executes:

```python
core.snapImage()                        # = pressing "Snap"; the preview layer updates
core.setStateLabel("Objective", "20x")  # = selecting "20x"; the dropdown follows
core.setConfig("Channel", "miRFP")      # = selecting "miRFP" in the Channel dropdown
core.setExposure(50.0)                  # = typing 50 in the Exposure box
core.snapImage()
```

The dropdowns now show 20x, miRFP and 50 ms: the GUI is a viewer onto the same `core` object your script controls.

#### Any property, and the stage

The Device Property Browser and your script read and write the same properties. With the browser open, run:

```python
print(core.getProperty("LED", "Label"))         # the LED the miRFP preset selected
core.setProperty("Camera", "Binning", 2)        # watch the Binning row change
core.snapImage()
print(core.getImage().shape)                    # (256, 256)
core.setProperty("Camera", "Binning", 1)

print(core.getXYPosition())                     # stage position, um
core.setXYPosition(500.0, 0.0)                  # 500 um to the right: new cells
```

#### An image is just an array

Scripts do one thing the GUI cannot: hand the pixels to your own analysis code.

```python
import matplotlib.pyplot as plt

core.snapImage()
img = core.getImage()               # a plain numpy array
print(img.shape, img.dtype, img.max())
plt.imshow(img, cmap="gray")
```

This is the bridge to everything that follows: once the image is an array, any image analysis can run on it, and its result can drive the next microscope command.

#### Reset for the next module

```python
core.setXYPosition(0.0, 0.0)
core.setStateLabel("Objective", "10x")
core.setConfig("Channel", "phase-contrast")
core.setExposure(50.0)
```
