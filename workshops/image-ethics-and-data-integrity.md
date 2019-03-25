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


### Activity: Save an image

![image](/uploads/284ad5edadf96234037f895a86338a58/image.png)

- Open image: `calibrated_16bit__cells_eres_noisy.tif`
- Note down the value and coordinate of the pixel at [218, 332]
- Save the image in **jpg** format
- Reopen the image
- Compare the pixel to your notes, did it change?

Repeat above workflow, but now adjust the image display before saving.

Repeat above workflow, but now save it in a different format (e.g. tif, png).


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
    - The cells in this image have been subjected to a drug.
- Inspect the images:
    - Did the drug affect the amount of the nuclear protein?
- Adjust the lookup-tables (LUTs) of both images to be the same
- Add the LUT calibration to both images 

### Formative Assessment

What helps to scientifically convey image intensity information (multiple answers)?

1. Use grayscale LUT whenever possible.
3. Add a LUT calibration bar.
4. Use the same LUT for all images.
5. Adjust the LUT to the image's full bit-depth.
6. Never change the LUT of images! Always keep it as is.

## 3-D image display

### Concepts

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    3-D data -> visualisation [label="  multiple options"];
    visualisation -> scientific_message [label="  affects"];
  }
'/>

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    3-D visualisation -> sum projection;
    3-D visualisation -> max projection;
    3-D visualisation -> slice animation;
  }
'/>


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


