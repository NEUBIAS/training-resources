---
title: Cloud based bioimage analysis course
layout: module
prerequisites:
  - "Basic shell command-line skills"
  - "Basic knowledge about cloud computing"
  - "Basic knowledge of containers"
  - "Understanding of web-based platforms and remote desktop environments"
 
objectives:
  - "Select appropriate tools for various bioimage analysis tasks"
  - "Use existing bioimage tools containers or build custom ones"
  - "Execute and manage workflows within the Galaxy platform"
  

motivation: |
  Cloud-based platforms, containers, and Galaxy workflows enable scalable, reproducible, and automated image processing. This course equips you with the skills to use and build bioimage tools, run workflows, and optimize cloud-based analysis. By mastering these technologies, you can enhance research efficiency and tackle complex image analysis tasks with ease.

concept_map: >
  graph TD;
    A("Cloud based bioimage analysis course") --> C("Bioimage tools containers");
    A("Cloud based bioimage analysis course") --> I("Cloud based interactive analysis");
    A("Cloud based bioimage analysis course") --> B("Cloud based batch analysis");


figure: /figures/cloud-course-figure.png 
figure_legend: "Cloud-based bioimage analysis tools can be categorized into three types. Bioimage Tool Containers provide standardized environments for reproducible analysis. Bioimage Interactive Analysis enables user-driven image processing. Bioimage Batch Analysis runs automated image analysis workflows without a graphical user interface (GUI)"

learn_next:
  - "[Bioimage tools containers](../containers/index.html)"


external_links:
  - "[Docker for beginers](https://www.docker.com/101-tutorial/)"
  - "[BARD Desktop](https://github.com/embl-cba/bard-containers)"
  - "[Galaxy training network](https://training.galaxyproject.org/)"
---

### General comments

The material for this course consists of the following training modules:

1. [Bioimage tools containers](../containers/index.html)
1. [Cloud based interactive analysis](../cloud_based_interactive_analysis/index.html)
1. [Cloud based batch analysis](../cloud_based_batch_analysis/index.html)


As usual, each training module contains several activities that can be executed in various compute platforms. As a trainer, it is necessary to familiarise yourself with the material and decide what to teach.

It is also highly recommended to consider our [TEACHING TIPS](https://github.com/NEUBIAS/training-resources/blob/master/TEACHING_TIPS.md).


### How to run this course

The course materials support teaching with Docker, Podman Desktop, the command-line interface, and usegalaxy.eu. Based on our experience, the course is best delivered in two sessions: the first covers Docker basics on a Linux or macOS computer, while the second is a Galaxy workflow click-through session using the [Galaxy EU instance](https://usegalaxy.eu). Learners can choose the session that aligns best with their interests.

