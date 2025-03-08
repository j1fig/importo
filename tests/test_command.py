import subprocess

import pytest


@pytest.mark.parametrize(
    "cmd,return_code",
    [
        (["importo", "-h"], 0),
        (["importo", "datetime"], 0),
        (["importo"], 2),
    ],
)
def test_command(cmd, return_code):
    r = subprocess.run(cmd)
    assert r.returncode == return_code
