---
title: Object filtering
layout: module
prerequisites:
  - "[Connected component labeling](../connected_components)"
  - "[Object shape measurements](../measure_shapes)"
objectives:
  - Remove objects from a label mask image.
motivation: >
  Once objects have been identified in an image as a result of image segmentation, one often filters the objects based on certain measured criteria. For example, very small objects may be noise rather than real objects and could be removed.

concept_map: >
  graph TD
    L("Label mask") -->|"remove label(s)"| ML("Modified label mask")

figure: /figures/filter_objects.png

figure_legend: Object filtering. Left - Noisy labeled mask. Middle - Mask after removing border objects. Right - Mask after removing smaller objects (noise).

activity_preface: |
  - Open a label mask image [xy_8bit_labels__noisy_nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__noisy_nuclei.tif)
  - Remove border labels
  - Remove small (noise) labels

activities:
    - ["ImageJ GUI", "filter_objects/activities/filter_objects_imagejgui.md", "markdown"]
    - ["ImageJ Macro", "filter_objects/activities/filter_objects_imagejmacro.ijm", "java"]

exercises:
    - ["ImageJ GUI", "filter_objects/exercises/filter_objects_imagejgui.md"]

assessment: >

  ### True of false?

    1. In bioimage analysis, one should always remove all labels that touch the image boundary.
    1. The largest object has the highest label index.
    1. If you remove one object, the number of distinct labels decreases by one.

    > ## Solution
    >   1. Very often, but not always. Sometimes it also is an option to normalize downstream measurements by the visible size of objects.
    >   1. No, the label index usually has no meaning.
    >   1. Yes.
    {: .solution}

  ###  Discuss with your neighbor

    1. Is it a good idea to manually remove objects (labels) from an image or should this rather be an automated procedure?
    1. What are the pros and cons of removing labels from the image as opposed to keeping all of them and removing the corresponding object measurements later during statistical analysis of the measurement results?

    > ## Solution
    > 1. Automated typically is better as it forces you to define objective and reproducible criteria for which objects to remove.
    > 1. Pro: (i) Reduce computational load for further processing (e.g. morphological filters), (ii) Label mask image is easier to inspect visually (less clutter); Con: (i) You cannot check during analysis how your conclusions would have changed including those objects, (ii) ...
    {: .solution}

learn_next:

external_links:

---
