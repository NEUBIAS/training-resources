
# Introduction

<p>
    <img width="3319" height="1810" alt="Guided_Acquisition_UI_two_columns" src="/_includes/smart_microscopy_low_zoom_high_zoom/figures/Guided_Acquisition_UI_two_columns.png" />
    <em>Figure 1: User interface of Guided Acquisition tool in ZEN blue.</em>
</p>

---

This workflow employs the Guided Acquisition UI Tool in ZEN (Figure 1). It follows a fixed workflow, where an overview scan is followed by an image analysis block and several detailed scans. Positions (FOVs) of the detailed scans are derived from the image analysis. To keep the user interface simple, the user plugs in pre-configured experimental and image analysis settings for the three main steps. 

Besides simplifying usability, this comes with the benefit that all available acquisition modes and other built-in features (like Deep Learning segmentations) also seamlessly work with GA. The user can furthermore add certain optional components, e.g. additional processing steps for the raw overview image, or manually adjust the number of detailed scans. Time-lapse acquisitions can be defined to allow for detection of sparse events. GA also is compatible with image data correlation via ZEN Connect, or high throughput well plate experiments.

___

# Pre-requisites
- Zeiss Imaging instrument (e.g. AxioObserver, LSM)
- ZEN blue as the imaging control software
- Smart Acquisition Toolkit


# Detailed guidelines
<p>
    <img width="3124" height="1144" alt="Graphical_workflow" src="https://github.com/user-attachments/assets/99144364-3ac0-4ca2-994b-28d7bcabf2dd" />
    <em>Figure 2: Guided Acquisition is configured by first configuring the individual acquisition and analysis settings, and then incorporating them into the GA setup. </em>
</p>

***Overview Scan***

For setting up the overview scan, the user must navigate to the "Acquisition" tab and create a new acquisition setting. Within the workflow, the overview scan serves first and foremost the detection of ROIs for targeted acquisition. Hence, image quality must be sufficient to reliably detect the desired phenotype, but imaging settings should otherwise be chosen to keep scan time and data sizes as slim as possible. There is several ways of reducing acquisition effort in this step:
- only acquire channels that are strictly required for ROI identification
- employ a low-magnification objective or binning
- only acquire a number of tiles that guarantees detecting your desired number of ROIs / phenotypes, not more
- avoid large stacks

***Image Analysis***

For the detection of events or phenotypes, the GA module employs the ZEN-internal Image Analysis. This gives the user many choices concerning segmentation methods, object hierarchies and feature filtering. Hence, it offers high flexibility in pursuing hard-to-detect phenotypes or events. For setting up the image analysis, the user must navigate to the "Image Analysis" tab. The wizard-like tool will lead through the setup in a step-wise fashion.
- [Segmentation Method] When creating a new analysis setup, the user can choose between default 2D segmentation methods, Zone-of-influence (an automatic detection of nuclei and cell bodies) and 3D segmentation.
- [Segmentation Classes] Next, the segmentation classes can be defined, hence, the types of objects-of-interest (e.g. nuclei, whole cells, organelles, or nuclear speckles). These can also be defined in a hierarchy to increase specificity of results (e.g. "nuclear speckles" within "nuclei". For every class, the underlying image channel can be adjusted
- [Segmentation Algorithm] Then, the segmentation algorithm is defined. Here, the Image Analysis Wizard offers great flexibility. Threshold-based segmenters (manual and automatic), variance-based segmenters, ML-based segmenters (Intellesis) and DL-based segmenters are available. The user can further do some limited pre-processing, rudimentary object filtering and morphological operations (e.g. watershed object splitting)
- [Feature Filtering] Then, the detected objects can be further selected via feature filters. Combining features allows for high specificity. Cut-off values can be typed in manually or defined interactively by including / excluding desired objects in the image pre-view.
- [Result features] Finally, result features can be defined. These are features that are measured and reported back to the user after execution of the image analysis. In the context of GA, these features allow for a selection of detailed scans. E.g. a user might want to create detailed images only from the 5 largest nuclei (feature: "Area") of a data set.

***Detailed Scan***
For setting up the detailed scan, the user must navigate to the "Acquisition" tab and create a new acquisition setting. The detailed scan is the final result of the GA workflows, the setup should guarantee "optimal" image quality. This may include e.g.
- use of high-resolution objectives
- tuning up illumination or exposure times to guarantee optimal SNR
- z-stacks with small stack intervals (to allow for high-quality 3D data and DCV post-processing)
- an optimized autofocus strategy

***Guided Acquisition User Interface***
Some settings are done directly in the GA user interface. These include the following parameters:
- [Acquisition and Analysis setups] The setups done above (Overview Scan, Image Analysis, Detailed Scan) can be chosen from respective drop-down lists.
- [Objective Settings] Objectives for overview and detailed scans are defined not in the experiment, but directly in the GA user interface.
- [Autofocus Settings] Some global autofocus settings can be set by checkboxes.
- [Pre-processing] The user can add some image pre-processing performed before image analysis, to increase the specificity of object detection. Available methods include Apotome Processing, DCV, Airyscan Processing, Shading correction and Extended-Depth-of-Focus.
- [Detailed Scan pre-selection] The number of detailed scans can be defined, as well as the required ordering based on object features (e.g. detailed scan from the 5 largest nuclei).
- [Settings for Rare Event detection] The user can activate repeated acquisition and set the number of cycles and the time intervals
- [Output Folder] The storage folder for images, settings and data tables can be defined. Alternatively, the user may create a "ZEN Connect" project to store the data there. 


