Essentially, follow these instructions: https://alisterburt.github.io/napari-workshops/SciPy-0722/scipy_installation.html

#### Installation (only once)

1. install miniconda (TODO)
1. `conda create -y -n skimage-napari-tutorial -c conda-forge python=3.9`
1. `conda activate skimage-napari-tutorial`
1. `pip install "napari[all]"`
1. `pip install notebook matplotlib`
1. `pip install aicsimageio`
1. `conda install -c conda-forge bioformats_jar`
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
1. go to `skimage-napari-tutorial`
1. `conda activate skimage-napari-tutorial`
1. `jupyter notebook`
  - `New > Python 3`
