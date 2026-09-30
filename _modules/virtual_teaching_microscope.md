---
title: Getting started with the virtual microscope
layout: module
tags: ["setup", "draft"]
prerequisites:
  - "Basic Python (variables, functions, running a script)"
objectives:
  - "Install the virtual microscope and launch its graphical user interface"
  - "Control the microscope programmatically: switch the objective, set the exposure, snap an image, set any device property"
  - "Explain how simulators (digital twins) help to develop and test smart microscopy workflows"
motivation: |
  A modern microscope is an imaging robot: its camera, stage, light sources and filters can all be controlled programmatically instead of through a graphical user interface. This enables custom automation, for example smart microscopy workflows in which the microscope analyzes its own images and decides what to do next.

  Developing such workflows on a real instrument is slow and risky: every test costs instrument time and samples, and a bug can damage hardware. This module introduces a **virtual microscope** that lets you develop and test workflows without access to real hardware. Because the sample is simulated too, it can do things a real sample cannot: for example, time can run faster than in reality, so you do not have to wait for slow biology to respond and can run many more tests.

  The virtual microscope builds on Micro-Manager and pymmcore-plus and implements exactly the same hardware interface as a real microscope running Micro-Manager. A script that works on the virtual microscope therefore runs on a real one after loading a different configuration file. In this module you install the virtual microscope, control it through its graphical user interface, and then do the same things from Python. Later modules reuse it, for example to learn how image feedback can automatically target specific regions with photostimulation.

concept_map: >
  graph TD
    G("GUI<br>(napari + napari-micromanager)") --> C("pymmcore-plus")
    S("Python script") --> C
    C --> V("Virtual microscope")
    C -.-> R("Real microscope")

figure: /figures/virtual_teaching_microscope.png
figure_legend: >
  The channels of the simulated sample, imaged on the virtual microscope. Cells express a nuclear marker (H2B-miRFP), a membrane-bound optogenetic receptor (optoFGFR-mVenus) and a kinase activity reporter (ERK-KTR-mScarlet). The composite shows the three fluorescence channels merged with pseudo-colors, as microscopy figures usually do.

multiactivities:
  - ["virtual_teaching_microscope/act1_gui.md", [["napari + Python", "virtual_teaching_microscope/act1_gui_napari.md"]]]
  - ["virtual_teaching_microscope/act2_script.md", [["napari + Python", "virtual_teaching_microscope/act2_script_vmteach.md"]]]

assessment: >

  ### Scenario checks

    1. You have booked time on a real microscope anyway. Why develop and test your control script on the virtual microscope first? Name two things that are faster or safer to get wrong on the simulator, and one thing only the real instrument can tell you.

    > ## Solution
    > Faster or safer on the simulator, for example: debugging analysis and control logic (a crash costs seconds, not a sample or a damaged objective), trying out acquisition strategies, and developing without occupying the instrument. Another one is reproducibility: the virtual microscope can restart exactly the same virtual sample, so when you change your code and run again, any difference in the result comes from your code. On a real microscope every run starts from different cells in a different state, so two runs are never directly comparable. Only the real instrument can tell you how the real biology responds and how your specific hardware behaves (illumination, focus drift, sample health, actual signal levels).
    {: .solution}

    2. Think of your last session at the microscope. Which steps could a script do for you by replaying what you clicked in the GUI, and which steps needed you to be there?

    > ## Solution
    > Replayable steps are the ones that don't require feedback: switching channels, setting exposures, moving through a list of stage positions, acquiring a time-lapse. Every GUI action is a call on the same core object scripts use, so these are straightforward to script. Steps that needed you were likely the ones where you looked at an image before deciding the next action: finding a good field of view, choosing which cells to image or stimulate, refocusing when the sample drifted. Automating those needs image analysis in the loop, the microscope reacting to its own images. That is feedback control, the topic of the follow-up modules.
    {: .solution}

    3. Your control script runs perfectly on the virtual microscope. On the real instrument it stops at the line that switches to a channel that does not exist there. Where would you look first, and what other differences should you expect between the two?

    > ## Solution
    > First in the configuration: channel presets are defined per instrument in its configuration file, so the real system needs a preset with that name, or the script must use the real system's name. Both microscopes expose the same interface, so many differences live in the configuration rather than the control logic. Do not expect it to end there, though: controlling real hardware is still difficult, and devices differ in subtle ways, for example cameras with a different bit depth or timing, stages that take time to travel and settle between positions, or light sources that need time to warm up. When you find that your system behaves differently in a way that matters for your script, consider modelling that behaviour in the simulator, so that the next test catches it before the real experiment does.
    {: .solution}

  ### Discuss with your neighbour

    1. What could a simulated microscope never tell you about your real experiment?
    2. Which quirk of your own microscope would you add to the simulator first, and how would it change the way you write your scripts?
    3. Think of the last experiment that went wrong at the microscope. Would any part of that failure have shown up while testing on a simulated instrument? Which part could only have failed on the real one?

learn_next:
  - "[Smart microscopy feedback photomanipulation](../smart_microscopy_photomanipulation)"
  - "[Smart microscopy targeted imaging](../smart_microscopy_low_zoom_high_zoom)"

external_links:
  - "[Micro-Manager: open-source microscope control](https://micro-manager.org/)"
  - "[pymmcore-plus documentation](https://pymmcore-plus.github.io/pymmcore-plus/)"
  - "[napari-micromanager plugin](https://github.com/pymmcore-plus/napari-micromanager)"
  - "[virtual-microscope-teaching: the simulator used in this module](https://github.com/hinderling/virtual-microscope-teaching)"
---

### The software stack

The virtual microscope combines several tools whose names can be confusing at first, because they are often mentioned together. From the hardware up to what you see on screen:

- **Micro-Manager** is open-source microscope control software. Its most valuable part is a library of drivers (device adapters) for hundreds of cameras, stages, light sources and filter wheels, all behind one common interface. It also has its own graphical user interface, which this module does not use.
- **pymmcore-plus** gives Python access to that common interface. Your script holds a `core` object and calls methods such as `core.snapImage()`, and the core forwards each call to whichever devices are loaded. It also adds conveniences on top, such as notifications when a device changes and an acquisition engine for time-lapses and multi-position experiments.
- **napari** is a Python image viewer, used across many image analysis workflows.
- **napari-micromanager** is a plugin that adds microscope controls to napari: snap, live view, channel and objective selection, exposure, stage control, acquisitions. Every control calls the same `core` object that your scripts use.
- **The virtual microscope** (the `virtual-microscope-teaching` Python package) plugs simulated devices into pymmcore-plus in place of real hardware, together with a simulated sample in front of the simulated camera. Everything above it, pymmcore-plus, napari-micromanager and your scripts, works exactly as with a real microscope.

This is what the virtual microscope looks like in napari, with the napari-micromanager toolbars at the top:

![napari with micro-manager toolbars](/training-resources/figures/virtual_teaching_microscope_napari_gui.png)

### Devices, properties and configurations

A few concepts from Micro-Manager appear in every script. They are the same on the virtual and on a real microscope.

**Device.** Each piece of hardware has a label, for example `Camera`, `XYStage`, `Objective` or `LED`.

**Property.** Every device has named properties that describe its state, for example the camera's `Exposure` and `Binning`, or the LED's `Label` (which light source is on). Each setting is therefore addressed by a triplet: **device**, **property**, **value**. `core.setProperty("Camera", "Binning", 2)` sets property `Binning` of device `Camera` to the value `2`, and `core.getProperty("Camera", "Binning")` reads the current value back.

The **Device Property Browser** shows exactly these triplets, one per row: the `Device-Property` column names the device and the property (`Camera-Binning`), the `Value` column shows the current value. Use it to explore which devices your microscope has and which properties each one offers, and to change them by hand. Anything you can change there, a script can change too with `core.setProperty`. The browser opens from the first button of the napari-micromanager toolbar (arrow); here it is docked on the right:

![the Device Property Browser docked in napari, and the toolbar button that opens it](/training-resources/figures/virtual_teaching_microscope_property_browser.png)

**Configuration group and preset.** A named combination of property values that are usually changed together. In the `Channel` group, the preset `miRFP` sets the LED to the red light source and the filter wheel to the matching far-red emission filter. One line applies both:

```python
core.setConfig("Channel", "miRFP")
```

It does exactly the same as the two separate property changes it stands for:

```python
core.setProperty("LED", "Label", "RED")
core.setProperty("Filter Wheel", "Label", "miRFP670(642/670)")
```

After either version, `core.getCurrentConfig("Channel")` reports `miRFP`: a preset is nothing more than a name for a set of property values. The Channel dropdown in the GUI applies these presets, and you can watch the `LED-Label` and `Filter Wheel-Label` rows of the property browser change when you switch it.

**Configuration file.** A plain text file that tells the core which devices to load, which device plays which role (the camera, the focus drive, ...), the configuration groups and presets, and the pixel size for each objective. Loading a different configuration file switches to a different microscope, for example from the virtual microscope to a real one. It is human-readable. An abridged excerpt of `MMConfig_demo.cfg`, the demo configuration that comes with Micro-Manager (its devices are Micro-Manager's built-in demo devices, but the file looks the same for real hardware):

```text
# Devices: label, device adapter (driver library), device in that library
Device,Camera,DemoCamera,DCam
Device,Emission,DemoCamera,DWheel
Device,Objective,DemoCamera,DObjective
Device,Z,DemoCamera,DStage
Device,XY,DemoCamera,DXYStage
...

# Roles: which device is the camera, the focus drive, ...
Property,Core,Camera,Camera
Property,Core,Focus,Z
...

# Labels: names for the positions of a filter wheel or turret
Label,Emission,0,Chroma-HQ620
Label,Emission,2,Chroma-HQ535
Label,Objective,1,Nikon 10X S Fluor
...

# Channel presets: group, preset, then device, property, value
ConfigGroup,Channel,DAPI,Emission,Label,Chroma-HQ620
ConfigGroup,Channel,FITC,Emission,Label,Chroma-HQ535
...

# Pixel size per objective, in um
ConfigPixelSize,Res10x,Objective,Label,Nikon 10X S Fluor
PixelSize_um,Res10x,1.0
```

Each preset line is again a device, property, value triplet, filed under a group and a preset name. On your own microscope, the configuration file is where to look up which devices it has and what its channel presets do. The virtual microscope's file follows the same format; its device lines load the simulated Python devices instead of hardware drivers.

The GUI controls you will use and the calls a script makes to do the same:

| GUI control | What it does | Script equivalent |
|---|---|---|
| Snap (camera icon) | acquire one image into the `preview` layer | `core.snapImage()`, then `core.getImage()` for the pixels |
| Live (film icon) | continuous acquisition | `core.startContinuousSequenceAcquisition()` |
| Channel dropdown | apply a channel preset | `core.setConfig("Channel", "miRFP")` |
| Objectives dropdown | switch the objective | `core.setStateLabel("Objective", "40x")` |
| Exposure box | exposure time in milliseconds | `core.setExposure(100)` |
| Stages Control (arrows icon) | move the stage | `core.setXYPosition(x, y)`, focus: `core.setPosition(z)` |
| Device Property Browser (table icon) | set any property of any device | `core.setProperty(device, property, value)` |

### The simulated sample

The virtual microscope can host different simulated samples. In this module and the modules that build on it, you will load the **optogenetic sample** (`load_microscope("optogenetic")`): live cells engineered with three fluorescent labels, plus a light-sensitive receptor whose role is explained in the follow-up module.

![every channel of the optogenetic sample](/training-resources/figures/virtual_teaching_microscope.png)

| Channel | Fluorophore labels | What you see |
|---|---|---|
| `phase-contrast` | (transmitted light) | all cells, label-free overview |
| `miRFP` | H2B, a histone: marks the nucleus | bright, well-separated nuclei on black |
| `mVenus` | optoFGFR, a membrane-bound receptor | the whole cell, slightly brighter at its edge, like a membrane stain |
| `mScarlet` | ERK-KTR, a kinase activity reporter | nucleus bright while the cell rests; the follow-up module puts this to work |
| `CyanStim` | (stimulation light path) | dark for now; used for photostimulation in the follow-up module |

Channels are named after the fluorophore, as they usually are on a real microscope, because the same fluorophore can label different proteins in different samples. The display colors in the composite are pseudo-colors chosen for contrast, not the emission colors.

### The devices of the virtual microscope

| Device | What it simulates |
|---|---|
| `Camera` | a 512 x 512 pixel, 8-bit camera with exposure, gain and binning (1, 2 or 4); photon and read noise, a few hot pixels |
| `Objective` | a turret with 4x, 10x, 20x, 40x and 60x objectives. The image always stays 512 x 512 pixels; the pixel size and the field of view change, as on a real microscope |
| `XYStage` | moves the sample: two square wells side by side, with travel limits at the well edges |
| `ZStage` | the focus drive: moving away from the focal plane blurs the image |
| `LED` | the excitation light source, with several selectable wavelengths |
| `Filter Wheel` | the emission filters, one per fluorophore |
| `Shutter` | opens and closes the light path during acquisitions |
| `SLM` | a spatial light modulator (a DMD) that shapes the stimulation light into a pattern; used in the follow-up module |

### What the simulation is, and is not

The simulated sample is a toy model: cells are soft shapes that crawl, protrude and bump into each other, and respond to light in a simplified way. It is designed to be easy to analyze, not to reproduce real cell biology, so do not draw biological conclusions from it. Nothing in the design prevents replacing it with a more realistic biophysical model; the virtual microscope can host different simulated samples, and the microscope side stays the same.

The microscope side reproduces what your control code interacts with: the devices, channels and presets, exposure and binning, objectives with their pixel sizes, optical blur and camera noise, and a stage with limits. It is not a perfect copy of real hardware either. The stage arrives at a new position instantly, where a real stage needs time to travel and settle. Filter wheels and light sources switch without delay, nothing drifts out of focus on its own, devices never time out or report errors, and the stimulation pattern lands exactly where it was meant to, where a real projector needs calibration. Treat a script that works on the simulator as ready for a first test on the real instrument, not as finished.

By default, the simulated sample evolves in real time while your code runs, like on a real microscope: your scripts wait with `time.sleep` as they would at the instrument, and the GUI shows every snap, channel switch and stimulation pattern live while an experiment runs. A simulator also offers two things a real sample never does. It can run **faster than real time** (`speed=10`: ten seconds of cell behavior per second of waiting), so slow biology such as migration can be tested in seconds. And in **stepped mode** (`mode="stepped"`), time advances only when your code says so (the `advance()` helper), so every run starts from exactly the same virtual sample and gives exactly the same result, on every machine. Automated tests and figure generation rely on that.
