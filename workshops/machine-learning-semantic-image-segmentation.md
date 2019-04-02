# Semantic image segmentation using machine learning

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    "intensity image" -> threshold;
    threshold -> "binary image";
    "binary image" -> "background value";
    "binary image" -> "foreground value";
    "intensity image" -> "machine learning";
    "machine learning -> "pixel class image";
    "pixel class image" -> "class01 value";
    "pixel class image" -> "class02 value";
    "pixel class image" -> "class.. value";
 }
'/>
