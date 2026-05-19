<h4 id="semantic_comparison"><a href="#semantic_comparison">Semantic comparison using IoU</a></h4>

 - Open the reference and candidate segmentation masks
 - Convert each label mask to a binary mask (foreground > 0)
 - Compute the IoU against the reference for the low-threshold and high-threshold results
 - Compare which thresholding result gives the higher IoU and discuss why
