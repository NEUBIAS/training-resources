<h4 id="batchshape"><a href="#batchshape">Batch analysis of nuclear shapes</a></h4>

- In a previous module [there is a workflow to measure the shapes of nuclei in one image](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html#2dnuclei)
- Adapt this workflow for automated batch analysis of many images
- Start by building the skeleton of the workflow without filling in the functionality;
  
  Note that the code below runs fine, but does not produce any results:

```
def analyse(image_path, output_folder):
    print("Analyzing:", image_path)
    
for image_path in image_paths:
    analyse(image_path, output_dir)
```

 - Make sure the loop with the (almost) empty analyse function runs without error before filling in the image analysis steps