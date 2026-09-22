#### Introduction

This workflow for targeted imaging is built in **JOBS**, the smart microscopy acquisition workflow
module of NIS-Elements. A job organises tasks into a visual program. The key tasks used here are a
low resolution image capture, an image analysis of the low resolution image to segment target
objects, a list storing the segmented objects, a loop over that list, and finally a high resolution
capture of each target.

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
- **General Analysis** for segmentation of the target objects. General Analysis is standard in
  NIS-Elements; **General Analysis 3** is a licensed addition and is not required for this workflow.
- Two objectives, e.g. 4x / 0.2 NA for the low resolution overview and 40x / 0.95 NA for the high
  resolution acquisition.
- No microscope is needed to build and test the job: a camera can be simulated with standard
  NIS-Elements, which allows safe virtual testing on saved images. A Nikon representative can set
  this up if it is not already configured, and setting up the simulator will be described on
  protocols.io.

#### Practical requirements before you start

- This example job was designed for a standard slide with DAPI staining. However, any sample with a
  robust, bright stain can be substituted.
- The low and high resolution image parameters are stored in `capture definition` tasks, which each
  call an *optical configuration*. The optical configurations must be preset with appropriate
  hardware settings — filter set, LED power, camera exposure — to image the target well enough for
  successful segmentation or scientific analysis. It is possible to automate the adjustment of such
  hardware settings; the SMWG is planning a separate module on that.
- The `General Analysis` recipe must be predefined to segment the target object of interest, for
  example the three largest cells, or a dividing cell. Here it is a simple threshold segmentation.
  More complex segmentation is possible with General Analysis 3 and with Python in NIS-Elements.
- If reusing the example job, it is advised to point the capture definitions at your own optical
  configurations.

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

- Set up imaging settings
    - Define a low resolution capture definition (`Lo_Res`, e.g. 4x) and a high resolution capture definition (`Hi_Res`, e.g. 40x)
    - Save both as named **capture definitions** so that they can be referenced by the JOBS workflow and re-used across samples
- Acquire the overview image
    - Add a `Capture` task using the `Lo_Res` definition
- Set up image analysis
    - Add a `General Analysis` task operating on the captured overview image
    - Segment the target objects (here: nuclei) with a threshold
    - Restrict the result to the objects to be re-imaged, using `Filter on ObjectArea` → `by Order` → `Keep Top` (here: the 3 largest objects); additional feature filters such as circularity can be added
    - In the **Calculations** tab, define a region list (action `Replace`, division `Per Object`). Each segmented object becomes one region; the list is what the acquisition loop iterates over. Give it a descriptive name (here: `Found_Largest_3_Nuclei`)

<img src="{{ site.baseurl }}/figures/smart_microscopy_low_zoom_high_zoom/nikon_jobs_segmentation.png" alt="Low resolution capture followed by General Analysis segmentation keeping the top 3 objects by area" style="display: block; margin: 2px 0;" /><br>

<img src="{{ site.baseurl }}/figures/smart_microscopy_low_zoom_high_zoom/nikon_jobs_region_list.png" alt="General Analysis Calculations tab: defining the region list, one region per segmented object" style="display: block; margin: 2px 0;" /><br>

- Test the image analysis
    - Run the analysis on a saved example overview image and check that the expected objects are found before running the full workflow

<img src="{{ site.baseurl }}/figures/smart_microscopy_low_zoom_high_zoom/nikon_jobs_segmentation_result.png" alt="Result of the segmentation step: the three largest nuclei selected for high resolution re-imaging" style="display: block; margin: 2px 0;" /><br>

- Configure and run the feedback loop
    - Add a `Region Loop` iterating over `Found_Largest_3_Nuclei.Regions`
    - Inside the loop, add `Move to center of Regions.CurrentRegion`
    - Inside the loop, add a `Capture` task using the `Hi_Res` definition
    - Run the job

<img src="{{ site.baseurl }}/figures/smart_microscopy_low_zoom_high_zoom/nikon_jobs_module_tree.png" alt="Complete JOBS module tree for the targeted acquisition workflow" style="display: block; margin: 2px 0;" /><br>

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
