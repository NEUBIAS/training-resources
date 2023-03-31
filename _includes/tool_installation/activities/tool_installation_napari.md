## Install skimage napari

### Installation (only once)

1. install [miniconda](https://docs.conda.io/en/latest/miniconda.html)
1. open a terminal window
	* Windows: *Anaconda Prompt (Miniconda3)*, e.g. type `Anaconda` in the search bar
1. `conda create -n skimage-napari-tutorial -c conda-forge python=3.10 napari=0.4.17 notebook matplotlib`
1. create a directory called `skimage-napari-tutorial` (e.g. on your Desktop)
1. download [open_tiff.py](https://neubias.github.io/training-resources/functions/open_tiff.py)
1. move `open_tiff.py` in the `skimage-napari-tutorial` directory

#### Test installation (only once)
1. open a terminal
1. `cd skimage-napari-tutorial`
1. `conda activate skimage-napari-tutorial`
1. `jupyter notebook`
  - `New > Python 3`
1. type following commands in a cell and run. You should get the napari GUI showing an image

``` python
# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# Read the intensity image
from skimage.io import imread
image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif')

# View the intensity image
viewer.add_image(image)
```


#### Start (every time)

1. open a terminal
1. `cd skimage-napari-tutorial`
1. `conda activate skimage-napari-tutorial`
1. `jupyter notebook`
  - `New > Python 3`
