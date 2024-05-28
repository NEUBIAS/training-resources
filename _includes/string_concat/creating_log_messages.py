# %%
# Creating log messages

image_index = 11
num_images = 100

# %%
# strings can be added together with the '+' operator
print("Analyzing image " + str(image_index) + "/" + str(num_images) + "...")

# %%
# An alternative way to combine strings and variables from your code
# are so called f-strings: in f-strings you can add variables (and some
# code) in between curly braces. Types are automatically coerced to strings.
#  The below code achieves the same output.
print(f"Analysing image {image_index}/{num_images}...")
