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
figure_legend: Screenshot of the community partners of https://forum.image.sc, containing many very useful bioimage analysis tools.

multiactivities:
  - ["tool_installation/imagej.md", [["Fiji", "tool_installation/install_fiji.md"], ["IntelliJ", "tool_installation/install_intellij.md"] ]]
  - ["tool_installation/skimage_napari.md", [["conda", "tool_installation/install_skimage_napari_conda.md"], ["BAND", "tool_installation/install_skimage_napari_BAND.md"] ]]
  - ["tool_installation/napari_standalone.md", [["desktop download", "tool_installation/install_napari_standalone.md"]]]
  - ["tool_installation/galaxy.md", [["Start a local Galaxy", "tool_installation/install_galaxy_local.md"],["Using Galaxy EU", "tool_installation/install_galaxy_eu.md"]]]

assessment:

learn_next:

external_links:

---

## Running bioimage analysis software

### Hardware

Bioimage analysis software can be run either locally on your own computer or remotely on a cloud-based system. Each approach has its advantages and limitations:

### Local (Your Computer)

- **Pros**:
  - No internet connection required.
  - Smooth interaction with screen, mouse, and keyboard.
- **Cons**:
  - Limited hardware resources.
  - Potential challenges with software installation.

### Remote (Cloud-Based)

- **Pros**:
  - Access to powerful, dedicated hardware.
  - Preinstalled and ready-to-use software.
- **Cons**:
  - Requires network access.
  - Limited ability to modify or install additional software.
  - Screen rendering may be slower due to network latency.
 
### Sofware

#### Package managers

Package managers are software that can install libraries (packages) on your computer that are needed to develop and run bioimage analysis appllications. Prominent examples are [`maven`](https://maven.apache.org) for managing Java and `conda` for managing Python and other libraries; [`pip`](https://pypi.org/project/pip/) is a relatively old and well-known package manager, specific to Python; we have heard good things about [`uv`](https://github.com/astral-sh/uv) as a modern Python package manager. Generally, the landscape of Python package managers is evolving and hard to keep track of.

##### Conda

- Conda is a software that you need to install on your computer
- Conda is a so-called package manager that will download software packages onto your computer
- Initially, conda was mainly for downloading python packages, thus the "snake" name, but now `conda` evolved to be a general purpose package manager
- Now, there are  many variants of conda ([mamba](https://mamba.readthedocs.io/en/latest/index.html), [micromamba](https://mamba.readthedocs.io/en/latest/index.html), [miniforge](https://github.com/conda-forge/miniforge), ...); those will all install the same software packages on your computer, but will do this more or less fast and well

###### Example use with explanations

`conda create -n skimage-napari-tutorial --override-channels -c conda-forge -c euro-bioimaging -c nodefaults python=3.10 napari=0.4.17 notebook matplotlib jupytext "scikit-image>=0.20" openijtiff "numpy<2"`

- `conda create -n skimage-napari-tutorial`: Asks `conda` to `create` a new "environment" on your computer with the name (`-n`) `skimage-napari-tutorial`
  - This simply creates a folder on your computer called `skimage-napari-tutorial` into which conda will download stuff
- `--override-channels -c conda-forge -c euro-bioimaging -c nodefaults`: Tells conda from where to download the software, a "channel" `-c` is one place that hosts conda packages
  - ` -c nodefaults`: The reason to adding this was that the licensing of the default distribution channel for conda packages changed such that even academic institutions are not allowed anymore to use them
- `python=3.10 napari=0.4.17`: We require specific versions of those packages, the versions of other packages that don't have the `=` will be chosen automatically by conda such that, hopefully, everything is compatible 
- "scikit-image>=0.20" & "numpy<2": Limits the range of versions to be above or below a certain version
  - `scikit-image>=0.20` this was done here to make sure that the installation contains a nice new feature of `scikit-image` that was only available from version `0.20` on and, back then, the version that conda would download by default was lower than this
  - `numpy<2`: Typically, if the so-called major version changes, e.g. `1.9` goes to `2.0`, there are "breaking changes"; this was also the case for `numpy` and, back then, many other packages that use `numpy` were not yet ready to use the new `2.0` version leading to errors.

General notes:

- The specific software that is downloaded by an identical conda command will differ depending on your operating system and on your hardware (e.g. newer Mac computers have a different chip for which conda will need to download other packages than for older Mac)
  - As a consequence, unfortunately, the same conda command may produce a working environment on some computers while it may not work on others