import numpy as np
from src.preprocessing import remove_dc, moving_rms
from src.features import time_domain_features

def test_remove_dc_centres_signal():
    x=np.array([1.,2.,3.,4.])
    assert abs(remove_dc(x).mean()) < 1e-12

def test_moving_rms_nonnegative_and_same_length():
    x=np.sin(np.linspace(0,10,1000))
    y=moving_rms(x,fs=1000,window_ms=100)
    assert len(y)==len(x)
    assert np.all(y>=0)

def test_time_features_are_finite():
    out=time_domain_features(np.array([0.,1.,-1.,2.,-2.]))
    assert all(np.isfinite(v) for v in out.values())
