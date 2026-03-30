from tsproc.timeseries import TimeSeries
from tsproc.resampler import Resampler

def test_get_pass():
    assert TimeSeries({'t1':1}).get('t1')==1

def test_resample_mean_pass():
    assert Resampler().aggregate([1,2,3])==2

def test_resample_sum_pass():
    assert Resampler().aggregate([1,2,3],'sum')==6

def test_resample_max_pass():
    assert Resampler().aggregate([1,2,3],'max')==3

def test_resample_min_pass():
    assert Resampler().aggregate([1,2,3],'min')==1
