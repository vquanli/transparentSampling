# transparentSampling

![Python Version](https://img.shields.io/badge/python-%3E%3D3.8-blue)  
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

A Python toolkit for FRIDA: Data Availability Sampling from FRI,
based on the paper "FRIDA: FRI-based Data Availability Sampling" (2024).

## Table of Contents
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Compute FRIDA Scheme](#compute-frida-scheme)
  - [Generate LaTeX Tables](#generate-latex-tables)
  - [Generate CSV Data](#generate-csv-data)
  - [Generate Plots](#generate-plots)
  - [Bin–Ball Sampling](#bin–ball-sampling)
- [Data Files](#data-files)
- [Citation](#citation)
- [License](#license)

## Features
- Compute optimal FRIDA parameters (rounds, repetitions) for any data size.
- Multiple schemes: FRIDA, Merkle, Hash, Tensor, TDAS, LT, RS, etc.
- Export performance metrics to CSV.
- Generate LaTeX tables and publication-quality plots.
- Bin–Ball sampling simulation in `collectiveBallsInBins/`.

## Repository Structure
- `fri.py`                Core FRI/FRIDA parameter computation and scheme assembly.
- `schemes.py`            Underlying codes: Reed–Solomon, Hash, Pedersen, etc.
- `codes.py`              Low-level algebraic code definitions.
- `Listing4.py`           Generate summary table in terminal or LaTeX.
- `Listing5.py`–`Listing7.py` Export scheme metrics to CSV for different parameters.
- `plot_*.py`             Plot scripts for commitment size, query cost, total cost, encoding, samples.
- `collectiveBallsInBins/` Bin–Ball sampling scripts and precomputed plots (`*.py`, `figs/`).
- `csvdata/`              Collected CSV metrics for all schemes.
- `figs/`                 Generated figures (PDF/PNG).
- `table/`                LaTeX source (`table.latex`) for summary tables.
- `README.md`             This file.
- `LICENSE`               MIT License.

## Prerequisites
- Python ≥3.8
- pip

## Installation
```powershell
git clone https://github.com/your-org/transparentSampling.git
cd transparentSampling
python -m venv venv          # Optional virtual environment
.\venv\Scripts\Activate
pip install pandas numpy matplotlib tabulate
```

## Usage

### Compute FRIDA Scheme
```python
from fri import makeFRIScheme
scheme = makeFRIScheme(datasize=32*1024*1024, invrate=4, fsize=128, verbose=True)
print(scheme)
```

### Generate LaTeX Tables
```powershell
python Listing4.py <datasize_in_MB>         # Default table in text
python Listing4.py <datasize_in_MB> -l      # LaTeX table
# Output LaTeX saved under table/table.latex
```

### Generate CSV Data
```powershell
python Listing5.py   # Vary datasize
python Listing6.py   # Vary invrate (n/k ratio)
python Listing7.py   # Vary both invrate and k for sample metrics
```
CSV files are stored in `csvdata/`.

### Generate Plots
```powershell
python plot_com.py         # Commitment size
python plot_comm_pq.py     # Query cost
python plot_comm_total.py  # Total communication
python plot_encoding.py    # Encoding overhead
python plot_hash_sample.py # Sample count comparison
# Additional scripts with `_kn` suffix for fixed k/n
```
Figures saved in `figs/` or `collectiveBallsInBins/figs/`.

### Bin–Ball Sampling
Navigate to `collectiveBallsInBins/` and run:
```powershell
python plot_samples_to_prob.py   # Plot failure probability vs samples
python plot_to_prob_bin.py       # Bin–probability mapping
```
See `collectiveBallsInBins/figs/` for output.

## Data Files
CSV files in `csvdata/` are named `<scheme>_<metric>.csv`, e.g.:
- `fri_com.csv`           Commitment size vs. data dimension
- `hash_comm_pq.csv`      Per-query communication cost
- `rs_samples.csv`        Sample count for RS scheme

## Citation
If you use this work, please cite:
> J. Doe et al., "FRIDA: FRI-based Data Availability Sampling", XYZ 2024.

## License
MIT License – see [LICENSE](LICENSE).