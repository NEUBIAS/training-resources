<h4 id='modify'><a href="#modify">Volume rendering</a></h4>

- Open a volume viewer with one of the below example images.
- Explore different volume rendering modes, such as
  - Maximum projection
    - Explore different camera positions
  - Volume rendering
    - Explore various transparency (alpha) mappings.
      - Interesting for [3-D FIB-SEM](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__fib_sem_crop.tif)
  - Iso-surface rendering
    - Explore various surface thresholds
    - Explore changing the light position
- Save a snapshot.
- Create and save a custom animation, e.g. rotating the image.

<h6>Example data</h6>

- [3-D+t Chromosome congression](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzt_8bit__starfish_chromosomes.tif)
  - Useful to see in 3-D rendering (as it is very hard to see what is going on in 2-D slices)
- [3-D EM and segmentation](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit__em_synapses_and_labels.tif)
  - EM data is difficult to render in 3-D but for the segmentation channel it is very useful
  - Note that the segmentation channel does not look good in a max-projection; actual volume rendering is much better.
- [3-D MRI head](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__mri_full_head.tif)
  - Good to compare various rendering modes
- [3-D Organoid nuclei](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__organoid_nuclei.tif)
  - Challenge: Outer nuclei occulde inner nuclei
- [3-D FIB-SEM](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__fib_sem_crop.tif)
  - Challenge: Dense signal, background is bright
- [3-D Tissue segmentation label mask](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated_labels__platy_tissues.tif)
  - Challenge: Epithelial tissue occludes inside
