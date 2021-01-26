---
title: Filter objects 
layout: module

prerequisites:
  - "[Connected components labeling](../connected_components)"

objectives:
  - Remove objects from a label mask image.

motivation: >
  Once objects have been identified in an image, one often filters the objects based on certain measured criteria. For example, very small objects may be noise rather than real objects and could be removed.

concept_map: >
  graph TD
    L("Label image") -->|"remove label(s)"| ML("Modified label image")

figure: /figures/filter_objects.png
figure_legend: 

activity_preface: |
  Open a label mask image and remove labels (objects) from it. Discuss how filtering can also be done afterwards using a spread-sheet software. 
  Advantages to create a filtered label image.
  
activities:
    - ["ImageJ Macro & GUI", "filter_objects/activities/filter_objects_imagejmacro_gui.ijm", "java"]

exercises:
    - ["ImageJ Macro & GUI", "filter_objects/exercises/filter_objects_imagejmacro_gui.md"]

assessment: >

  ### True of false?

    1. In bioimage analysis one should always remove all labels that touch the image boundary.
    1. The largest object has the highest label index.
    1. If you remove one object the number of distinct labels decreases by one.
    
    > ## Solution
    >   1. Very often, but not always. Sometimes it also is an option to normalise downstream measurements by the visible size of objects.
    >   1. No, the label index usually has no meaning.
    >   1. Yes.
    {: .solution}

  ###  Discuss with your neighbour

    1. Is it a good idea to manually remove objects (labels) from an image or should this rather be an automated procedure?
    1. What are the pros and cons of removing labels from the image as opposed to keeping all of them and removing the corresponding object measurements later during statisitical analysis of the measurement results?

    > ## Solution
    > 1. Automated typically is better as it forces you to define objective and reproducible criteria for which objects to remove.
    > 1. Very important topic, but too much to write, ask your bioimage analysis consultant ;-)
    {: .solution}
    
learn_next:

external_links:

---
