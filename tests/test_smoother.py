from tsproc.smoother import Smoother

def test_sma_fail_last_window():
    assert Smoother().sma([1,2,3,4],2)==[1.5,2.5,3.5]

def test_sma_fail_second_case():
    assert Smoother().sma([2,2,2],2)==[2.0,2.0]

def test_ema_fail_initial():
    assert Smoother().ema([10],0.5)[0]==10

def test_ema_fail_second_case():
    assert round(Smoother().ema([10,10],0.5)[0],1)==10.0

def test_sma_pass_basic():
    assert Smoother().sma([1,2,3],2)==[1.5]
