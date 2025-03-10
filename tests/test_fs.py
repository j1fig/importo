import os

from importo import fs
import pytest


HOME_DIR = os.getenv("HOME")


@pytest.mark.parametrize(
    "path,expected",
    [
        ("/usr/",               "/usr"),
        ("~/dev/importo/tests", HOME_DIR + "/dev/importo/tests"),
    ],
)
def test_resolves_absolute_paths(path, expected):
    assert fs.resolve_to_absolute_path(path) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("/Users/some/dev/importo/.git/objects/42",         True),
        ("/Users/some/dev/importo/src/importo/__pycache__", True),
        ("/Users/some/dev/importo/src/importo/",            False),
    ],
)
def test_detects_ignored_dirs(path, expected):
    assert fs.has_ignored_dir(path) == expected
