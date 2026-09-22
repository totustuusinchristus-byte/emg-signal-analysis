"""Simple EMG preprocessing helpers for a teaching portfolio project."""
import numpy as np
from scipy.signal import butter, sosfiltfilt, iirnotch, filtfilt

def remove_dc(x):
    x = np.asarray(x, dtype=float)
    return x - np.mean(x)

def bandpass_emg(x, fs, low=20.0, high=350.0, order=4):
    sos = butter(order, [low, high], btype="bandpass", fs=fs, output="sos")
    return sosfiltfilt(sos, x)

def notch_mains(x, fs, freq=50.0, q=30.0):
    b, a = iirnotch(freq, q, fs=fs)
    return filtfilt(b, a, x)

def moving_rms(x, fs, window_ms=100):
    x = np.asarray(x, dtype=float)
    n = max(1, int(round(window_ms * fs / 1000)))
    kernel = np.ones(n) / n
    return np.sqrt(np.convolve(x**2, kernel, mode="same"))
