"""
Search for `.py` script files in the _include folder and run them in batches.
Only runs scripts that should work on all platforms

(e.g. scripts that require bioconda packages cannot be run on windows)
"""

import pathlib
import runpy
import sys
import pytest
import napari  # Import napari to potentially interact with its state

def filter_criteria(filename):
    exclude_filters = ("jython",)
    if any(filt in str(filename).lower() for filt in exclude_filters):
        return False

    bioioimports = ("import bioio", "from bioio")
    content = filename.read_text()
    if any(bioimp in content for bioimp in bioioimports):
        return False

    return True

scripts = list(filter(filter_criteria, (pathlib.Path(__file__).parent / ".." / "_includes").resolve().glob("**/*.py")))

known_failures = {
    "measure_intensities_act1_skimage_napari.py": "Requires manual interaction to pass.",
    "spatial_calibration_act1_skimage_napari.py": "Requires manual interaction to pass.",
    "volume_slicing_act1_python-napari.py": "Not supposed to be run in a script, but in the napari viewer itself.",
    "batch_measure_nuclei_shape.py": "Requires image download.",
    "parquet_pyarrow.py": "Unfinished script/module",
    "pixels_act1_skimage_napari.py": "Requires active window napari viewer"
}

def run_script(script: pathlib.Path):
    if script.name in known_failures:
        pytest.xfail(known_failures[script.name])
    print(f"Running script: {script}")
    runpy.run_path(script.as_posix(), run_name="__main__")
    print(f"Finished running script: {script}")

def batched_execution(scripts, max_scripts):
    if max_scripts > len(scripts) - 1:
        max_scripts = len(scripts) -1 
    batch = scripts[0:max_scripts]
    print(f"\n--- Running batch {max_scripts}  ---")
    for script in batch:
        run_script(script)
    print(f"--- Finished batch {max_scripts} ---")

@pytest.mark.parametrize("batch_size", [10])  # Example batch sizes, adjust as needed
def test_script_execution_batched(batch_size):
    batched_execution(scripts, batch_size)