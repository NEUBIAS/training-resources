# Rank filters

## Basic rank filters

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
	"rank filters" -> awesome [label="  are"];
	"rank filters" -> minimum -> erosion [label="  aka"];
	"rank filters" -> maximum -> dilation [label="  aka"];
	"rank filters" -> median;
	"rank filters" -> "size" [label="  have"];
  }
'/>

### Activity: Explore rank filters on binary images

- Open image: xy_8bit_binary__two_spots_different_size.tif
- Explore how the structures grow and shrink when using erosion and dilation

### Activity: Explore rank filters on grayscale images

- Open image: xy_8bit__two_noisy_squares_different_size.tif
- Explore how a median filter
	- removes noise
	- removes small structures
	- preserves egdes
- Compare median filter to mean filter of same radius


### Formative assessment

True or false? Discuss with your neighbour!

1. Median filter is just another name for mean filter.
2. Small structures can completely disappear from an image when applying a median filter.

Fill in the blanks, using those words: shrinks, increases, decreases, enlarges.

1. An erosion _____ objects in a binary image. 
2. An erosion in a binary image _____ the number of foreground pixels.
3. A dilation in a grayscale image _____ the average intensity in the image.
4. A dilation _____ objects in a binary image.


## Morphological opening and closing

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
        "opening" -> "rank filter sequence" [label="  is"];
        "closing" -> "rank filter sequence" [label="  is"];
	"opening" -> "removes small structures";
	"closing -> "fills small gaps";
  }
'/>

```
opening( image ) = dilation( erosion( image ) )
```

```
closing( image ) = erosion( dilation ( image ) )
```


### Activity: Explore opening and closing on binary images

- Open image: xy_8bit_binary__for_open_and_close.tif
- Explore the effect of morphological closing and opening
	- Closing can fill the hole
	- Closing can connect the circle
	- Opening can remove thin structures 


### Formative assessment

TODO


## Top hat filter for local background subtraction

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
	"top hat filter" -> "rank filter sequence" [label="  is"];
	"top hat filter" -> "local background subtraction";
  }
'/>


```
topHat( image ) = image - dilation( erosion( image, r), r )
```

TODO: Add image from pdf


### Activity: Explore tophat filter

- Open image: xy_8bit__spots_local_background.tif
- Use topHat filter to remove local background

## Activity: Implement a tophat filter

- Devise code to implement a tophat filter using basic functions

## Activity: Explore tophat filter on biological data

- Open image: xy_16bit__autophagosomes.tif 
- Use topHat filter to remove local background

## Activity: Explore tophat fiter on noisy data

- Open image: xy_8bit__spots_local_background_with_noise.tif 
- Use topHat filter to remove local background
- Appreciate that noise poses a challenge to the tophat filter


### Formative assessment

TODO


## Median filter for local background subtraction

<img src='https§://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
	"median" -> "local background";
	"median" -> "radius" -> "about 3 times larger than foreground objects";
  }
'/>


```
median_based_background_correction = image - median( image, r)
```

TODO: Add image from pdf


### Activity: Implement median based background subtraction

- Write code to implement a median based background subtraction


### Activity: Explore median filter for local background subtraction

- Open images: 
	- xy_8bit__spots_local_background.tif 
	- xy_8bit__spots_local_background_with_noise.tif
	- 
- Use topHat filter to remove local background
- Devise code to implement a tophat filter using basic functions

### Formative assessment

TODO







