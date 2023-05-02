### Installation (only once)

1. install [miniconda](https://docs.conda.io/en/latest/miniconda.html)
1. open a terminal window
	* Windows: *Anaconda Prompt (Miniconda3)*, e.g. type `Anaconda` in the search bar
1. write `conda create -n skimage-napari-tutorial -c conda-forge python=3.10 napari=0.4.17 notebook matplotlib jupytext` and press enter
1. create a directory called `skimage-napari-tutorial` (e.g. on your Desktop)
1. download [OpenIJTIFF.py](https://neubias.github.io/training-resources/functions/OpenIJTIFF.py) to the `skimage-napari-tutorial` directory

#### Test installation (only once) 
1. download [test_installation_skimage_napari.py](https://neubias.github.io/training-resources/functions/test_installation_skimage_napari.py) to 
the `skimage-napari-tutorial` directory.
1. open a terminal window (see above)
1. `cd skimage-napari-tutorial`
1. `conda activate skimage-napari-tutorial`
1. `jupyter notebook`
1. Click on `test_installation_skimage_napari.py`. You will get a notebook with preconfigured cells. Run the cells one by one (`Run` button or `Shift-Enter`). 
The napari GUI will show twice the same image.
1. create a new notebook
	- `New  > Python 3`
    - type following commands in a cell and execute the cell by pressing the `Run` button or `Shift-Enter`.

``` python
# %% [markdown]
# # Test python napari skimage install

# %%
# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# %%
# Read the intensity image
from skimage.io import imread
fpath = 'https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif'
image = imread(fpath)

# %%
# View the intensity image
viewer.add_image(image)

# %% 
# Read via OpenIJTIFF (OpenIJTiff.py must be in the same folder as the notebook path)
from OpenIJTIFF import open_ij_tiff
image_opentiff, axes, scales, units = open_ij_tiff(fpath)
# View the intensity image
viewer.add_image(image_opentiff)
```


#### Start (every time)
1. open a terminal window (see above)
1. `cd skimage-napari-tutorial`
1. `conda activate skimage-napari-tutorial`
1. `jupyter notebook`

To run an activity either: 
 * (with package `jupytext`) create an empty file, e.g. `current_activity.py` in the `skimage-napari-tutorial` directory. 
	Copy the activity code to this file and save the file. From the `jupyter` main landing page click on the file.
 *  Create a new notebook `New > Python 3` and copy the code in the activity into the notebook.
