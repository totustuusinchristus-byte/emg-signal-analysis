# EMG Signal Analysis in Python

A learning-oriented physiological signal-processing project using synthetic EMG-like data.

## Aim
Build a transparent Python workflow for signal inspection, DC-offset removal, band-pass and 50 Hz notch filtering, power spectral density, rectification, RMS-envelope calculation, activation detection, and basic feature extraction.

## Scope
This project uses synthetic data for learning. It does not represent human-subject research, motor-unit decomposition, or high-density EMG expertise.

## Processing workflow
Raw signal → inspection → DC removal → band-pass filtering → 50 Hz notch filtering → rectification → RMS envelope → feature extraction.

## Tools
Python, NumPy, pandas, SciPy, Matplotlib and Jupyter.

## Processing choices
The starter analysis uses a 20–350 Hz Butterworth band-pass, a 50 Hz notch and a 100 ms moving RMS window. These are teaching choices rather than universal EMG settings; appropriate parameters depend on acquisition hardware, sampling rate, electrode configuration, movement task, noise and the research question.

## Learning goals
- understand sampling frequency and Nyquist frequency;
- explain why filtering can both preserve and remove information;
- understand rectification and RMS envelopes;
- compare time- and frequency-domain features;
- distinguish signal-processing foundations from motor-unit decomposition.

## Next development
Complete the notebook exercises, document parameter sensitivity, and later test the workflow on a properly licensed open EMG dataset.

## Research integrity
This repository documents developing computational skills. Synthetic data and guided code are clearly distinguished from experimental research experience.