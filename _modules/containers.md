---
title: Bioimage tools containers
layout: module
tags: ["draft"]
prerequisites:
  - "Basic familiarity with command-line(e.g., cd, ls, mkdir, rm)"
  - "Basic knowledge of software installaion on Linux/macOS"
  - "Ability to read and edit text files using command-line editor (e.g., nano, vim)"
  - "Some experience with version control (e.g., Git))"
objectives:
  "By the end of this course, learners will will understand the fundamentals of containers, including installation, image management, container execution. They will also gain hands-on experience in building, running their own containers."
motivation: |
  Containers provide a lightweight, reproducible, and portable way to package and run applications across different environments. This module introduces Docker as a tool for simplifying software deployment. By learning container basics, users can streamline workflows, improve reproducibility, and easily share applications in research and development.

concept_map: >
  graph TD
    A[Docker Containers]
    
    A --> D[Installation]
    A --> E[Docker Images]
    A --> F[Running Containers]
    A --> G[Managing Containers]
    
    D --> D1[Linux/macOS]
    D --> D2[Verifying Installation]

    E --> E1[Pulling Images]
    E --> E2[Building Custom Images]

    F --> F1[docker run]
    F --> F2[Interactive vs Batch Mode]

    G --> G1[Listing Containers]
    G --> G2[Stopping & Removing]


figure: /figures/container-figure.png
figure_legend: Example container architecture

multiactivities:
  - ["containers/act01.md", [["Linux(Ubuntu)", "containers/act01_ubuntu.md"], ["macOS", "containers/act01_mac.md"]]]
  - ["containers/act02.md", [["Run a simple container", "containers/act02_simple.md"], ["Run CellPose container", "containers/act02_cellpose.md"]]]
  - ["containers/act03.md", [["Understand Dockerfile", "containers/act03_understand.md"], ["Build from Dockerfile", "containers/act03_build.md"]]]

external_links:
  - "[Docker Docs](https://docs.docker.com/)"
  - "[Podman Docs](https://docs.podman.io/en/latest/)"
---

