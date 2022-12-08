### Install skimage napari

Essentially, follow these instructions: https://alisterburt.github.io/napari-workshops/SciPy-0722/scipy_installation.html

#### Installation (only once)

1. install miniconda (TODO)
1. `conda create -n skimage-napari-tutorial python=3.9`
1. `conda activate skimage-napari-tutorial`
1. `conda install -c conda-forge notebook matplotlib`
1. `pip install aicsimageio`
1. `conda install bioformats_jar`
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
1. download the file `load_from_url.py`
1. move `load_from_url.py` in `skimage-napari-tutorial` folder
1. `conda activate skimage-napari-tutorial`
1. `jupyter notebook`
  - Click on folder: `skimage-napari-tutorial`
  - `New > Python 3`
