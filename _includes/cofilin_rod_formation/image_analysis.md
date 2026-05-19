<h4 id="image_analysis"><a href="#image_analysis">Image analysis</a></h4>

The aim of this activity is to measure the formation of rod-like structures in the nuclei of cells in 3D. 

This image analysis workflow consists of several steps, which may be adapted depending on the concrete implementation in a specific software package.

- Nuclei segmentation
  - Thresholding of the 3D nuclei fluorescence image resulting in a binary mask
  - Optionally running a fill holes algorithm on the binary mask
  - Optionally separation of touching nuclei by a watershed
  - Connected component labelling of the binary mask resulting in a label mask
- Rod segmentation
  - Thresholding of the 3D rod fluorescence image resulting in a binary mask
  - Connected component labelling of the binary mask resulting in a label mask
- Assignment of each rod to one nucleus
  - Note that there are also rods outside nuclei should not be assigned to any nucleus
  
