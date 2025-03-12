---
title: Cloud based interactive analysis
layout: module
prerequisites:
  - "[Bioimage tools containers ](../containers)"
objectives:
  - "Understand interactive analysis platforms, including virtual desktops, Galaxy interactive tools, and Jupyter notebooks for bioimage analysis."
  - "Run bioimage tools, such as CellPose on virtual desktops"
  - "Run Galaxy Interactive Tools for bioimage analysis"
motivation: |
  Bioimage analysis requires interactive tools that combine computational power with user-friendly interfaces, enabling researchers to process and analyze complex image datasets efficiently.In this course, we introduce BARD Virtual Desktop, Galaxy interactive tools, providing hands-on experience in deploy bioimage tools to these platforms.

concept_map: >
  graph TD
    T1("Bioimage interactive analysis") 
    T2("Virtual Desktops")--> T1
    T3("Galaxy Interactive Tools")--> T1
    T4("Containerized GUI app")--> T1
 

figure: /figures/cloud_based_interactive_analysis.png
figure_legend: Key components that enable efficient bioimage interactive analysis

multiactivities:
  - ["cloud_based_interactive_analysis/act01.md", [["BARD Desktops", "cloud_based_interactive_analysis/act01_bard01.md"], ["Galaxy Interactive Tools", "cloud_based_interactive_analysis/act01_git01.md"]]]
  - ["cloud_based_interactive_analysis/act02.md", [["BARD Desktops", "cloud_based_interactive_analysis/act02_bard_deploy_app.md"], ["Galaxy Interactive Tools", "cloud_based_interactive_analysis/act02_git_deploy_app.md"]]] 

learn_next:
  - "[Cloud based batch analysis](../cloud_based_batch_analysis/index.html)"

external_links:
  - "[BARD Desktop](https://bard-external.embl.de)"
  - "[Galaxy Interactive Tools](https://training.galaxyproject.org/training-material/topics/admin/tutorials/interactive-tools/tutorial.html) "
---

