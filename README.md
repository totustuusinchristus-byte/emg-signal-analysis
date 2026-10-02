# EMG Signal Analysis in Python

A reproducible learning project for physiological signal processing using synthetic EMG-like data.

## Scientific question
How do common preprocessing choices transform a noisy surface-EMG-like signal, and which time- and frequency-domain features can be extracted reproducibly?

## Workflow
Raw signal → DC removal → 20–350 Hz Butterworth band-pass → 50 Hz notch → rectification → 100 ms RMS envelope → Welch power spectral density → feature extraction.

## Reproduce
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python generate_synthetic_data.py
python analysis.py
pytest -q
```

The analysis writes generated data/results to `data/` and figures to `figures/`.

## Repository structure
- `analysis.py` — end-to-end analysis.
- `generate_synthetic_data.py` — deterministic synthetic dataset generator.
- `src/preprocessing.py` — filtering and RMS utilities.
- `src/features.py` — time/frequency features.
- `tests/` — basic automated checks.
- `LEARNING_GUIDE.md` — concepts and exercises.
- `.github/workflows/` — automated Python checks.

## Skills demonstrated
Python, NumPy, pandas, SciPy, Matplotlib, physiological signal preprocessing, Welch PSD, feature extraction, reproducibility and basic testing.

## Interpretation and limitations
The parameters are teaching choices, not universal EMG settings. Appropriate filters depend on acquisition hardware, electrode placement, task, sampling and the scientific question. This project uses synthetic data and does **not** represent human-subject EMG acquisition, high-density EMG, or motor-unit decomposition experience.

## Development goals
Complete parameter-sensitivity exercises, document interpretation in my own words, and extend the workflow to an appropriately licensed open physiological dataset.
