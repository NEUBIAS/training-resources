---
title:     Image binarization
layout:    page
permalink: /binarization
---

# Image binarization 

## Requirements

To understand this episode you need to know:

- A
- B
- C

## Motivation

Few sentences.

## Learning objectives

- Understand the relationship between an intensity image and a derived binary image.
- Execute binarization on an image.

## Concept map

<img src='https://g.gravizo.com/svg?
 digraph G {
shift [fontcolor=white,color=white];
	"pixel values" -> "foreground\n1,255" [label = " >= threshold"];
	"pixel values" -> "background\n0" [label = " < threshold"];
	"foreground\n1,255" -> "binarised pixel values"
	"background\n0" -> "binarised pixel values"
  }
'/>

## Example

![binarization_figure_00](../figures/binarization_concept_example.png)

## Activity

Open an image and binarize it by applying a threshold.

<details>
 <summary>ImageJ user interface</summary>
	- `Open...`
		- "/image-analysis-training-resources/image_data/xy_8bit__two_cells.tif";
  	- `Threshold...` 
</details>

<details>
 <summary>ImageJ macro</summary>
  open("/image-analysis-training-resources/image_data/xy_8bit__two_cells.tif");
  setThreshold(30, 255);
  setOption("BlackBackground", true);
  run("Convert to Mask");
</details>




## Formative assessment

Quizz or something

## Follow-up material

- [http:// ](next module in this repo)

## Learn more

External links...

