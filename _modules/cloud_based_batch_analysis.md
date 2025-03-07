---
title: Cloud based batch analysis
layout: module
prerequisites:
  - "[Bioimage tools containers ](../containers)"
objectives:
  - "Understand how to leverage cloud computing platforms, such as Galaxy, for efficient bioimage batch analysis"

motivation: |
  Bioimage analysis requires significant computational power, making local processing inefficient and time-consuming. By leveraging cloud-based batch processing, researchers can scale their analyses, automate workflows, and handle imaging data with greater efficiency.

concept_map: >
  graph TD
    T1("Bioimage batch analysis") 
    T2("Galaxy")--> T1
    T3("Nextflow")--> T1
    T4("Others")--> T1
 

figure: /figures/cloud_based_batch_analysis.png
figure_legend: Key components that enable efficient bioimage batch analysis

multiactivities:
  - ["cloud_based_batch_analysis/act01.md", [ ["Batch containers", "cloud_based_batch_analysis/act01_headless_containers.md"],["Galaxy", "cloud_based_batch_analysis/act01_galaxy.md"], ["Nextflow", "cloud_based_batch_analysis/act01_nf.md"]]]

external_links:
  - "[Galaxy Training Network](https://training.galaxyproject.org/)"
  - "[Nextflow Training](https://training.nextflow.io/latest/) "
---
