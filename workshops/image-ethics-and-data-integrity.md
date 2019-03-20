# Image ethics and data integrity

### Duration

1.5 hours

### Learn more

- http://www.imagedataintegrity.com/about.html
- http://jcb.rupress.org/content/166/1/11.full

## Image data saving

### Concepts

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


### Activity: Explore image saving can change image content

- Open image: `calibrated_16bit__cells_eres_noisy.tif`
- Inspect its content and take notes of some pixel values and coordinates 
- Save the image in whatever format (e.g. tiff, png, gif, jpeg, ...)
- Reopen the image
- Compare the image content to your notes, did it change?

Repeat above activity

- testing different formats for saving
- adjusting the image display before saving

### Formative assessment

How can I ensure that image content is preserved during saving (one answer)?

1. I always use Tiff format, this is safe.
2. I test it by checking pixel values and coordinates before and after saving.
3. I ask my colleagues in the lab, and do what they do.


## Lookup tables

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


### Activity: Quantitative image display

- Open image: `xy_calibrated_16bit__nuclear_protein_control.tif`
    - This image shows a nuclear protein in control cells.   
- Open image: `xy_calibrated_16bit__nuclear_protein_treated.tif`
    - The cells in this 'treated' image have been subjected to a drug.
- Inspect the images! 
    - Did the drug affect the nuclear protein?
- Adjust the lookup-tables (LUTs) of both images to be the same
- Add the LUT calibration to both images 

### Formative Assessment

What helps to scientifically convey image intensity information (multiple answers)?

1. Use a grayscale LUT whenever possible.
2. Color the images in the color of the fluorophore.
3. Add a LUT calibration bar.
4. Use the same LUT for all images.
5. Always adjust the LUT to the image's full bit-depth.
6. Never change the LUT of images! Always keep it as in the raw data.

## 4-D image display

### Concepts


### Activity: ...

- Open image: `xyzt_calibrated_16bit__golgi_bfa.zip`
- Discuss different options how to present this data

### Formative Assessment


## High dynamic range image display

### Concepts

### Activity: Quantitative image display

- Open image: `xyt_calibrated_16bit__golgi_bfa_sum_projection.tif`

### Formative Assessment


## Image background subtraction

### Concepts


<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    image_math -> pixel_values [label="  changes"];
    image_math -> scientific_image_content [label="  can distort"];
  }
'/>

### Activity: ...


### Formative Assessment


