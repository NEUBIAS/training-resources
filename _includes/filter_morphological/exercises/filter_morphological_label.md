- Open [xy_8bit_labels__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nup_nuclei/xy_8bit_labels__nuclei.tif)
- [Plugins > MorpholibJ > Filtering >  Morphological Filters]
   - Operation : Internal Gradient
   - Element : Square
   - Radius : 3
- [ Image › Rename... ]
    - "rim"
- Open [xyc_16bit__nup_nuclei](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nup_nuclei.tif)
- [Image > Duplicate...]
  - Title : Ch1
  - [x] Duplicate hyperstack
  - Channels (c): 1
 
-  [Plugins > MorpholibJ > Analyze >  Intensity Measurements 2D/3D] 
   - Input : Ch1 
   - Labels : rim
  