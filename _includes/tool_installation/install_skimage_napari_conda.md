### Installation

#### Install a conda package manager

If you already have a conda package manager you can skip this step.

Due to updates in the licensing conditions affecting Anaconda and Miniconda installations, we recommend the usage of miniforge instead. For installation follow the respective instructions for your operating system on the [miniforge github page](https://github.com/conda-forge/miniforge).

OSX and linux: Note that for the following installation instructions the base environment needs to be activated. This is the case if you see `(base)` left of the shell prompt. If you do not see this you may use 

```
source ~/miniforge3/bin/activate
```

to activate it.

#### Install the course environment 

Within a terminal window execute
  
```
conda create -n skimage-napari-tutorial --override-channels -c conda-forge -c euro-bioimaging -c nodefaults python=3.12 napari=0.6.0 pyqt notebook matplotlib jupytext scikit-image openijtiff -y
```

This will create an environment named `skimage-napari-tutorial` with the necessary packages for the course.

### Use the course environment

#### Activate the environment and open a notebook 

1. Create a directory called `skimage-napari-tutorial` (e.g. on your Desktop)
1. Open a terminal window (see above)
1. Go into the above directory `cd skimage-napari-tutorial`
1. `conda activate skimage-napari-tutorial`
1. `jupyter notebook` or `jupyter lab`

#### Test the environment

Activate the environment and open a notebook (see above).

1. Download [test_installation_skimage_napari.py](https://neubias.github.io/training-resources/functions/test_installation_skimage_napari.py) to
the `skimage-napari-tutorial` directory.
1. Richt-click on `test_installation_skimage_napari.py` and choose _Open with -> Notebook_. You will get a notebook with preconfigured cells. Run the cells one by one (`Run` button or `Shift-Enter`). The napari GUI will show twice the same image.
1. Create a new notebook
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

### Run code in the environment

Activate the environment (see above).

To run code either:
 * (with package `jupytext`) create an empty file, e.g. `my_code.py` in the `skimage-napari-tutorial` directory.
	Copy the activity code to this file and save the file. From the `jupyter` main landing page right-click on the file and choose _Open with -> Notebook_.
 *  Create a new notebook `New > Python 3` and copy the code in the activity into the notebook.

### Troubleshooting

#### Ubuntu: Napari fails to show 3D viewer

We've encountered an OpenGL error for the napari 3D viewer on a Ubuntu machine when using the conda environment installed as described above. 

This installation procedure got it to work (Note: not yet tested for all modules):

```
conda create -n skimage-napari-tutorial --override-channels -c conda-forge python=3.9
conda activate skimage-napari-tutorial
pip install napari[all]
pip install notebook
pip install jupytext
conda install --override-channels -c conda-forge -c euro-bioimaging -c nodefaults openijtiff
```
