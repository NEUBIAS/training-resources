
# Introduction

<p>
    <img width="3319" height="1810" alt="Guided_Acquisition_UI_two_columns" src="https://github.com/user-attachments/assets/3f9c151c-6833-4b0c-a41c-7e594ea6e7f2" />
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

Within the workflow, the overview scan serves first and foremost the detection of ROIs for targeted acquisition. Hence, image quality must be sufficient to reliably detect the desired phenotype, but imaging settings should otherwise be chosen to keep scan time and data sizes as slim as possible. There is several ways of reducing acquisition effort in this step:
- only acquire channels that are strictly required for ROI identification
- employ a low-magnification objective or binning
- only acquire a number of tiles that guarantees detecting your desired number of ROIs / phenotypes, not more
- avoid large stacks


