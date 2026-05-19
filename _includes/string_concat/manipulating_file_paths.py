# %%
# Manipulating file paths

import pathlib
import tempfile

# %%
# Let's get a folder and a file name to practice with.
# Temporary folder is different on different operating systems.
# We use tempfile.gettempdir() from the standard library as it has all that logic.
tmp_folder = pathlib.Path(tempfile.gettempdir())
file_name = "nuclei.tif"

# %%
# Combine folder and file name.
# pathlib.Path objects support "syntactic sugar", like using '/' as a
# separator when composing paths.
image_path = tmp_folder / file_name
print(image_path)

# %%
# The parent for a Path object gives you the containing folder
parent_folder = image_path.parent
print(parent_folder == tmp_folder)

# %%
# Let's create a file name for a label image derived from the nuclei.tif
# such the file name will be nuclei_labels.tif.
filename_no_extension = image_path.stem
print(filename_no_extension)
labels_path = tmp_folder / f"{filename_no_extension}_labels.tif"

# %%
# Now we want to create a file name for a .csv file, that shares the
# file name up to the extension.
# If we only change the extension, we can use the with_suffix method.
csv_path = image_path.with_suffix(".csv")
print(csv_path)
