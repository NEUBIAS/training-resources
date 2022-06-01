- Open the image [xy_8bit_binary__nuclei_noisy.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nup_nuclei/xy_8bit_binary__nuclei_noisy.tif)
- [Plugins > MorpholibJ > Filtering >  Morphological Filters]
   - operation : Opening 
   - element : Square 
   - radius : 1
- [Plugins > MorpholibJ > Filtering >  Morphological Filters]
  - operation : Closing 
  - element : Square 
  - radius : 16
- An alternative to the closing operation is also [Plugins > MorpholibJ > Filtering >  Fill Holes (Binary/Gray)]



