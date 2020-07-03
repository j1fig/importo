import pytest

from importo import utils


@pytest.mark.parametrize("array,percentile,result", [([15, 20, 35, 40, 50], 40, 29.0),])
def test_percentile(array, percentile, result):
    assert result == utils.percentile(array, percentile)


@pytest.mark.parametrize("array,result", [([15, 20, 35, 40, 50], 32.0),])
def test_avg(array, result):
    assert result == utils.avg(array)
