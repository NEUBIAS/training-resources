# Image binarization
 
<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    intenstiy_image -> threshold;
    threshold -> background [label="  <threshold"];
    threshold -> foreground [label="  >=threshold"];
    background -> binaryimage;
	foreground -> binaryimage;
	binaryimage -> 0 [label="  background"];
	binaryimage -> 1 [label="  foreground"];   
  }
'/>

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    ![Figure 1-1](images/xy_8bit__two_cells.tif "Figure 1-1") -> threshold;
    threshold -> background [label="  <threshold"];
    threshold -> foreground [label="  >=threshold"];
    background -> binaryimage;
	foreground -> binaryimage;
	binaryimage -> 0 [label="  background"];
	binaryimage -> 1 [label="  foreground"];   
  }
'/>
