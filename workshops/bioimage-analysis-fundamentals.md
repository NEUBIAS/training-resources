# Bioimage analysis fundamentals

## Image content

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    image -> pixel [label="  has many"];
    pixel -> value;
    pixel -> indices;
    pixel -> coordinates;
    indices -> calibration;
    calibration -> coordinates;
    image -> calibration;
    image -> data_type;
    data_type -> value [label=" restricts"];
    pixel -> voxel [label="  3D"];   
  }
'/>

### Activity

- Open image: *_8bit_* 
	- Explore pixel values and pixels indices
	- Add image calibration
	- Explore pixel coordinates
		- Check whether the sofware changed indices to coordinates
- Open image: *_float_*
	- Explore pixel values

### Formative assessment

Which statements about images are true (multiple answers)? 

- Pixel coordinates are always integer values.
- Changing the image calibration changes the pixel values.
- Pixel coordinates depend on image calibration.
- Pixel indices are always positive integer values.
- Image data type affects the possible range of pixel coordinates.
- A pixel can take any value.
- The lowest pixel index of a 2D image always is `[1,1]`.

## Image display

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    lookup_table__LUT -> color;
    lookup_table__LUT -> brightness;
    lookup_table__LUT -> LUT_min;
    lookup_table__LUT -> LUT_max;
    pixel_value -> brightness;
    LUT_min -> brightness;
    LUT_max -> brightness;
  }
'/>

```
brightness( pixel_value ) = ( pixel_value - LUT_min ) / ( LUT_max - LUT_min )
0 <= brightness <= 1 
contrast = LUT_max - LUT_min 
``` 

### Activity

- Open image:
- Change LUT settings
	- Appreciate that LUT settings do not affect image content.


###



