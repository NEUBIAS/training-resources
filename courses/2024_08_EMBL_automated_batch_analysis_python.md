# Automated batch analysis using python  

## Why take this course

Typically, one starts a bioimage analysis project by, more or less, interactively analysing one or a couple of images. However, to draw sound scientific conclusions one almost always needs to analyse many images. Doing this (semi-)interactively has some major drawbacks: It can take a lot of time and it is not readily reproducible, not by yourself and even less so by collaborators or readers of your publication. Thus, fully automated, and thereby reproducible, batch analysis is typically what is needed. In this course you will learn the basics of setting up and running fully automated analysis of many images.

## Prerequisites

* You should know how to conduct basic image analysis in python (see, e.g., the content of [this course](https://github.com/NEUBIAS/training-resources/blob/master/courses/YYYY_MM_HOST_skimage_napari_beginners.md)).

### IT Setup

Please, before the course use the `conda` platform to install skimage and napari on your laptop, following [these instructions](https://neubias.github.io/training-resources/tool_installation/index.html#skimage_napari). 

## Schedule 

The whole course will be guided hands-on sessions.

- **2024 August Tuesday 06, 9:30 - 12:00** 

## Venue

- Germany, Heidelberg, Meyerhofstr. 1, EMBL, Room: IC Lecture hall
- Zoom link: TBD

## Trainers and organisers

- Christian Tischer (EMBL)
- ...

## Teaching tips

Dear Trainers, please consider checking these [teaching tips](https://github.com/NEUBIAS/training-resources/blob/master/TEACHING_TIPS.md).

## Teaching content

### Introduction

- Trainers introduce themselves, where they work and how they are competent
- Participants introduce themselves, where they work, why they joined the course, and what previous experience they have
    - Depending on the number of participants, one could distribute the introductions across the course, e.g. do some in the morning and some in the afternoon

### Basics of automated image batch analysis in python

1. [Loops](https://neubias.github.io/training-resources/script_for_loop/index.html)
    - Trainer: Felix Schneider
    - TODO: Flex: check and improve
1. [String and path manipulations](https://neubias.github.io/training-resources/string_concat/index.html)
    - TODO: Tischi change to multi-activities
    - Trainer: Dominik Kutra
1. [Functions](https://neubias.github.io/training-resources/script_functions/index.html)
    - TODO: Arif check this 
    - Trainer: Arif Khan
1. Discuss good practices for input and output file and folder names
    - Trainer: Christian Tischer
    - Show how the input and output of the "Batch analysis" module
    - Show this? https://git.embl.de/grp-cba/astrocyte-differentiations/-/blob/main/data_management.md
    - Recommend saving the analysis script into the same folder structure, with a date?!
1. [Batch analysis](https://neubias.github.io/training-resources/batch_processing/index.html)
    - Trainer: Julian Hennies or Felix Schneider
    - TODO: Dominik: how hard would it be to save a MoBIE table
1. Demo batch inspection with MoBIE
    - Trainer: Christian Tischer

## Follow-up courses

- Batch QC of image analysis results 
    - Using MoBIE to open the images, label masks, and tables
- Batch running using Nextflow
