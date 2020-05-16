```
// determine the touch matrix
Ext.<a href="https://clij.github.io/clij2-docs/reference_generateTouchMatrix">CLIJ2_generateTouchMatrix</a>(label_map, touch_matrix);

// draw mesh
Ext.<a href="https://clij.github.io/clij2-docs/reference_touchMatrixToMesh">CLIJ2_touchMatrixToMesh</a>(pointlist, touch_matrix, mesh);
Ext.CLIJ2_pull(mesh);
```