"""Feature extraction helpers."""
import numpy as np
from scipy.signal import welch

def time_domain_features(x):
    x = np.asarray(x, dtype=float)
    return {
        "rms": float(np.sqrt(np.mean(x**2))),
        "mean_absolute_value": float(np.mean(np.abs(x))),
        "waveform_length": float(np.sum(np.abs(np.diff(x)))),
    }

def spectral_features(x, fs):
    f, pxx = welch(x, fs=fs, nperseg=min(2048, len(x)))
    total = np.sum(pxx)
    mean_f = float(np.sum(f * pxx) / total)
    cumulative = np.cumsum(pxx)
    median_f = float(f[np.searchsorted(cumulative, cumulative[-1] / 2)])
    return {"mean_frequency_hz": mean_f, "median_frequency_hz": median_f}
