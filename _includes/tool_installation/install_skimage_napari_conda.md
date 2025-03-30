### Installation (only once)

1. install [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) see also [here](https://www.anaconda.com/docs/getting-started/miniconda/install). It is best to install as local user.
	* Windows: the graphical installer works well. You can get it from the [repo](https://repo.anaconda.com/miniconda/) directly
	* OSX: install using the `MacOS terminal installer`. This is the version that allows a local install. Install in the suggested path `~/miniconda3` 
1. open a (new) terminal window
	* Windows: *Anaconda Prompt (Miniconda3)*, e.g. type `Anaconda` in the search bar
	* OSX: Open a `terminal` window. If conda is active you see `(base)` left of the shell prompt. If you do not see `(base)` you may have to manually activate the environment as described [here](https://www.anaconda.com/docs/getting-started/miniconda/install#quickstart-install-instructions) by typing
	```
	 source ~/miniconda3/bin/activate
	```

1. Write 
```
conda create -n skimage-napari-tutorial --override-channels -c conda-forge -c euro-bioimaging -c nodefaults python=3.10 napari=0.4.17 notebook matplotlib jupytext "scikit-image>=0.20" openijtiff "numpy<2"
```
 and press enter to create an environment named `skimage-napari-tutorial` with the necessary packages for the course.
1. create a directory called `skimage-napari-tutorial` (e.g. on your Desktop)

#### Test installation (only once)
1. download [test_installation_skimage_napari.py](https://neubias.github.io/training-resources/functions/test_installation_skimage_napari.py) to
the `skimage-napari-tutorial` directory.
1. open a terminal window (see above)
1. `cd skimage-napari-tutorial`
1. `conda activate skimage-napari-tutorial`
1. `jupyter notebook` (light weight interface) or `jupyter lab`
1. Richt-click on `test_installation_skimage_napari.py` and choose _Open with -> Notebook_.
   You will get a notebook with preconfigured cells. Run the cells one by one (`Run` button or `Shift-Enter`).
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
1. `jupyter notebook` or `jupyter lab`

To run an activity either:
 * (with package `jupytext`) create an empty file, e.g. `current_activity.py` in the `skimage-napari-tutorial` directory.
	Copy the activity code to this file and save the file. From the `jupyter` main landing page right-click on the file and choose _Open with -> Notebook_.
 *  Create a new notebook `New > Python 3` and copy the code in the activity into the notebook.
