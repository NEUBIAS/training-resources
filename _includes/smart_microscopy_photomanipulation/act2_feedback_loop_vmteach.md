This continues the notebook of the previous activity: `core`, `sim`, `viewer`, `snap()`, `add_spot()` and `stimulate()` are already defined, and the microscope keeps running. Run the blocks below one by one.

#### Setup

Stimulated cells protrude and migrate toward the light, so a spot placed slightly *above* a cell pulls it upward. Because the cells move, the mask must be recomputed from every new image: a feedback loop. Two more helpers are needed: `link_tracks` for tracking, and `overlay` to draw a mask on an image.

```python
import time

from vmteach.gui import show_mask
from vmteach.optogenetic import link_tracks, overlay
```

#### One pass through the loop

Acquire the nuclear marker channel and detect the cells, with the same pipeline as in the previous activity:

```python
cells = detect_nuclei(snap("miRFP"))
phase = snap("phase-contrast")
print(f"detected {len(cells)} cells")
```

Decide: one spot per cell, offset upward. The offset direction is the entire steering logic.

```python
def build_steer_mask(cells, dy=-15, spot_radius=11, shape=(512, 512)):
    """One illumination spot per cell, offset by dy pixels in y."""
    mask = np.zeros(shape, dtype=np.uint8)
    for cx, cy in cells:
        add_spot(mask, cx, cy + dy, spot_radius)
    return mask


mask = build_steer_mask(cells)
plt.imshow(overlay(phase, mask))
plt.title("stimulation mask (blue): one spot above each cell")
```

Actuate with `stimulate()` from the previous activity: upload the mask and expose with `CyanStim`.

```python
stimulate(mask)
```

#### Close the loop

Acquire, analyze, decide, actuate, wait, repeat. Each cycle snaps `miRFP` to find the cells and then `CyanStim` to deliver the new mask: forget the `CyanStim` exposure and nothing happens, a classic debugging moment at a real microscope. The loop also snaps `phase-contrast`, so that you can follow the cells in the viewer, and `show_mask` puts the current mask on top, so you can see the spots follow the cells.

```python
n_cycles = 60                                   # one minute


def steer_up(run):
    detections = []
    for i in range(n_cycles):
        if run.stop_requested:
            break
        cells = detect_nuclei(snap("miRFP"))    # acquire + analyze
        phase = snap("phase-contrast")          # to follow the cells
        mask = build_steer_mask(cells)          # decide
        stimulate(mask)                         # actuate
        show_mask(viewer, mask, "stimulation")
        detections.append(cells)
        run.sleep(1.0)                          # the sample responds
    return detections, phase


sim.reset()
run = run_experiment(steer_up)                  # returns immediately
```

The loop runs in the background, so the notebook stays usable; `run.stop()` ends it early. Wait for it to finish:

```python
detections, phase = run.wait()
```

#### Tracking: what did each cell do?

The steering decision never needed cell identities, but following and quantifying each cell over time does. `link_tracks()` links the per-frame detections into trajectories (Hungarian assignment with a distance gate); real pipelines use a tracking library such as trackpy.

```python
rows = link_tracks(detections)                  # columns: id, frame, y, x

dys = []
for tid in np.unique(rows[:, 0]):
    tr = rows[rows[:, 0] == tid]
    if len(tr) >= 10:
        tr = tr[np.argsort(tr[:, 1])]
        dys.append(tr[-1, 2] - tr[0, 2])
print(f"{len(dys)} tracks, mean displacement {np.mean(dys):+.0f} px (negative = up)")
```

The mean y position of all nuclei in the first and last frame would not show the movement: the whole population moves, so cells leave the field at the top while new ones enter from below. Displacement along each track does.

Draw the trajectories on the last phase-contrast image of the loop. Use this image and not a new snap: the cells keep moving, and a later image no longer matches the ends of the tracks.

```python
def plot_tracks(rows, color_of, min_len=5):
    """Plot each track as a line (x, y over time), colored by color_of(track)."""
    for tid in np.unique(rows[:, 0]):
        tr = rows[rows[:, 0] == tid]
        if len(tr) < min_len:
            continue
        tr = tr[np.argsort(tr[:, 1])]            # sort by frame
        plt.plot(tr[:, 3], tr[:, 2], color=color_of(tr), lw=2)


plt.imshow(phase, cmap="gray")
plot_tracks(rows, lambda tr: "green")
plt.title("one-minute trajectories: everyone went up")
```

#### Per-object decisions

Steer each cell differently based on a measured property: cells left of the midline go up, cells right of it go down. Only the decide step changes; acquisition and actuation stay the same.

```python
def build_split_mask(cells, offset_px=15, spot_radius=11, shape=(512, 512)):
    mask = np.zeros(shape, dtype=np.uint8)
    for cx, cy in cells:
        dy = -offset_px if cx < shape[1] // 2 else +offset_px   # the decision
        add_spot(mask, cx, cy + dy, spot_radius)
    return mask


def steer_split(run):
    detections = []
    for i in range(n_cycles):
        if run.stop_requested:
            break
        cells = detect_nuclei(snap("miRFP"))
        phase = snap("phase-contrast")
        mask = build_split_mask(cells)
        stimulate(mask)
        show_mask(viewer, mask, "stimulation")
        detections.append(cells)
        run.sleep(1.0)
    return detections, phase


sim.reset()
detections, phase = run_experiment(steer_split).wait()
```

Draw the tracks again, colored by the half of the field each cell started in: green for up, purple for down.

```python
def by_start(tr):
    return "green" if tr[0, 3] < 256 else "purple"


plt.imshow(phase, cmap="gray")
plot_tracks(link_tracks(detections), by_start)
plt.axvline(256, color="w", ls="--")
plt.title("left half steered up, right half steered down")
```

One measurement per cell, here its x position, is enough to give every cell its own treatment. Any other measured feature works the same way: size, intensity, shape, or biosensor activity.

#### Explore the timing

The loop timing is the most important parameter of any feedback experiment. Re-run the up-steering loop with `run.sleep(5.0)` instead of `run.sleep(1.0)`: the same minute now contains five times fewer stimulations, and each mask acts on older information. The steering becomes weaker or fails.

The sample keeps moving while your code runs, so the duration of your analysis is part of the experiment too. Add `time.sleep(2)` between the analyze and decide steps (a slow segmentation) and watch the spots land where the cells used to be. This is exactly the situation on a real microscope.
