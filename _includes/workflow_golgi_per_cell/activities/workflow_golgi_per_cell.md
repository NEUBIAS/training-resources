## Workflow Golgi per cell
- Open the image [xyc_16bit__nuclei_golgi.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nuclei_golgi.tif).
- Segment nuclei and Golgi
- Dilate nuclei to approximate cells
- Assign the Golgi fragments to their parent cell
- Measure the intensity of the child (Golgi) objects in the parent (cell) label mask
- You could, e.g., measure the `min`, `max` and `mode` intensity
    - `min = max`: the child object is within one parent object
    - `min != max`: the child object overlaps with multiple parent objects
    - `mode`: the label of the parent object that the child object overlaps most with
    - `min = 0`: the child object is (partially) located outside of any parent cell
    