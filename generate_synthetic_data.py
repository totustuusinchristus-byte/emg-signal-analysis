"""Generate reproducible synthetic EMG-like data for the portfolio project."""
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.signal import butter, sosfiltfilt

FS = 1000
DURATION = 20
rng = np.random.default_rng(20260922)
t = np.arange(0, DURATION, 1 / FS)

activation = np.full_like(t, 0.08)
for start, stop, amp in [(2,5,0.55),(7,10,0.85),(12,15,0.65),(17,19,0.95)]:
    activation[(t >= start) & (t < stop)] = amp

sos = butter(4, [20, 350], btype="bandpass", fs=FS, output="sos")
carrier = sosfiltfilt(sos, rng.normal(size=t.size))
carrier /= np.std(carrier)
raw = (activation * 0.22 * carrier
       + 0.025*np.sin(2*np.pi*50*t)
       + 0.035*np.sin(2*np.pi*0.7*t)
       + rng.normal(0, 0.012, t.size) + 0.015)

Path("data").mkdir(exist_ok=True)
pd.DataFrame({"time_s":t,"emg_mV":raw,"known_activation":activation}).to_csv(
    "data/synthetic_emg.csv", index=False)
print("Created data/synthetic_emg.csv")
