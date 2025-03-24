"""
Search for `.py` script files in the _include folder and run them.
"""

import pathlib
import runpy

import pytest


def filter_criteria(filename):
    exclude_filters = ("jython",)
    if any(filt in str(filename).lower() for filt in exclude_filters):
        return False

    bioioimports = ("import bioio", "from bioio")
    content = filename.read_text()
    if any(bioimp in content for bioimp in bioioimports):
        return True

    return False

scripts = filter(filter_criteria, (pathlib.Path(__file__).parent / ".." / "_includes").resolve().glob("**/*.py"))


known_failures = {
    "measure_intensities_act1_skimage_napari.py": "Requires manual interaction to pass.",
    "spatial_calibration_act1_skimage_napari.py": "Requires manual interaction to pass.",
    "volume_slicing_act1_python-napari.py": "Not supposed to be run in a script, but in the napari viewer itself.",
    "batch_measure_nuclei_shape.py": "Requires image download.",
}


@pytest.mark.parametrize("script", [pytest.param(script, id=script.name) for script in scripts])
def test_script_execution(script: pathlib.Path):
    if script.name in known_failures:
        pytest.xfail(known_failures[script.name])
    runpy.run_path(script.as_posix())
