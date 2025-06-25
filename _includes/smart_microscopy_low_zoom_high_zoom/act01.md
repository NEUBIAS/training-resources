<h4 id="act01"><a href="#act01">Basic targeted acquisition workflow</a></h4>

- Manual configuration and test at the microscope
    - Setup imaging settings for low zoom and high zoom acquisition jobs
    - (If available) Save all settings as imaging jobs (observation methods) in microscope software
    - Acquire and save example images for testing and debugging image analysis

- Image analysis
    - Define or re-use image analysis function implementing threshold-based segmentation of nuclei
    - Use acquired images to test segmentation parameters

- Configure and run feedback microscopy pipeline
    - Define default positions for the feedback microscopy (the same as positions for screening)
    - Configure selected feedback microscopy tool (see implementations) by linking pre-configured acquisition settings and segmentation protocol as parameters.
    - Run the pipeline
