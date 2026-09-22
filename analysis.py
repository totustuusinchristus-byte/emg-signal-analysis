"""Run the complete starter EMG analysis and save figures/metrics."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import welch
from src.preprocessing import remove_dc, bandpass_emg, notch_mains, moving_rms
from src.features import time_domain_features, spectral_features

FS = 1000
Path("figures").mkdir(exist_ok=True)
if not Path("data/synthetic_emg.csv").exists():
    exec(Path("generate_synthetic_data.py").read_text())

df = pd.read_csv("data/synthetic_emg.csv")
t = df.time_s.to_numpy()
raw = df.emg_mV.to_numpy()
centered = remove_dc(raw)
filtered = notch_mains(bandpass_emg(centered, FS), FS)
rms = moving_rms(filtered, FS, 100)

features = {**time_domain_features(filtered), **spectral_features(filtered, FS)}
pd.Series(features, name="value").to_csv("data/emg_features.csv")

plt.figure(figsize=(10,4)); plt.plot(t, raw, lw=.5, label="Raw")
plt.plot(t, filtered, lw=.6, label="Filtered"); plt.xlabel("Time (s)")
plt.ylabel("Amplitude (mV)"); plt.legend(); plt.tight_layout()
plt.savefig("figures/raw_vs_filtered.png", dpi=160); plt.close()

f0,p0 = welch(centered, fs=FS, nperseg=2048)
f1,p1 = welch(filtered, fs=FS, nperseg=2048)
plt.figure(figsize=(8,4)); plt.semilogy(f0,p0,label="Raw/centered")
plt.semilogy(f1,p1,label="Filtered"); plt.xlim(0,450)
plt.xlabel("Frequency (Hz)"); plt.ylabel("PSD"); plt.legend(); plt.tight_layout()
plt.savefig("figures/power_spectral_density.png", dpi=160); plt.close()

plt.figure(figsize=(10,4)); plt.plot(t,np.abs(filtered),lw=.35,alpha=.5,label="Rectified")
plt.plot(t,rms,lw=1.2,label="100 ms RMS"); plt.xlabel("Time (s)")
plt.ylabel("Amplitude (mV)"); plt.legend(); plt.tight_layout()
plt.savefig("figures/rms_envelope.png", dpi=160); plt.close()
print(pd.Series(features))
