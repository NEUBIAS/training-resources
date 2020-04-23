---
title:     Pixel data types
layout:    module
---

## Pixel data types

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    "data type" -> "pixel values" [label="  restricts"];
    "N-bit unsigned integer" -> "0, 1, ..., 2^N-1";
    "data type" -> float -> "..., -1031.0, ..., 10.5, ...";
    "data type" -> "...";
    "data type" -> "N-bit unsigned integer";
  }
'/>

## Pixel data type conversions

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    "data type conversion" -> "values" [label="  can change"];
    "data type conversion" -> "value range" [label="  changes"];
  }
'/>

### Activity: 16-bit to 8-bit conversion

* Open image: xy_16bit__two_values.tif
* Convert to 8-bit
* Understand the mathematics underlying the conversion from 16-bit to 8-bit.

### Activity: 16-bit to float conversion

* Open image: xy_16bit__two_values.tif
* Convert to float

### Formative Assessment

True or false? Discuss with your neighbor!

1. Changing pixel data type never changes pixel values.
2. Converting from 16-bit unsigned integer to float never changes the pixel values.
3. Changing from float to 16-bit unsigned integer never changes the pixel values.
4. There is only one correct way to convert from 16-bit to 8-bit.
