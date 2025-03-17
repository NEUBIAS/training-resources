---
title: Cloud based bioimage analysis course overview
layout: module
prerequisites:
  - "Basic knowledge of desktop based image analysis tools, e.g. Fiji"
  - "Basic shell command-line skills"

objectives:
  - "Execute cloud based interactive biomage analysis tools"
  - "Execute and manage cloud based batch analysis workflows"
  - "Use bioimage tool containers"
  - "Create bioimage tool containers"
  

motivation: |
  Cloud-based platforms, containers, and Galaxy workflows enable scalable, reproducible, and automated image processing. This course equips you with the skills to use and build bioimage tools, run workflows, and optimize cloud-based analysis. By mastering these technologies, you can enhance research efficiency and tackle complex image analysis tasks with ease.

concept_map: >
  graph TD;
    C("Client computer(s)") -->|"shell, browser"| CR("Cloud resource\n\n(Google Colab, Slurm cluster,\nVirtual desktop, Galaxy, ...)")
    CR --- S("Software")
    CR --- H("Hardware")
    
figure: /figures/cloud-course-figure.png 
figure_legend: "Cloud based bioimage analysis."

learn_next:
  - "[Cloud based interactive analysis](../cloud_based_interactive_analysis/index.html)"

external_links:
  - "[Docker for beginers](https://www.docker.com/101-tutorial/)"
  - "[BARD Desktop](https://github.com/embl-cba/bard-containers)"
  - "[Galaxy training network](https://training.galaxyproject.org/)"
---


The material for this course consists of the following training modules:

- [Cloud based interactive analysis](../cloud_based_interactive_analysis/index.html)
- [Cloud based batch analysis](../cloud_based_batch_analysis/index.html)
- [Bioimage tools containers](../containers/index.html)


As usual, each training module contains several activities that can be executed on various compute platforms. As a trainer, it is necessary to familiarise yourself with the material before and decide which activities to teach. It is also highly recommended to consider our [TEACHING TIPS](https://github.com/NEUBIAS/training-resources/blob/master/TEACHING_TIPS.md).
