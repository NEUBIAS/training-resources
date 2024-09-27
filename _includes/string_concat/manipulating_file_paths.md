<h4 id="manipulate_paths"><a href="#manipulate_paths">Manipulate file paths</a></h4>

In bioimage analysis, one very often opens one image and then needs to save a segmentation (label mask file) and segmented object measurements (a table file). To this end, it is useful if the output images have similar names than the input image, such that one knows that they belong to each other. Sometimes it is useful for those output files to be placed in the same folder as the input image, but often you want to specify a dedicated output folder.

To manage all these scenarios it is critical to learn how to manipulate file and folder paths in various ways and thereby construct the output paths from the input path and a given output directory.
