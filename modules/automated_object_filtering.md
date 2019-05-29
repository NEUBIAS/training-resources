# Image analysis automation

## Automated object filtering

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    label_image -> table [label="  measure_shape"];
    table -> filtered_objects;
    filtered_objects -> label_image [label="  remove"];
}
'/>

### Activity: Automatically remove objects from label image

- Open image: `xy_8bit_labels__four_objects.tif`
- Devise code to automatically remove objects from the label image, e.g.
	- Remove all cells larger than N pixels in area

### Formative assessment


