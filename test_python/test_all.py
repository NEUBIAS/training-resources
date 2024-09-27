import pathlib
import runpy

import pytest

scripts = filter(
    lambda x: "jython" not in x.lower(),
    map(lambda x: x.as_posix(), (pathlib.Path(__file__).parent / ".." / "_includes").resolve().glob("**/*.py")),
)


known_failures = {
    "measure_intensities_act1_skimage_napari.py": "Requires manual interaction to pass.",
    "spatial_calibration_act1_skimage_napari.py": "Requires manual interaction to pass.",
    "volume_slicing_act1_python-napari.py": "Not supposed to be run in a script, but in the napari viewer itself.",
}


@pytest.mark.parametrize("script", scripts)
def test_script_execution(script):
    if (script_name := pathlib.Path(script).name) in known_failures:
        pytest.xfail(known_failures[script_name])
    runpy.run_path(script)
