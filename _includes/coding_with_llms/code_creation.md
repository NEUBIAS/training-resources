<h4 id="create_code_llm"><a href="#create_code_llm">Create code using a LLM</a></h4>

Ask an LLM to create code that implements a bioimage analysis task.

Activities that could be solved using a LLM:
- [Threshold an image](https://neubias.github.io/training-resources/binarization/index.html#brightdim)  
- [Segment nuclei and measure their shape](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html#2dnuclei)

Tips for creating the prompt:
- Often the instructions given in the activity can be a good starting point to create the LLM prompt.
- Tell the LLM in which programming language you would like the code to be implemented.
- Sometimes it may also be good to tell it which libraries to use. For example, chatGPT seems to like "openCV" while "skimage" is more what we may typically use in bioimage anlaysis.
- Tell the LLM where exactly the input data is stored on your computer such that it can write the code to open the data.

Fixing errors:
- If you get an error executing the code, create a new prompt with this error and ask the LLM to fix it.

Understanding the code:
- If you do not understand parts of the code ask the LLM to explain them to you.

 
