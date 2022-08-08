---
title:     Tool installation
layout:    module

prerequisites:

objectives:
  - "Install the software that is required to execute the activities in this training material"

motivation: |
  Provide instructions for installing the software required for this workshop. Please follow the instructions given by your trainer regarding which software you will need!

concept_map: >
  graph TD
    I("Image Analysis") -->|with| C("Computer")
    C -->|using| T("Tools")
    T -->|require| S("Installation")

figure: /figures/tool_installation.png
figure_legend:

activity_preface:

activities:

exercises:

assessment:

learn_next:

external_links:

---

## Activities

- ImageJ GUI
  - Install Fiji
- ImageJ Macro
  - Install Fiji
- ImageJ Jython
  - Install Fiji
- skimage napari
  - ???
- MATLAB
  - Install MATLAB or GNU Octave

## Installation instructions

### Install Fiji

1. Install Fiji on your machine, as described [here](https://imagej.net/software/fiji/downloads).
1. Add the following updates sites, as described [here](https://imagej.net/update-sites/following).
  - IJPB-Plugins

### Install skimage napari

Essentially, follow these instructions: https://alisterburt.github.io/napari-workshops/SciPy-0722/scipy_installation.html

#### Installation (only once)

1. install miniconda (TODO)
1. `conda create -n skimage-napari-tutorial python=3.9`
1. `conda activate skimage-napari-tutorial`
1. `conda install -c conda-forge notebook`
1. `pip install "napari[all]"`
1. `pip install napari-brightness-contrast`
1. `pip install napari-plot-profile`

#### Test installation (only once)

1. `conda activate skimage-napari-tutorial`
1. `jupyter notebook`
1. `napari`

#### Start (every time)

1. `cd somewhere` (TODO)
1. `mkdir skimage-napari-tutorial`
1. `conda activate skimage-napari-tutorial`
1. `jupyter notebook`
  - Click on folder: `skimage-napari-tutorial`
  - `New > Python 3`

### Install MATLAB or GNU Octave

- MATLAB is a [licensed software](https://www.mathworks.com/products/get-matlab.html) by MathWorks. Please contact your Institution to verify if you have access to a license. If this is the case, you can find detailed instructions on how to install the software [here](https://www.mathworks.com/help/install/).
- Alternatively, [GNU Octave](http://www.gnu.org/software/octave/) is a free and open-source alternative to MATLAB which shares its syntax (more about compatibility at this [link](https://en.wikipedia.org/wiki/GNU_Octave#MATLAB_compatibility)). Installation instructions can be found [here](http://www.gnu.org/software/octave/download).
