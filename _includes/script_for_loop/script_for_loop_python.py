# %%
# Create a bunch of example images to simulate a typical analysis problem
# np.random.randint(lower,upper,size): generates random integers from lower to upper
# .reshape: reshapes a np.array to new dimensions
import numpy as np
image1 = np.random.randint(0,255,100).reshape((10,10))
image2 = np.random.randint(0,255,100).reshape((10,10))
image3 = np.random.randint(0,255,100).reshape((10,10))
image4 = np.random.randint(0,255,100).reshape((10,10))
image5 = np.random.randint(0,255,100).reshape((10,10))
image6 = np.random.randint(0,255,100).reshape((10,10))
image7 = np.random.randint(0,255,100).reshape((10,10))
image8 = np.random.randint(0,255,100).reshape((10,10))
image9 = np.random.randint(0,255,100).reshape((10,10))
image10 = np.random.randint(0,255,100).reshape((10,10))

# Calculate the mean of every image
# Oberserve that it is very tedious and error prone
print(f'Image {1} has an avg intensity of {image1.mean()}.')
print(f'Image {2} has an avg intensity of {image2.mean()}.')
print(f'Image {3} has an avg intensity of {image3.mean()}.')
print(f'Image {4} has an avg intensity of {image4.mean()}.')
print(f'Image {5} has an avg intensity of {image5.mean()}.')
print(f'Image {6} has an avg intensity of {image6.mean()}.')
print(f'Image {7} has an avg intensity of {image7.mean()}.')
print(f'Image {8} has an avg intensity of {image8.mean()}.')
print(f'Image {9} has an avg intensity of {image9.mean()}.')
print(f'Image {10} has an avg intensity of {image10.mean()}.')

# %%
# Create a for loop
# Typical notation in C-style: for i=0, i<10, i++ {do something}
# For loop in python
# Observe the difference in notation
for i in [0,1,2,3,4,5,6,7,8,9]:
    print(i)

# use range
# Observe that range is actually a generator producing values on the fly
print(range(10))
print(type(range(10)))
for i in range(10):
    print(i)

# %%
# Use a for loop for the example in the beginning
# First pack images into a list for looping over
image_list = [image1,image2,image3,image4,image5,image6,image7,image8,image9,image10]

# Loop over images and calculate the mean
for image in image_list:
    print(f'Avg intensity: {image.mean()}')

# Excersize: Modify the loop to calculate the standard deviation
for image in image_list:
    print(f'Intensity standard deviation: {image.std()}')

#%%
# Iterate with an index
number_of_images = len(image_list)
print(number_of_images)
for i in range(number_of_images):
    print(f'Image {i} has an avg intensity of {image_list[i].mean()}.')

# Iterate with additional index
for i,image in enumerate(image_list):
    print(f'Image {i} has an avg intensity of {image.mean()}.')
