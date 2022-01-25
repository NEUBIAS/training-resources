---
title:  Semantic image segmentation using machine learning (DRAFT)
layout: module
---

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    "intensity image" -> threshold;
    threshold -> "binary image";
    "binary image" -> "background value";
    "binary image" -> "foreground value";
    "intensity image" -> "machine learning";
    "annotations" -> "machine learning";
    "machine learning" -> "pixel class image";
    "pixel class image" -> "class00 value";
    "pixel class image" -> "class01 value";
    "pixel class image" -> "class.. value";
    "pixel class image" -> "class C value";
 }
'/>


&nbsp;

&nbsp;

&nbsp;

## Decision tree based image segmentation

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    "Intensity image" -> "filter00 image" -> "Decision tree(s)";
    "Intensity image" -> "filter01 image" -> "Decision tree(s)";
    "Intensity image" -> "filter02 image" -> "Decision tree(s)";
    "Intensity image" -> "filter.. image" -> "Decision tree(s)";
    "Intensity image" -> "filter F image" -> "Decision tree(s)";
    "Annotations" -> "Decision trees(s)"
    "Decision tree(s)" -> "class00 (probability) image";
    "Decision tree(s)" -> "class01 (probability) image";
    "Decision tree(s)" -> "class.. (probability) image";
    "Decision tree(s)" -> "class C (probability) image";
 }
'/>

## Activity: Semantic image segmentation

- Open image: xy_8bit__em_fly_eye.tif
- Segment three classes: background, eye, other
	- Choose image filters
	- Draw few labels in the blurry image background => class00
	- Draw few labels on the eye => class01
	- Draw few labels on other parts of the animal => class02
	- While( not happy):
		- Train the classifier
 		- Inspect the predictions
		- Add more labels where the predictions are wrong

TODO: use multiple files to demo that a classifier can be applied on other images.

## Formative assessment

True or false? Discuss with your neighbour!

- In contrast to simple thresholding, using machine learning for pixel classification, one always has more than 2 classes.
- If one wants to learn 4 different classes one has to, at least, add 4 annotations on the training image.
- One cannot classify an image where one did not put any training annotations.
