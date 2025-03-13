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
    L1("Client computer") -->|"shell, browser"| CR("Cloud resource")
    CR --- OS("Software\n(Platform, Applications)")
    OS --- H("Hardware")
    CR ---|examples| E("Google Colab\nSlurm cluster\nVirtual Desktops\n Galaxy\n...")
    
figure: /figures/cloud-course-figure.png 
figure_legend: "There are cloud-based solutions for both interactive and automated batch analysis of microsopy image data."

learn_next:
  - "[Bioimage tools containers](../containers/index.html)"

external_links:
  - "[Docker for beginers](https://www.docker.com/101-tutorial/)"
  - "[BARD Desktop](https://github.com/embl-cba/bard-containers)"
  - "[Galaxy training network](https://training.galaxyproject.org/)"
---


The material for this course consists of the following training modules:

- [Bioimage tools containers](../containers/index.html)
- [Cloud based interactive analysis](../cloud_based_interactive_analysis/index.html)
- [Cloud based batch analysis](../cloud_based_batch_analysis/index.html)


As usual, each training module contains several activities that can be executed in various compute platforms. As a trainer, it is necessary to familiarise yourself with the material and decide what to teach.

It is also highly recommended to consider our [TEACHING TIPS](https://github.com/NEUBIAS/training-resources/blob/master/TEACHING_TIPS.md).
