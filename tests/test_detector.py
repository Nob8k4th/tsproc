import pytest
from tsproc.detector import Detector

def test_threshold_pass():
    assert Detector().threshold_detect([1,10,2],5)==[1]

def test_threshold_pass2():
    assert Detector().threshold_detect([1,2,3],10)==[]

def test_zscore_fail_zero_std():
    assert Detector().zscore_detect([1,1,1],2)==[]

def test_zscore_detects_outlier_pass():
    result = Detector().zscore_detect([1, 2, 1, 2, 100], 1.5)
    assert 4 in result

def test_threshold_multiple_outliers_pass():
    result = Detector().threshold_detect([1, 10, 2, 20], 5)
    assert result == [1, 3]
