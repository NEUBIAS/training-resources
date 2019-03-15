# Image ethics and data integrity

### Duration

1.5 hours

### Learn more

- http://www.imagedataintegrity.com/about.html
- http://jcb.rupress.org/content/166/1/11.full

## Image data integrity

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    image_integrity -> image_content [label="  preserving"];
    image_content -> pixel_values;
    image_content -> pixel_coordinates;
  }
'/>

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    saving_images -> image_content [label="  can change"];
  }
'/>


### Activities

#### Explore how saving images can change image content

- Open an image
- Inspect it contents, take notes of some pixel values and coordinates 
- Save the image
- Reopen the image
- Compare the image content to your notes, did it change?

##### Example data:

- calibrated_16bit__cells_eres_noisy.tif

### Formative Assessments

How can I ensure that image content is preserved during saving?

1. I always use Tiff format, this is safe.
2. I always test it by checking pixel values and coordinates before and after saving.
3. 

## Image data presentation

### Concepts

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    lookup_table_settings -> image_appearance [label="  change"];
    image_appearance -> scientific_message [label="  changes"];
  }
'/>

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    responsible_scientist -> lookup_table_settings [label="  configures thoughtfully"];
  }
'/>

### Activities


### Formative Assessments

