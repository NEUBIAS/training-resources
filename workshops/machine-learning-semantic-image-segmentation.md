# Semantic image segmentation using machine learning

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    "intensity image" -> threshold;
    threshold -> "binary image";
    "binary image" -> "background value";
    "binary image" -> "foreground value";
    "intensity image" -> "machine learning";
    "machine learning" -> "pixel class image";
    "pixel class image" -> "class00 value";
    "pixel class image" -> "class01 value";
    "pixel class image" -> "class.. value";
    "pixel class image" -> "class N value";
 }
'/>

## Decision tree based image segmentation

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    "intensity image" -> "filter00 image" -> "Decision tree(s)";
    "intensity image" -> "filter01 image" -> "Decision tree(s)";
    "intensity image" -> "filter02 image" -> "Decision tree(s)";
    "intensity image" -> "filter.. image" -> "Decision tree(s)";
    "intensity image" -> "filter F image" -> "Decision tree(s)";
    "Decision tree(s)" -> "class00 (probability) image";
    "Decision tree(s)" -> "class01 (probability) image";
    "Decision tree(s)" -> "class.. (probability) image";
    "Decision tree(s)" -> "class C (probability) image";
 }
'/>
