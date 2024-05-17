# Automated batch analysis using python  

## Why take this course

Typically, one starts a bioimage analysis project by, more or less, interactively analysing one or a couple of images. However, to draw sound scientific conclusions one almost always needs to analyse many images. Doing this (semi-)interactively has some major drawbacks: It can take a lot of time and it is not readily reproducible, not by yourself and even less so by collaborators or readers of your publication. Thus, fully automated, and thereby reproducible, batch analysis is typically what is needed. In this course you will learn the basics of setting up and running fully automated analysis of many images.

## Prerequisites

* You should know how to conduct basic image analysis in python (see, e.g., the content of [this course](https://github.com/NEUBIAS/training-resources/blob/master/courses/YYYY_MM_HOST_skimage_napari_beginners.md)).

### IT Setup

Please, before the course use the `conda` platform to install skimage and napari on your laptop, following [these instructions](https://neubias.github.io/training-resources/tool_installation/index.html#skimage_napari). 

TODO: In principle we could again use Jupyter for this? Just have the processing function in one cell and the for-loop in another cell? Or shall we use some other setup?

## Schedule

The whole course will be guided hands-on sessions.

- Day, Month, Year, Times

This includes a lunch break (1 hr) and two coffee breaks (20 minutes), resulting in approximately 5 hr of teaching time.
As there are 6 modules per day that makes ~45 minutes per module.

## Venue

- Country, City, Street, Institute, Room
- Zoom link

## Trainers and organisers

- Name (Institute)
- ...

## Teaching tips

Dear Trainers, please consider checking these [teaching tips](https://github.com/NEUBIAS/training-resources/blob/master/TEACHING_TIPS.md).

## Teaching content

### Essential python scripting skills for conducting automated batch analysis (day 1)

1. Introduction
    - Trainers introduce themselves, where they work and how they are competent
    - Participants introduce themselves, where they work, why they joined the course, and what previous experience they have
        - Depending on the number of participants, one could distribute the introductions across the course, e.g. do some in the morning and some in the afternoon
1. [Loops](https://neubias.github.io/training-resources/script_for_loop/index.html)
    - Trainer
1. [String and path manipulations](https://neubias.github.io/training-resources/string_concat/index.html)
    - Trainer 
1. [Functions](https://neubias.github.io/training-resources/script_functions/index.html)
    - TODO: strictly speaking this is not needed, one could just type everything into the for-loop directly???
    - Trainer

### Conducting batch analysis using python scripting 

1. [Batch analysis](https://neubias.github.io/training-resources/batch_processing/index.html)
    - TODO: Is there an added benefit of also teaching how to make the script command line executable and give the input and output directory as CLI parameters? Disadvantage would be that we could not do this with Jupyter notebooks!
    - Trainer

## Follow-up courses

- Batch QC of image analysis results 
    - Using MoBIE to open the images, label masks, and tables
- Batch running using Nextflow
