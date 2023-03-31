## Install skimage napari

### Installation (only once)

1. [install mamba](https://github.com/conda-forge/miniforge#mambaforge)
1. open a terminal window
1. `mamba create -n skimage-napari-tutorial -c conda-forge python=3.10 napari=0.4.17 notebook matplotlib`
1. create a directory called `skimage-napari-tutorial` (e.g. on your Desktop)
1. download [open_tiff.py](https://neubias.github.io/training-resources/functions/open_tiff.py)
1. move `open_tiff.py` in the `skimage-napari-tutorial` directory

#### Test installation (only once)

1. `conda activate skimage-napari-tutorial`
1. `jupyter notebook`
1. type `napari` in a notebook cell and execute it: the napari GUI should show up

#### Start (every time)

1. open a terminal
1. `cd skimage-napari-tutorial`
1. `mamba activate skimage-napari-tutorial`
1. `jupyter notebook`
  - `New > Python 3`
