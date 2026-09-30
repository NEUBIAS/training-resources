Install the simulator once with `pip install "virtual-microscope-teaching[gui]"` (Python 3.10 or newer), then run the blocks below one by one, for example as cells of a Jupyter notebook. The next activities continue in the same notebook, with the same microscope and viewer, so the whole module runs top to bottom.

#### Setup

The sample is the `optogenetic` simulation from the setup module: cells expressing optoFGFR (`mVenus` channel), ERK-KTR (`mScarlet` channel) and a nuclear marker (`miRFP` channel). In real-time mode the sample keeps changing while your code runs, as on a real microscope, and napari-micromanager shows every snap. `channel_layers=True` keeps one layer per channel, named after it, so that a loop snapping several channels shows all of them, not only the last one.

```python
import matplotlib.pyplot as plt
import numpy as np

from vmteach import load_microscope, run_experiment
from vmteach.gui import launch_gui
from vmteach.optogenetic import detect_nuclei, measure_activity

core, sim = load_microscope("optogenetic", n_cells=20, seed=0, mode="realtime")
viewer = launch_gui(core, channel_layers=True)
```

The image analysis uses two small helpers from `vmteach.optogenetic`: `detect_nuclei()` segments the nuclear marker with an Otsu threshold and returns the nucleus centroids, and `measure_activity()` computes each cell's C/N ratio of the reporter. They are deliberately simple reference implementations, not part of the microscope: they take plain images and return plain lists, so you can replace either of them with your own analysis (for example a deep-learning segmentation), and they work on images from a real microscope as well.

Snapping a channel always takes the same three core calls, so wrap them in a small helper:

```python
def snap(channel: str) -> np.ndarray:
    core.setConfig("Channel", channel)
    core.snapImage()
    return core.getImage()
```

#### Photoactivation, step by step

The experiment runs in the background with `run_experiment`, so the viewer stays live while it runs. The steps are written as one function; the blocks below build it up piece by piece, and the last block runs it.

**1. Image.** Find the cells in the nuclear marker channel, then measure the reporter in the ERK-KTR channel. `measure_activity()` computes each cell's cytoplasm-to-nucleus (C/N) ratio of the reporter and rescales it to 0 (resting) to 1 (fully active). It needs the nuclei image too, to know where each nucleus and its surrounding cytoplasm are.

```python
def image_cells():
    nuclei = snap("miRFP")
    cells = detect_nuclei(nuclei)
    ktr = snap("mScarlet")
    return cells, ktr, measure_activity(ktr, nuclei, cells)
```

**2. Create the mask.** Choose who gets light, here every cell in the left half of the field. The mask is a black-and-white image in camera pixels: white means light. A spot of light is a disk of pixels: all pixels closer to its centre than its radius.

```python
yy, xx = np.mgrid[0:512, 0:512]      # row (y) and column (x) of every pixel


def add_spot(mask, x, y, radius):
    """Switch on (255) all mask pixels within radius of (x, y)."""
    mask[(xx - x) ** 2 + (yy - y) ** 2 <= radius ** 2] = 255


def left_half_mask(cells, radius=25):
    targets = [(x, y) for x, y in cells if x < 256]
    mask = np.zeros((512, 512), np.uint8)
    for x, y in targets:
        add_spot(mask, x, y, radius)
    return targets, mask
```

**3. Stimulate.** Upload the mask to the SLM and expose with `CyanStim`. The snap delivers the light pulse and also records what the projected pattern looks like on the sample.

```python
def stimulate(mask):
    core.setSLMImage("SLM", mask)
    projected = snap("CyanStim")
    core.setSLMImage("SLM", np.zeros((512, 512), np.uint8))
    return projected
```

**4. Put it together.** Image, stimulate, wait for the pathway to respond (the full response takes about 5 s), image again, and check once more after 20 s in the dark:

```python
def photoactivation(run):
    cells, ktr_before, before = image_cells()
    targets, mask = left_half_mask(cells)
    projected = stimulate(mask)
    run.sleep(5)
    _, ktr_after, after = image_cells()
    run.sleep(20)
    _, _, later = image_cells()
    return dict(cells=cells, targets=targets, before=before, after=after,
                later=later, ktr_before=ktr_before, projected=projected,
                ktr_after=ktr_after)


run = run_experiment(photoactivation)     # returns immediately
```

In the viewer, watch the channels update and the nuclei of the targeted cells turn dark in the `mScarlet` layer. Note that `image_cells()` detects the cells again each time: they move a little between snaps.

#### Check the result

`run.wait()` returns what the experiment returned, after about 30 s:

```python
res = run.wait()
n_active = lambda acts: sum(a > 0.5 for a in acts)
print(f"{len(res['cells'])} cells, {len(res['targets'])} targeted, "
      f"{n_active(res['before'])} active before stimulation")
print(f"{n_active(res['after'])} active 5 s after the pulse")
print(f"{n_active(res['later'])} active 20 s later")

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
for ax, img, title in [(axes[0], res["ktr_before"], "ERK-KTR before"),
                       (axes[1], res["projected"], "projected light (CyanStim)"),
                       (axes[2], res["ktr_after"], "ERK-KTR 5 s after the pulse")]:
    ax.imshow(img, cmap="gray", vmin=0, vmax=255)
    ax.set_title(title)
    ax.axis("off")
plt.tight_layout()
plt.show()
```

About half of the cells should be targeted, none active before, the targeted ones active after the pulse, and (almost) none active again 20 s later.

#### Your first closed loop: keep the targeted cells active

A single pulse decays. A loop that measures every second and stimulates again exactly the cells whose activity has dropped keeps them active. No tracking is needed: every cycle detects and measures the cells again, and the decision only depends on each cell's current position and state.

```python
def keep_active(run, seconds=60, threshold=0.7):
    history = {"targeted": [], "others": []}
    for cycle in range(seconds):
        if run.stop_requested:
            break
        nuclei = snap("miRFP")                               # acquire
        cells = detect_nuclei(nuclei)                        # analyze
        activity = measure_activity(snap("mScarlet"), nuclei, cells)

        mask = np.zeros((512, 512), np.uint8)                # decide
        for (x, y), a in zip(cells, activity):
            if x < 256 and a < threshold:
                add_spot(mask, x, y, 25)

        if mask.any():                                       # actuate
            stimulate(mask)

        left = [a for (x, _), a in zip(cells, activity) if x < 256]
        right = [a for (x, _), a in zip(cells, activity) if x >= 256]
        history["targeted"].append(np.nanmean(left) if left else 0.0)
        history["others"].append(np.nanmean(right) if right else 0.0)
        run.sleep(1.0)
    return history


sim.reset()
history = run_experiment(keep_active).wait()                 # about one minute
```

Plot the mean activity of both groups over time:

```python
plt.figure(figsize=(7, 3))
plt.plot(history["targeted"], label="targeted cells (kept active by the loop)")
plt.plot(history["others"], label="untargeted cells")
plt.xlabel("time (s)")
plt.ylabel("mean ERK activity")
plt.legend()
plt.tight_layout()
plt.show()
```
