---
title: Smart microscopy feedback photomanipulation
layout: module
tags: ["workflow", "draft"]
prerequisites:
  - "[Getting started with the virtual microscope](../virtual_teaching_microscope)"
  - "[Segmentation overview](../segmentation)"
  - "[Thresholding](../binarization)"
  - "[Connected component labeling](../connected_components)"
objectives:
  - "Understand the general logic of a feedback-controlled experiment: acquire, analyze, decide, actuate"
  - "Implement an automated photomanipulation experiment: image the sample, compute a stimulation pattern, stimulate, and image the response"
  - "Apply per-object decision logic to stimulate different cells differently based on measured properties"
  - "Understand how feedback-control strategies can be used to drive a specific cellular behavior"
motivation: |
  Photomanipulation techniques use targeted light to actively perturb a biological sample rather than only observe it: photoactivation and photoconversion mark cells or proteins for tracking and sorting, photobleaching (FRAP) measures molecular turnover, and optogenetics switches engineered signaling proteins on and off with subcellular precision.

  Classically, the experimenter draws stimulation regions by hand before the experiment starts. This breaks down as soon as the target moves, deforms, or responds to the stimulus itself: a migrating cell leaves the drawn region within minutes. **Closed-loop feedback control** solves this: images are analyzed on the fly, and the stimulation pattern is recomputed from each new image, forming a feedback loop between the microscope and the biology. This enables experiments that are impossible manually: steering the migration of many individual cells in parallel, clamping signaling activity at a set level, or maintaining stimulation on a subcellular structure while the cell deforms.

  Smart microscopy experiments can be classified by what drives their decisions. The experiments in this module are **outcome-driven**: the loop's purpose is to *bring the sample into a desired state*, such as an activity level, a direction of migration, or a target pattern, and the specimen's response steers the next perturbation. In **event-driven** experiments, by contrast, analysis decides *what to image*, not what the sample should do (Related module: [Smart microscopy targeted imaging](../smart_microscopy_low_zoom_high_zoom)).

  This module can be worked through without access to a real microscope, using a microscope simulator (Related module: [Getting started with the virtual microscope](../virtual_teaching_microscope)). The code translates directly to microscopes that can be controlled with Micro-Manager; step-by-step guides for other microscope control software will be added in the future. All illustrations in this module were acquired with the virtual microscope.

concept_map: >
  graph TD
    A("Acquire image") --> B("Analyze<br>segment & measure objects")
    B --> C("Decide<br>compute stimulation pattern")
    C --> D("Actuate<br>targeted illumination (SLM/DMD/galvo)")
    D --> E("Sample responds<br>signals, moves, recovers")
    E --> A

figure: /figures/smart_microscopy_photomanipulation.png
figure_legend: >
  Closed-loop optogenetic steering on the virtual microscope. Left: one pass through the feedback loop; an illumination spot (blue) is placed above each detected cell, toward which it will protrude and migrate. Right: trajectories after one minute of closed-loop steering, each cell's path linked over time; the whole population moved up.

multiactivities:
  - ["smart_microscopy_photomanipulation/act1_photoactivation.md", [["pymmcore-plus (virtual microscope)", "smart_microscopy_photomanipulation/act1_photoactivation_vmteach.md"]]]
  - ["smart_microscopy_photomanipulation/act2_tracking.md", [["pymmcore-plus (virtual microscope)", "smart_microscopy_photomanipulation/act2_feedback_loop_vmteach.md"]]]
  - ["smart_microscopy_photomanipulation/act3_letter.md", [["pymmcore-plus (virtual microscope)", "smart_microscopy_photomanipulation/act3_letter_vmteach.md"]]]

assessment: >

  ### Scenario checks

    1. You run the steering experiment and the cells do not move. Name three different places the experiment can silently fail, and for each, one extra image or measurement that would expose it.

    > ## Solution
    > Any three of, for example: the analysis finds no or wrong cells (overlay the detections on the image); the mask is computed in the wrong place or coordinates (display the mask on top of the image); the light is never delivered, for example the stimulation channel is selected but never exposed (image the projected light and check it matches the mask); the light lands but the response is too weak or the sample does not respond (check a single cell with a strong manual stimulus). The habit to build: make every stage of the loop inspectable.
    {: .solution}

    2. An experiment stimulates the same hand-drawn region every 30 seconds for an hour. Give one experiment where this open-loop design is perfectly fine, and one where it quietly produces garbage.

    > ## Solution
    > Fine: the target does not move or respond, for example bleaching a region of a fixed sample, or activating a spot in a dish where position does not matter. Garbage: anything where the target moves, deforms, or reacts, for example migrating cells leave the region within minutes, so later pulses hit the wrong cells while the experiment looks like it is running normally.
    {: .solution}

    3. Between snapping an image and the light reaching the sample, the sample has changed. What two properties of your experiment decide whether this matters?

    > ## Solution
    > How fast the sample changes relative to the loop's latency, and how spatially precise the stimulation must be. A slow-moving cell hit by a generous spot tolerates seconds of delay; a subcellular target on a fast-moving edge does not. This is why latency is an experimental parameter, not an implementation detail.
    {: .solution}

    4. For each goal, decide whether the loop needs to keep cell identities across frames, and why: (a) keep every cell in the field active; (b) stimulate each cell exactly three times; (c) stimulate only cells that have been quiet for the last five minutes; (d) steer all cells to the left.

    > ## Solution
    > (a) No: re-detect and re-measure each cycle, the decision depends only on each cell's current state. (b) Yes: "three times" is per-cell history, so cells must be recognized across frames. (c) Yes: "quiet for five minutes" is also history. (d) No: every detected cell gets the same treatment each cycle. The rule: tracking is needed exactly when a decision depends on a cell's past, not only on its present.
    {: .solution}

    5. Now imagine the cells had no ERK activity reporter, only the nuclear marker. Which experiments from this module still work, and which require ERK-KTR?

    > ## Solution
    > The steering and letter experiments still work: their readout is position, which the nuclear marker provides. The photoactivation and keep-active experiments need ERK-KTR: without an activity readout, stimulation is still delivered, but nothing in the images reports whether the pathway responded, so the loop cannot verify or regulate activity.
    {: .solution}

    6. The activities use two image analysis helpers, `detect_nuclei(img)` and `measure_activity(ktr_img, nuclei_img, centroids)`. You want to replace them with your own, for example a deep-learning segmentation. What does each function take as input and return as output, so that the rest of the loop keeps working unchanged? And when would a centroid per cell not be enough?

    > ## Solution
    > `detect_nuclei` takes one image of the nuclear marker channel (a 2D array) and returns one `(x, y)` centroid per nucleus, in camera pixels. `measure_activity` takes the reporter image, the nuclear marker image of the same field and those centroids, and returns one number per centroid, in the same order: the activity between 0 (resting) and 1 (fully active), or `nan` where it could not be measured. Any replacement with the same inputs and outputs fits into the loop.
    >
    > Centroids are enough for everything in this module: placing a spot at an offset from the nucleus, and tracking. Other stimulation strategies need the whole segmentation, for example stimulating the edge of each cell rather than a spot next to its nucleus, or illuminating the entire cell body. A replacement should then return a label image (one integer per cell, 0 for background), from which centroids, outlines and edges can all be derived.
    >
    > The versions used in the activities, condensed from `vmteach.optogenetic` and written with numpy and `scipy.ndimage`:
    >
    > ```python
    > import numpy as np
    > from scipy import ndimage
    >
    >
    > def otsu_threshold(img):
    >     """The gray level that best separates dark from bright pixels (Otsu)."""
    >     p = np.bincount(img.ravel(), minlength=256) / img.size
    >     w = np.cumsum(p)                             # fraction of pixels below
    >     mu = np.cumsum(p * np.arange(256))           # their summed intensity
    >     between = (mu[-1] * w - mu) ** 2 / np.maximum(w * (1 - w), 1e-12)
    >     return np.argmax(between)
    >
    >
    > def label_nuclei(img):
    >     """Label image: threshold, then number the connected bright regions."""
    >     labels, _ = ndimage.label(img > otsu_threshold(img),
    >                               structure=np.ones((3, 3)))
    >     return labels
    >
    >
    > def detect_nuclei(img, min_area=20):
    >     """Nucleus centroids (x, y), without small specks and clipped nuclei."""
    >     labels = label_nuclei(img)
    >     h, w = img.shape
    >     centroids = []
    >     for i, (sy, sx) in enumerate(ndimage.find_objects(labels), start=1):
    >         ys, xs = np.nonzero(labels[sy, sx] == i)
    >         if len(ys) < min_area:
    >             continue                              # noise
    >         if sy.start == 0 or sx.start == 0 or sy.stop == h or sx.stop == w:
    >             continue                              # cut off by the border
    >         centroids.append((int(xs.mean()) + sx.start, int(ys.mean()) + sy.start))
    >     return centroids
    >
    >
    > def measure_activity(ktr_img, nuclei_img, centroids, lo=0.3, hi=1.2):
    >     """C/N ratio of the reporter per cell, rescaled to 0 (lo) .. 1 (hi)."""
    >     labels = label_nuclei(nuclei_img)
    >     img = ktr_img.astype(float)
    >     bg = np.percentile(img, 5)                    # camera background
    >     r = np.arange(-4, 5)
    >     disk = lambda radius: r[:, None] ** 2 + r[None, :] ** 2 <= radius ** 2
    >     activity = []
    >     for x, y in centroids:
    >         if labels[y, x] == 0:                     # centroid not on a nucleus
    >             activity.append(np.nan)
    >             continue
    >         nucleus = labels == labels[y, x]
    >         inside = ndimage.binary_erosion(nucleus, disk(1))
    >         ring = (ndimage.binary_dilation(nucleus, disk(4))
    >                 & ~ndimage.binary_dilation(nucleus, disk(1)))
    >         ring &= (labels == 0) & (img > bg + 8)    # cytoplasm, not background
    >         n = np.median(img[inside]) - bg
    >         c = np.median(img[ring]) - bg
    >         activity.append(np.clip((c / max(n, 1) - lo) / (hi - lo), 0, 1))
    >     return activity
    > ```
    >
    > The C/N ratio does not depend on how bright a cell is, which is why it is the standard readout of translocation reporters. On real data, calibrate `lo` and `hi` from resting and maximally stimulated control cells.
    {: .solution}

  ### Discuss with your neighbour

    1. For which photomanipulation experiments would an *open-loop* (pre-defined pattern) approach be sufficient, and where is feedback strictly required?
    2. What could you measure *during* the experiment to detect that your feedback loop is failing (segmentation errors, cells not responding)?
    3. Sketch a feedback experiment for your own project: what would the microscope measure, what would it decide, and what would it change on the sample? What is the fastest-changing thing in your sample, and what loop speed does that dictate?
    4. A feedback experiment makes decisions while you are at lunch. What would you log during the run so that you can trust the result afterwards?

learn_next:
  - "[Smart microscopy targeted imaging](../smart_microscopy_low_zoom_high_zoom)"
  - "[Smart microscopy - adjustment of the acquisition parameters](../smart_microscopy_acquisition_parameters)"
  - "[Object filtering](../object_filtering)"

external_links:
  - "[Optogenetic actuator-ERK biosensor circuits identify MAPK network nodes that shape ERK dynamics (Dessauges et al. 2022)](https://doi.org/10.15252/msb.202110670)"
  - "[Closed-loop optogenetic control of cell biology enables outcome-driven microscopy (Passmore et al. 2025)](https://doi.org/10.1038/s41467-025-67848-5)"
  - "[Real-time feedback control microscopy for automation of optogenetic targeting (Hinderling et al. 2025)](https://doi.org/10.1101/2025.08.17.670729)"
  - "[SMWG white paper: Smart microscopy, current implementations and a roadmap for interoperability](https://www.degruyterbrill.com/document/doi/10.1515/mim-2025-0029/html)"
  - "[FARO: Real-time feedback control microscopy for automation of optogenetic targeting](https://github.com/pertzlab/FARO)"
  - "[Smart Microscopy Exercise (H. Heil): analysis-driven targeted acquisition on real data](https://github.com/HannahSHeil/Smart-Microscopy-Exercise)"
  - "[trackpy: particle tracking for real pipelines](https://soft-matter.github.io/trackpy/)"
  - "[virtual-microscope-teaching: the simulator used in this module](https://github.com/hinderling/virtual-microscope-teaching)"
---

### Photomanipulation techniques at a glance

| Technique | What the light does | Feedback needed when… |
|---|---|---|
| Photoactivation / photoconversion | Switches a fluorophore on or changes its color, marking cells or proteins for tracking or sorting | targets are selected by phenotype found in the live image |
| Photobleaching (FRAP) | Destroys fluorophores in a region; the recovery reports molecular mobility | the bleached structure moves or is chosen automatically |
| Optogenetics | Activates engineered light-sensitive proteins that control signaling, motility, or gene expression | the cell moves/deforms, or activity must be held at a set level |
| Ablation | Destroys structures to probe mechanics and wound responses | the cut target is identified by on-the-fly analysis |

### The sample: an optogenetic actuator and a biosensor

This module is built around optogenetics and biosensor readouts, but the same feedback logic applies to any other photomanipulation technique. A large range of optogenetic actuators (light-controlled proteins that switch a cellular process on or off) and biosensors (fluorescent reporters of a cellular state) is available. The simulated sample used here combines one actuator and one biosensor into a circuit that activates and measures the MAPK/ERK signaling pathway, modelled after the optoFGFR and ERK-KTR circuit of Dessauges et al. (2022). A third label marks the nuclei:

| Component | Channel | Role |
|---|---|---|
| optoFGFR | `mVenus` | **Actuator**: a membrane-bound, light-sensitive receptor. Blue light switches it on, which activates the ERK pathway in exactly the illuminated cells. In the simulated sample, activated cells also protrude and migrate toward the light, which activities 2 and 3 use to steer them |
| ERK-KTR | `mScarlet` | **Biosensor**: a kinase translocation reporter. While ERK is inactive the reporter sits in the nucleus, so the nucleus is bright. When ERK activates, the reporter is exported to the cytoplasm and the nucleus turns dark. The translocation is reversible: once the light stops, the reporter returns to the nucleus within tens of seconds |
| H2B-miRFP | `miRFP` | **Nuclear marker**: labels the nuclei. They are compact and well separated, so they are easy to segment, which gives the cell positions and a nuclear mask for measuring the biosensor |

The ERK-KTR biosensor makes the response to optogenetic stimulation visible. To quantify it per cell, measure the reporter intensity inside the nucleus (using the nuclear mask from the `miRFP` channel) and in a thin ring of cytoplasm around it, and take the ratio: the cytoplasm-to-nucleus (C/N) ratio, the standard readout of translocation reporters. It rises when ERK activates, and because it is a ratio, it does not depend on how brightly each cell expresses the reporter.

![photoactivation, before and after](/training-resources/figures/smart_microscopy_photomanipulation_photoactivation_expected.png)

The stimulation light is delivered through the `CyanStim` channel: a blue LED whose light is shaped by a spatial light modulator (SLM), here a digital micromirror device (DMD). It works like a small projector that switches the stimulation light on or off pixel by pixel; the stimulation mask you compute is uploaded to it.

### Why a loop?

Cells move, deform, and respond to the stimulus itself, so a pattern drawn once is soon out of date. And many responses are transient: to keep a cell in a given state, it must be stimulated again and again. In both cases the next stimulation depends on what the sample is doing now, so the microscope has to keep measuring and deciding, in a feedback loop. Passmore et al. (2025) show how this outcome-driven approach can impose artificial cellular states, with the feedback correcting for cell-to-cell heterogeneity and drift over time.

Let's look at a single optogenetic activation pulse: the ERK response rises, and then decays as the reporter returns to the nucleus. A closed loop can measure each cell's activity in every cycle and re-stimulate exactly the cells whose activity has dropped, holding them in the active state. Below the traces, crops of the ERK-KTR channel around one cell per condition show the translocation directly (dark nucleus: active):

![single pulse versus closed loop](/training-resources/figures/smart_microscopy_photomanipulation_keep_active_expected.png)

This loop needs no tracking: every cycle detects the nuclei and measures their activity again, and the decision only depends on each cell's *current* state. Tracking becomes necessary only when a decision depends on a cell's *history*, or when cells must be followed as individuals over time, which is where activity 2 picks up.

### Stage 1, image analysis: from pixels to measurements

Every feedback experiment starts with an image-analysis pipeline that extracts *data* from the live images. Here we use a very basic approach with "classical" image analysis algorithms; in practice this step is often deep-learning based, for example for segmenting cells in label-free images. On a small crop with three cells:

![the analysis pipeline step by step](/training-resources/figures/smart_microscopy_photomanipulation_pipeline_explained.png)

1. **Acquire** the phase-contrast channel (what we display).
2. **Acquire** the nuclear marker channel (`miRFP`, what we analyze). Nuclei are compact and never touch, so they stay easy to segment even when cells crowd together.
3. **Threshold** the nuclei image. Related module: [Thresholding](../binarization).
4. **Label** connected regions and measure their centroids. Related modules: [Connected component labeling](../connected_components), [Measure shapes](../measure_shapes).

Nothing here is specific to smart microscopy, except that it must run *fast enough* to keep up with the sample.

### Stage 2, stimulation logic: from measurements to light

The extracted measurements feed the experiment's *control logic*: decide where the light should go, and physically deliver it.

![from decision to projected light](/training-resources/figures/smart_microscopy_photomanipulation_stimulation_logic.png)

1. **Decide**: turn per-cell measurements into planned illumination spots. Here, the spots are placed above the cell centroids, so that each cell migrates upward.
2. **Upload**: rasterize the plan into a binary mask on the SLM (white = light on). The pattern is loaded, but no light has reached the sample yet, because the SLM only *shapes* light.
3. **Deliver**: expose in the `CyanStim` channel, i.e. snap with the stimulation light selected. Only now, while the shutter is open, is the pattern projected onto the sample. The camera can image the projected light itself, which is how the alignment between mask and sample is verified on a real system.

### A note on timing

The sample does not wait for your software. While an image is being analyzed, the cells keep moving and signaling, so every decision is based on a slightly outdated picture of the sample, and every stimulation lands a little later than planned. Latency and loop frequency are therefore experimental parameters, as real as laser power or exposure time: a slower loop delivers fewer stimuli and acts on older information. The core rule of every feedback experiment: **the feedback loop must be faster than the biology it controls.** Activity 2 ends with an exploration that makes this failure mode visible.
