## Install skimage napari

### Installation (only once)

1. [install mamba](https://github.com/conda-forge/miniforge#mambaforge)
1. open a terminal window
1. `mamba create -n skimage-napari-tutorial -c conda-forge python=3.10 napari=0.4.17 notebook`


1. `conda install -c conda-forge notebook matplotlib`
1. `pip install aicsimageio`
1. `conda install -c conda-forge openjdk=11.0.8`
1. `conda install -c conda-forge bioformats_jar`
1. `pip install "napari[all]"`
1. `pip install napari-brightness-contrast`
1. `pip install napari-plot-profile`
1. create a directory called `skimage-napari-tutorial` (e.g. on your Desktop)
1. download [load_from_url.py](https://neubias.github.io/training-resources/functions/load_from_url.py) 
1. move `load_from_url.py` in `skimage-napari-tutorial` directory

#### Test installation (only once)

1. `conda activate skimage-napari-tutorial`
1. `jupyter notebook`
1. `napari`

#### Start (every time)

1. open a terminal
1. `cd skimage-napari-tutorial`
1. `mamba activate skimage-napari-tutorial`
1. `jupyter notebook`
  - `New > Python 3`
