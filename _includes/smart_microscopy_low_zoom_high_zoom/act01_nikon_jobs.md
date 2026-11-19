#### Introduction

This workflow for targeted imaging is built in **JOBS**, the smart microscopy acquisition workflow
module of NIS-Elements. A job organises tasks into a visual program. The key tasks used here are a
low resolution image capture, an image analysis of the low resolution image to segment target
objects, a list storing the segmented objects, a loop over that list, and finally a high resolution
capture of each target.

#### Goal of the procedure
Here we want to implement a simple pipeline to detect cells in a large FoV in DAPI and then focus on some of them with a high zoom for multiple dyes.

Steps:

- Perform large FoV in widefield at different registered positions
- For all positions:
  - go to the position, perform autofocus.

    > **Note:** [autofocus not implemented yet]
  - acquire and detect cells in (DAPI) low resolution large FoV.
  - For a defined number of cells, switch to high resolution and acquire all desired dyes.

<div class="mermaid">
---
config:
  layout: elk
---
flowchart TD
    subgraph Setup [" "]
        direction LR
        L["Define low-resolution capture<br/>Lo_Res"]:::setup
        H["Define high-resolution capture<br/>Hi_Res"]:::setup
    end
    O["Capture overview image<br/>using Lo_Res"]:::capture
    A["Analyse overview image<br/>identify target regions"]:::analysis
    F{"For each target region"}:::loop
    T["Capture high-resolution image<br/>using Hi_Res"]:::capture
    R(["Output target images"]):::finish
    L --> O
    H --> T
    O --> A
    A --> F
    F --> T
    T -->|Next region| F
    F -->|All regions complete| R
    classDef setup fill:#eef2ff,stroke:#818cf8,color:#1e1b4b;
    classDef capture fill:#ecfeff,stroke:#22d3ee,color:#164e63;
    classDef analysis fill:#f5f3ff,stroke:#a78bfa,color:#3b0764;
    classDef loop fill:#fff7ed,stroke:#fb923c,color:#7c2d12;
    classDef finish fill:#fefce8,stroke:#facc15,color:#713f12;
    style Setup fill:none,stroke:none;
</div>

This description assumes working familiarity with NIS-Elements. A fuller walkthrough, including how
to set up the simulated camera, is being published separately on protocols.io.

#### Hardware and software requirements

- Nikon microscope with a motorised XY stage, controlled by NIS-Elements.
- **JOBS** module (licensed) for defining the acquisition workflow.
- **General Analysis** for segmentation of the target objects. **General Analysis** is standard in NIS-Elements; **General Analysis 3** is a licensed addition and is not required for this workflow.
- Two objectives, e.g. 4x / 0.2 NA for the low resolution overview and 40x / 0.95 NA for the high resolution acquisition.
- No microscope is needed to build and test the job: a camera can be simulated with standard NIS-Elements, which allows safe virtual testing on saved images. A Nikon representative can set this up if it is not already configured, and setting up the simulator will be described on protocols.io.

#### Sample requirement

The pipeline relies on finding nuclei (even if it can be directly used for other cases), therefore we recommend preparing a HeLa cells sample with DAPI and whatever other dyes you desire. This example job was designed for a standard slide with DAPI staining. However, any sample with a robust, bright stain can be substituted.


#### Practical requirements before you start

The low and high resolution image parameters are stored in `capture definition` tasks, which each call an optical configuration. The optical configurations must be preset with appropriate hardware settings — filter set, laser power, camera exposure — to image the target well enough for successful segmentation or scientific analysis. It is possible to automate the adjustment of such hardware settings; the SMWG is planning a separate module on that.
The `General Analysis` recipe must be predefined to segment the target object of interest, for example the three largest cells, or a dividing cell. Here it is a simple threshold segmentation. More complex segmentation is possible with General Analysis 3 and with Python in NIS-Elements.
If reusing the [example job](https://github.com/NEUBIAS/training-resources/raw/master/_includes/smart_microscopy_low_zoom_high_zoom/nikon_jobs/targeted_imaging.bin), it is advised to point the capture definitions at your own optical configurations. The job file contains the capture definitions it was built with, and those call optical configurations that exist on the microscope it was made on. They will not match another system, so after importing, point each capture definition at your own optical configurations before running anything. The version of NIS-Elements the files were saved from, and the names of the optical configurations the job expects, are listed in `README.txt` in the same folder.

#### Sources

- Detailed protocol on [protocols.io](http://protocols.io)

  > **Note:** (broken link)

- [Example job (.bin)](https://github.com/NEUBIAS/training-resources/raw/master/_includes/smart_microscopy_low_zoom_high_zoom/nikon_jobs/targeted_imaging.bin)

  > **Note:** (broken link)

- [General Analysis recipe (.ga)](https://github.com/NEUBIAS/training-resources/raw/master/_includes/smart_microscopy_low_zoom_high_zoom/nikon_jobs/targeted_imaging_segmentation.ga)

  > **Note:** (broken link)

#### Hazard considerations

- Before attempting this on a real microscope, check the focus-height and XY offsets between the low
  resolution and high resolution objectives before running the workflow unattended.
- Before running a job on hardware, be sure that no XY or Z crash can happen. Check the clearance of
  tall high-magnification objectives against the slide or plate holder over the full range of stage
  positions that the workflow may visit.
- Take care when mixing air and immersion objectives at the same XY position.

#### Reusing the example job

The job and its analysis recipe can be downloaded and imported into NIS-Elements:

- [Example job (`.bin`)](https://github.com/NEUBIAS/training-resources/raw/master/_includes/smart_microscopy_low_zoom_high_zoom/nikon_jobs/targeted_imaging.bin)
- [General Analysis recipe (`.ga`)](https://github.com/NEUBIAS/training-resources/raw/master/_includes/smart_microscopy_low_zoom_high_zoom/nikon_jobs/targeted_imaging_segmentation.ga)

The job file contains the capture definitions it was built with, and those call optical
configurations that exist on the microscope it was made on. They will not match another system, so
after importing, point each capture definition at your own optical configurations before running
anything. The version of NIS-Elements the files were saved from, and the names of the optical
configurations the job expects, are listed in `README.txt` in the same folder.

#### Step-by-step guidelines
1. Set up imaging settings (optical configuration panel)
   Define optical settings to detect nuclei and see wanted features. For that you have to tweak the optical parameters and then save them : New Optical Configuration > name : DAPI_LowZoom, > Finish

   | name to use | short description |
   | --- | --- |
   | `DAPI_LowZoom` | create a DAPI configuration for your 4x, with sufficient SNR to detect nuclei |
   | `DAPI_HighZoom` | create a DAPI configuration for your 40x |
   | `CY3_HighZoom` | create a CY3 configuration for your 40x |
   | `GFP_HighZoom` | create a GFP configuration for your 40x |
   {: style="width: auto"}

2. Capture an image at the DAPI_LowZoom configuration, 4x

3. Set up the JOBS layout

   To create a step in JOBS, use the Search bar to find it, then drag and drop it. To remove one, drag and drop it out of the JOBS list.

   - create a **capture definition**, name it `LowZoom`, using `DAPI_LowZoom` optical configuration
   - create a **capture definition**, name it `HighZoom`, using `DAPI_HighZoom`, `CY3_HighZoom` and `GFP_HighZoom` optical configurations
   - create a **new region list**, name it `nuclei_list`
   - create a **select objective**, to 4x
   - create a **Capture**, name it `image_Low_Zoom`, using `LowZoom`
   - create a **General Analysis**, name it `analysis_nuclei`. See part 4 for its settings.
   - create a **select objective**, to 40x
   - create a **Region Loop** and set it to `nuclei_list`
   - inside the Region Loop, create a **Move to center of Regions**
   - inside the Region Loop, create a **Capture**, name it `image_HighZoom`, using `HighZoom`
   - below the loop, outside of it, create a **select objective**, to 4x

4. Defining the General Analysis

   - Rename it `analysis_nuclei`
   - Select its application channel : Analysis Palette > Add Channel > `DAPI_LowZoom`
   - Filter the image with Preprocessing > Denoising > Median and put it to 4
   - Update the Threshold boundaries and look at the previously captured image. The selected thresholded cell should appear in highlight
   - Select only the 3 biggest : Binary Process > Filter Object (Top 10) > ObjectSize > ObjectArea : put its count to 3
   - Now that we have a binary channel we can add a calculation (it's what will extract positions): Analysis Palette > Add Calculations
   - Define regions > select `nuclei_list` in Region
	   - Objects : `DAPI_LowZoom`
	   - Action : Append
	   - Region Division : Per Object

5. Run it

   - Click on the green triangle to start the JOBS
#### Notes on the segmentation step

Two segmentation strategies were tested for finding the target objects:

- **Bright spot detection**, with typical diameter and contrast as parameters. It takes object shape into account as well as intensity, which for round objects such as nuclei usually makes it the more robust of the two. Like thresholding, it returns a set of objects, which are then filtered down to the targets.

<img src="{{ site.baseurl }}/figures/smart_microscopy_low_zoom_high_zoom/nikon_jobs_segmentation_single_object.png" alt="Bright spot detection, filtered to a single target object" style="display: block; margin: 2px 0;" /><br>

- **Threshold + `Keep Top` N by area**, optionally combined with circularity filtering. Less shape-aware than bright spot detection, but simple to set up. Its result on the same field is the three-object image shown under *Test the image analysis* above.

Thresholding is used in this example because it is the easier of the two to set up and to follow. On
a cleaner sample — cultured nuclei, for instance — bright spot detection would be the better choice.
Either way, the choice of *how* objects are detected is independent of the feedback loop itself, and
swapping one for the other changes nothing else in the job. More complex methods, such as Cellpose or
ConvPaint, are also available in NIS-Elements.
