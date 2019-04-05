# Image feature enhancement

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    image -> filter -> "enhanced image";
    "enhanced image" -> "feature" [label="  aka"];
    filter -> "feature enhancement" [label=" aka"];   
}
'/>



## Difference of Gaussian (DoG) for spot enhancement

<img src='https://g.gravizo.com/svg?
 digraph G {
	shift [fontcolor=white,color=white];
	image -> "small blur";
	image -> "large blur";
	"small blur" -> "remove noise";
	"large blur" -> "estimate local background";
	"small blur" -> "DoG = small blur - large blur";
	"large blur" -> "DoG = small blur - large blur";
}
'/>

### Activity: Enhance spots in noisy image with uneven background

- Open image: xy_8bit__two_spots_noisy_uneven_background.tif
- Appreciate that you cannot simply threshold them
- Copy the image and blur with a Gaussian of small radius -> gs
- Copy the image and blur with a Gaussian of bigger radius -> gb
- Create `DoG = gs - gb`
- Appreciate that you can simply threshold the DoG image
 
### Formative Assessment

TODO

### Learn more

- https://en.wikipedia.org/wiki/Difference_of_Gaussians

