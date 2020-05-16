```python
from ij import IJ;
from net.haesleinhuepf.clij2 import CLIJ2;

threshold = 30;

inputImage = IJ.getImage()

# init GPU
clij2 = CLIJ2.getInstance();

# push image to GPU
input = clij2.push(inputImage);

# reserve memory for output, same size and type as input
output = clij2.create(input);

# apply a given fixed threshold on GPU
clij2.threshold(input, output, threshold);

# Show result
clij2.pullBinary(output).show();
IJ.setMinAndMax(0, 255);


```
