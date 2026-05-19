---
title: Table file formats (DRAFT)
layout: module
tags: ["draft"]
prerequisites:
objectives:
  - "Understand the pros and cons of a number of table file formats"
motivation: |
  Next to images, tables are the most prevalent data format in bioimage analysis. For instance, segmenting cells in a image very often results in a cells by features table, including cell shape or intensity measurements. To effectively share these measurements it is very important to understand how to write and read tabular data.

concept_map: >
  graph TD
    M("Measurements") --> T("Table")
    T --> F("On disk representation")

figure: /figures/table_file_formats.png
figure_legend: TODO

multiactivities:
  - ["table_file_formats/parquet.md", [["Java TableSaw", "table_file_formats/ParquetTableSaw.java"], ["Python PyArrow", "table_file_formats/parquet_pyarrow.py"]]]

assessment: >

  ### Fill in the blanks

    1. TODO ___ .
    1. TODO ___ .
    
    > ## Solution
    >   1. TODO
    >   1. TODO
    {: .solution}

learn_next:
  - "[TODO](../auto_threshold)"

external_links:
  - "[Wikipedia: Binary image](https://en.wikipedia.org/wiki/Binary_image)"
---

