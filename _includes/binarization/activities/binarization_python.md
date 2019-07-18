``` python
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

# load the image from file
image_file = "/image-analysis-training-resources/image_data/xy_8bit__two_cells.tif"
image = io.imread(image_file)

# binarize the image, so that all values larger than the threshold are foreground
threshold_value = 60
binarized = image > threshold_value

# display the original and the binarized image
fig, ax = plt.subplots(2)
ax[0].imshow(image)
ax[0].set_title("Image")
ax[1].imshow(binarized)
ax[1].set_title("Binarized")

```

For associated course material in jupyter, [click here](https://nbviewer.jupyter.org/github/embl-bio-it/image-analysis-with-python/blob/carpentry/image-analysis-session/image-binarization.ipynb#Image-Binarization).
You can also spin up an interactive [binder session](https://gke.mybinder.org/v2/gh/embl-bio-it/image-analysis-with-python/carpentry?filepath=image-analysis-session/image-binarization.ipynb).
