---
title:  Image feature enhancement
layout: module
tags : ["draft"]
---

<img src='https://g.gravizo.com/svg?
digraph G {
    shift [fontcolor=white,color=white];
    image -> filter -> "enhanced image";
    node [shape=box, color=grey, fontcolor=grey];
    "enhanced image" -> "feature" [label=" aka", style=dashed, color=grey, fontcolor=grey, fontsize=10];
    "feature enhancement" [shape=box, color=grey, fontcolor=grey, margin=0.05];
    filter -> "feature enhancement" [label=" aka", style=dashed, color=grey, fontcolor=grey, fontsize=10];
}
'/>

## Examples

- Difference of Gaussian filter enhances spots
- ...

## Learn next

- filter_difference_of_gaussian.md
