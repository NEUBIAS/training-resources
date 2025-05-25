---
title: Watershed
layout: module

prerequisites:
  - "[Connected component labeling](../connected_components)"
  - "[Distance transform](../distance_transform)"
objectives:
  - "Understand the concept of watersheds in image analysis."
  - "Understand that a watershed algorithm is often applied to a distance map to split objects by their shape."
  - "Be able to run a watershed algorithm in an image analysis platform."
motivation: |
  The segmentation of touching objects often is a challenge in image analysis. The watershed algorithm is a very common operation to split touching objects and is available in most image analysis frameworks.

concept_map: >
  graph TD
    T("Image") --> W("Watershed transform")
    SP("Seed points (at local intensity minima)") --> W
    W --> S("Segmented image")
    S --- B("Boundaries / Watersheds (at intensity ridges)")

figure: /figures/watershed.png
figure_legend: Illustration of the watershed transform. a) Image with three objects that cannot be separated by a simple threshold. b) Foreground/background segmentation of (a). c) Inverse of (a). d) Intensity line profile along the line depicted in (c) with illustration of filling up the basins up to a the level where the yellow and blue regions meet and a first watershed is build. e) As (d) but filling up the basins to a higher level where a second watershed is build between the blue and red region. f) Watershed transform of (c). g) (f) masked with (b). 

activity_preface: |
  - Basic watershed
    - Open [xy_8bit__touching_objects.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__touching_objects.tif).
    - Appreciate that you cannot segment the three objects using a simple threshold.
    - Anyway find a threshold that segments the image into foreground (objects) and background.
      - Keep this binary mask, we will need it later.
    - Invert the original image and apply the watershed transform.
    - Appreciate that the image is now split into three regions.
    - Combine the binary mask and the watershed image to segment the three objects.
  - Shape watershed
     - Open [xy_8bit__touching_objects_same_intensity.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__touching_objects_same_intensity.tif).
    - Appreciate that you cannot segment the objects using a simple threshold.
    - Appreciate that a watershed transform on the intensity signal does not help here, because there is no "intensity ridge" bewteen the two touching objects.
    - Create a binary mask.
    - Create a distance map within objects.
    - Invert the distance map.
    - Slightly blur the distance map to avoid spurious minima (water basins).
    - Apply a watershed transform.
    - Combine the binary mask and the watershed image to segment the two objects.
  - Seeded watershed for noisy data
    - Open [xy_8bit__noisy_touching_objects.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__noisy_touching_objects.tif).
    - Invert the image and apply the watershed transform.
    - Appreciate that this does not work because there are too many basin due to the noise.
      - Note that one could tackle this by applying a smoothing filter, but we want to explore another route now.
    - Open [xy_8bit_binary__touching_objects_markers.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__touching_objects_markers.tif).
      - This image marks the centers of the three objects.
    - Combing the two images run a seeded watershed transform to split the image into three regions.
      - For segmenting the three objects one would have to apply a mask to the resulting image (see activities above).

activities:
- ["ImageJ Macro: MorpholibJ basic watershed", "watershed/activities/watershed_basic_morpholibj.ijm", "java"]
- ["ImageJ GUI: MorpholibJ basic watershed", "watershed/activities/watershed_basic_morpholibj_imagejgui.md", "markdown"]
- ["ImageJ Macro: MorpholibJ shape watershed", "watershed/activities/watershed_shape_morpholibj.ijm", "java"]
- ["ImageJ Macro: MorpholibJ seeded watershed", "watershed/activities/watershed_seeded_morpholibj.ijm", "java"]

exercise_preface: |
  - Shape watershed
    - Open [xy_8bit__several_touching_nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__several_touching_nuclei.tif)
    - Using the watershed transform try to segment the nuclei.
      - Hints:
        - Directly applying a watershed on the inverted image will likely fail as there are too many intensity maxima even within one nucleus. Thus, one will need to binarise the image and perform a watershed on the distance transform.
  - Seeded watershed
    - The full challenge would be to segment the cells and nuclei in this image: [xyc_16bit__nuclei_tubulin.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/watershed/xyc_16bit__nuclei_tubulin.tif)
    - However, to make it easier we will start from preprocessed data:
      - Open tubulin mask: [xy_8bit_binary__tubulin.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/watershed/xy_8bit_binary__tubulin.tif)
      - Open nuclei mask: [xy_8bit_binary__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/watershed/xy_8bit_binary__nuclei.tif)
      - Open smooth tubulin: [xy_16bit__tubulin_smooth.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/watershed/xy_16bit__tubulin_smooth.tif)
    - Using the three preprocessed images perform a seeded watershed to segment the cells.

exercises:
  - ["ImageJ Macro: MorpholibJ shape watershed", "watershed/exercises/morpholibj_shape_watershed_exercise.ijm"]
  - ["ImageJ Macro: MorpholibJ seeded watershed", "watershed/exercises/morpholibj_seeded_watershed_exercise.ijm"]


assessment: >

  ### Fill in the blanks

    - The output of watershed transform is a  ___ .
    - Before applying the watershed transform on a flurorescence image, one often ___ and ___ the image.
    - When providing the watershed basins one speaks of a ___ watershed transform.

    > ## Solution
    >   - label mask image
    >   - inverts and smoothes
    >   - seeded (or marker controlled)
    {: .solution}

keypoints:
  - A watershed transform can separate touching objects if there are intensity valleys (or ridges) between touching objects. In case of intensity ridges the image needs to be inverted before being subjected to the watershed transform.
  - To separate object by their shape, use a distance transform on the binary image and inject this into the watershed transform. It is often good to smooth the distance transform to remove spurious minima, which could serve as wrong seed points and thus lead to an over-segmentation.

learn_next:

external_links:
  - "[Wikipedia: Watershed image processing](https://en.wikipedia.org/wiki/Watershed_(image_processing))"
---

