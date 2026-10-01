This continues the notebook of the previous activities: `core`, `sim`, `viewer`, `snap()`, `add_spot()` and `stimulate()` are already defined, and the microscope keeps running.

#### Setup

```python
from scipy import ndimage
from scipy.spatial import cKDTree
from vmteach.optogenetic import letter_mask

sim.reset(n_cells=75, base_radius=13.0)   # smaller, more numerous cells
SPEED = 5                                 # simulation only: 5x faster than real time
sim.speed = SPEED
target = letter_mask("N", fill=0.85, thickness=60)   # uint8, 255 inside the letter
show_mask(viewer, target, "target", color="orange")  # overlay in the viewer
```

`sim.reset()` rebuilds the population on the running microscope: smaller and more numerous cells than in the earlier activities, because cells are solid objects that need room on the stroke of the letter.

Real cells need minutes to assemble, and every attempt at a real microscope costs that long. A simulation can simply run faster: with `sim.speed = SPEED` the sample evolves five times faster than in real time, so wait `1.0 / SPEED` seconds per cycle to keep one second of cell time per cycle. About 50 cycles are enough for the letter to form, which takes 10 s instead of 50 s. On a real microscope `SPEED` is 1 and the rest of your script stays the same. One thing does not speed up: your own code. At `SPEED = 5`, 30 ms of analysis cost 0.15 s of cell behavior, so the information each mask acts on is proportionally older.

> ## Hint 1: what should each cell do?
> Treat each cell independently, exactly like in the split-steering activity: for every detected cell, decide **where its illumination spot should go**. A cell moves toward its spot, so aim each cell at a target pixel, and stop stimulating it once it has arrived.
{: .solution}

> ## Hint 2: finding the nearest target pixel
> `scipy.spatial.cKDTree` on the target coordinates does this in two lines:
>
> ```python
> from scipy.spatial import cKDTree
> target_pts = np.column_stack(np.nonzero(target)[::-1])  # (x, y) pairs
> tree = cKDTree(target_pts)
> dist, idx = tree.query([(cx, cy) for cx, cy in cells])
> ```
>
> Two catches, both worth discovering yourself first:
> - Don't place the spot *on* the possibly distant target pixel, because the cell only responds to light near its own body. Place the spot a fixed step (about 12 px) from the cell centroid, in the direction of the target pixel.
> - The nearest target pixel is always on the letter's *edge*. A cell that stops there is half outside. Aim at the stroke's **core** instead: `ndimage.distance_transform_edt(target > 0)` gives each letter pixel's distance to the letter edge, and pixels with distance of 14 or more are "deep". Use those as the routing targets, and consider a cell "arrived" when *its centroid* reaches a deep pixel.
{: .solution}

> ## Hint 3: my cells pile up and block each other!
> Two crowd-control problems appear, both real issues in tissue-patterning
> experiments:
>
> - **Everyone heads to the same spot.** Remove target pixels that are already claimed by a cell before the nearest-pixel query, so free cells are routed to *unoccupied* parts of the letter.
> - **The removal radius must respect cell spacing.** The simulated cells collide (and stop) when their centers come within roughly two cell radii (~28 px for `base_radius=13`). If you only remove a small disc around each settled cell, the next cell aims at a pixel directly beside an occupied one and gets blocked by the collision. Remove a disc of about the collision distance (~28 px) so every routing target is a spot where a cell can actually fit.
{: .solution}

> ## Solution
> Validated reference solution (50 cycles, about 10 s at `SPEED = 5`). Expect roughly 80 to 90% of the detected cells to settle on the target, forming a clearly legible letter as in the expected progression shown above, while pixel coverage stays around 40%. Perfect filling is not achievable, see the "Going further" questions.
>
> ```python
> dist_in = ndimage.distance_transform_edt(target > 0)
> DEEP = 14                                  # "core" of the letter stroke
> deep = (dist_in >= DEEP).astype(np.uint8) * 255
> deep_pts_all = np.column_stack(np.nonzero(deep)[::-1])
>
> def build_letter_mask(cells, step_px=12, spot_r=11, occupied_r=28,
>                       shape=(512, 512)):
>     mask = np.zeros(shape, np.uint8)
>     # routing targets: unoccupied core pixels, with cell-sized spacing
>     free_deep = deep.copy()
>     for cx, cy in cells:
>         free_deep[(xx - cx) ** 2 + (yy - cy) ** 2 <= occupied_r ** 2] = 0
>     pts = np.column_stack(np.nonzero(free_deep)[::-1])
>     if len(pts) == 0:                      # letter full, stop recruiting
>         pts = deep_pts_all
>     tree = cKDTree(pts)
>     for cx, cy in cells:
>         if dist_in[cy, cx] >= DEEP:
>             continue                       # settled: no stimulus, stays put
>         _, i = tree.query((cx, cy))
>         vx, vy = pts[i] - (cx, cy)
>         d = np.hypot(vx, vy)
>         if d == 0:
>             continue
>         s = min(step_px, d)
>         add_spot(mask, cx + s * vx / d, cy + s * vy / d, spot_r)
>     return mask
>
> def assemble(run):
>     for i in range(50):
>         if run.stop_requested:
>             break
>         cells = detect_nuclei(snap("miRFP"))   # acquire nuclei
>         snap("phase-contrast")                 # to follow the cells
>         mask = build_letter_mask(cells)
>         stimulate(mask)                        # expose the pattern
>         show_mask(viewer, mask, "stimulation")
>         run.sleep(1.0 / SPEED)                 # one second of cell time
>     return cells, snap("mScarlet")            # filled cell bodies for the metric
>
> sim.reset()
> cells, img = run_experiment(assemble).wait()   # watch the letter form live
> ```
>
> Metrics:
>
> ```python
> def otsu_threshold(img):
>     """The gray level that best separates dark from bright pixels (Otsu)."""
>     p = np.bincount(img.ravel(), minlength=256) / img.size
>     w = np.cumsum(p)                             # fraction of pixels below
>     mu = np.cumsum(p * np.arange(256))           # their summed intensity
>     between = (mu[-1] * w - mu) ** 2 / np.maximum(w * (1 - w), 1e-12)
>     return np.argmax(between)
>
> # the mScarlet reporter fills the whole cell body, so a threshold on it
> # gives a cell-pixel mask for the coverage metric
> cell_px = img > otsu_threshold(img)
> coverage = (cell_px & (target > 0)).sum() / (target > 0).sum()
> on_target = sum(1 for cx, cy in cells if target[cy, cx] > 0) / len(cells)
> print(f"target coverage {coverage:.0%}, cells on target {on_target:.0%}")
> ```
>
> The *cells on target* fraction is the fairer metric: pixel coverage can never reach 100% because the cells keep a collision distance. Like real cells, they cannot be packed arbitrarily densely.
{: .solution}

Explore the finished experiment in napari (`vmteach.gui.show_results`): overlay the stimulation masks and tracks to see exactly where your routing sent each cell. Tracking uses `vmteach.optogenetic.link_tracks`, a short Hungarian assignment with distance gating. On real data you would reach for a tracking library with the same detections-in, tracks-out interface: [trackpy](https://soft-matter.github.io/trackpy/), [btrack](https://github.com/quantumjot/btrack), or [motile](https://github.com/funkelab/motile).
