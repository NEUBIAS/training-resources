---
title: Coding with LLMs
layout: module
tags: ["draft"]
prerequisites:
  - "[Running a script](../script_run)"
objectives:
  - Use a large language model (LLM) to create bioimage analysis code
  - Use a LLM to understand bioimage analysis code
motivation: |
  Creating and understanding bioimage anlaysis code can be very challenging, especially for coding beginners. Large language models (LLMs) are very useful tools to generate code based on instructions formulated in normal language. Moreover, LLMs can also be asked to explain parts of the code in normal language. Therefore, using LLMs can save a lot of time when creating code for bioimage analysis or other tasks. 

concept_map: >
  graph TD
    CS("'Create a script that...'") --> LLM("Large language model (LLM)")
    LLM --> S("from skimage import io\nimage = io.imread('cells.tif')\n...")

figure: /figures/coding_with_llms.png
figure_legend: "TODO: create a better figure; current figure shows not so great success using DALL-E"

multiactivities:
  - ["coding_with_llms/code_creation.md", [["chatGPT python", "coding_with_llms/code_creation_chatGPT_python.md"]]]

assessment: >

  ### True or false

    1. If you ask a large language model to generate code for you it will reprodcibly give you the exact same answer.
    1. The code that is produced by a large language model can be used to do reproducible science.
    
    > ## Solution
    >   1. This is generally wrong; several common models have some randomicity in their outputs.
    >   1. This is true; you just have to store code once it has been generated, e.g. using version control systems such as git.
    {: .solution}

learn_next:
  - "[Automatic threshold for binarization](../auto_threshold)"

external_links:
  - "[bia-bob](https://github.com/haesleinhuepf/bia-bob)"
---

