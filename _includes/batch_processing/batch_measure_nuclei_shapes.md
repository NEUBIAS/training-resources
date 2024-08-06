<h4 id="batchshape"><a href="#batchshape">Batch analysis of nuclear shapes</a></h4>

- Download the [input.zip](https://github.com/NEUBIAS/training-resources/raw/master/image_data/batch_process/inputs.zip) containing the input images and unpack to your course directory
- In a previous module [there is a workflow to measure the shapes of nuclei in one image](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html#2dnuclei)
- Adapt this workflow for automated batch analysis of many images
- Start by building the skeleton of the workflow without filling in the functionality;
  
  Note that the pseudo-code below will run fine, but does not produce any results:

```
FUNCTION analyse(image_path, output_folder)
    PRINT "Analyzing:", image_path
END FUNCTION

FOR each image_path in image_paths
    CALL analyse(image_path, output_dir)
END FOR
```

 - Make sure the loop with the (almost) empty analyse function runs without error before filling in the image analysis steps
 - Inspect the analysis results in a suitable software

