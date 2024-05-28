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
path = tmp_folder / file_name
print(path)
