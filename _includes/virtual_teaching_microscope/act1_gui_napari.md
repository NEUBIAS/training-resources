#### Installation

```bash
pip install "virtual-microscope-teaching[gui]"
```

(Python 3.10 or newer. For the scripted part you can use any Python console or Jupyter. In Jupyter, run `%gui qt` first.)

#### Launch the microscope

The first argument of `load_microscope` picks the simulated sample; use `"optogenetic"` here and in the follow-up modules.

```python
from vmteach import load_microscope
from vmteach.gui import launch_gui

core, sim = load_microscope("optogenetic", n_cells=20, seed=0)
viewer = launch_gui(core)
```

napari opens with the napari-micromanager control toolbars, as in the screenshot in the module introduction.

#### Explore like at a real microscope

- Press **Snap** (camera icon): a `preview` layer appears
- Press **Live** (film icon) for continuous acquisition: the cells ruffle and crawl
- **Objectives** dropdown: switch 10x to 40x and the field of view shrinks around the current stage position. 4x shows a large overview
- **Channel** dropdown: step through phase-contrast, miRFP, mVenus and mScarlet with Live running, and match what you see to the channel gallery. The fifth entry, CyanStim, is the stimulation light path used in the follow-up module; for now it shows a dark frame
- **Exposure**: increase and decrease it, and observe brightness and noise
- **Stages Control** (arrows icon in the toolbar): step the stage and watch new cells come into view. The two wells are 2048 um wide; at 4x, move toward the edge of a well until its wall and rounded corner appear in phase contrast
- **Device Property Browser** (table icon, the first in the toolbar): switch the Channel dropdown and watch the `LED-Label` and `Filter Wheel-Label` rows change, since that is all a channel preset does. Then set `Camera-Binning` to 2: the image shrinks to 256 x 256 pixels and gets four times brighter, because each pixel now sums 2 x 2 sensor pixels. Lower the exposure to compensate, and set the binning back to 1
