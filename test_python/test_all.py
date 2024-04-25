import pathlib
import runpy
import pytest

scripts = map(str, (pathlib.Path(__file__).parent / '..'/ '_includes').resolve().glob('**/*.py'))


@pytest.mark.parametrize('script', scripts)
def test_script_execution(script):
    runpy.run_path(script)
