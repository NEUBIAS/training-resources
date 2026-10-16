<h4 id="act2"><a href="#act2">Follow moving targets: the mask must chase the cells</a></h4>

Stimulated cells do not only signal, they also protrude and migrate toward the light. This turns targeted illumination into a way to steer cells, and it brings in the central difficulty of photomanipulation on live samples: the target moves, so a mask computed once is soon out of date. The loop has to recompute the mask from every new image.

- Run the feedback loop from the previous activity, but place each light spot slightly *above* its cell instead of on it: every stimulation now pulls the cell upward
- Let the loop run until the whole population has clearly moved up
- Link the per-frame detections into trajectories to see each cell's path, as in the figure at the top of the module. This is where **tracking** comes in: the steering decision needs no identities, but following and quantifying each cell's behavior over time does, because that means keeping cell identities across frames
- Then make the decision per object: steer cells in the left half of the field up and cells in the right half down. Only the decide step changes; acquisition and stimulation stay the same

![expected split-steering result](/training-resources/figures/smart_microscopy_photomanipulation_act2_split_expected.png)

- Explore the loop timing: what happens when the interval between iterations grows?
