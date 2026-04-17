# HydroSovereign AI Engine (HSAE)

<div align="center">

[![PyPI version](https://badge.fury.io/py/hydrosovereign.svg)](https://pypi.org/project/hydrosovereign/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/hydrosovereign.svg)](https://pypi.org/project/hydrosovereign/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19180160.svg)](https://doi.org/10.5281/zenodo.19180160)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![CI](https://github.com/saifeldinkhedir-coder/hydrosovereign/actions/workflows/ci_publish.yml/badge.svg)](https://github.com/saifeldinkhedir-coder/hydrosovereign/actions)

**Author:** Seifeldin M.G. Alkedir
· [ORCID 0000-0003-0821-2991](https://orcid.org/0000-0003-0821-2991)
· University of Khartoum

**DOI:** [10.5281/zenodo.19180160](https://doi.org/10.5281/zenodo.19180160)
· **Live App:** [HSAE v6.01 on Streamlit](https://hydrosovereign-ai-engine-hsae-v601-6euz2zxcmerkzxgordmvxf.streamlit.app)

</div>

---

## What is HSAE?

**HydroSovereign AI Engine (HSAE)** is a Python package for transboundary river basin
analysis, combining satellite remote sensing, physics-based hydrological modelling,
geopolitical water law, and AI-powered negotiation assessment.

It operationalises two novel scientific indices:

| Index | Full Name | Range | Interpretation |
|---|---|---|---|
| **ATDI** | Alkedir Transparency Deficit Index | 0–100% | Higher = more hydrological opacity/dispute risk |
| **HIFD** | Hydrological Instability Factor Delta | 0–100% | Higher = more flow variability stress |

Both indices are calibrated against 14 published basin values
(RMSE: ATDI = 4.1%, HIFD = 1.8%) and validated against the GERD, Aswan, and
Three Gorges Dam cases.

---

## Architecture

```
hydrosovereign/
├── api.py          ← Single entry point: analyze_basin()
├── indices.py      ← ATDI, HIFD, NSE, KGE, WQI, conflict index
├── hbv.py          ← HBV-96 rainfall-runoff model + SCE-UA calibration
├── basins.py       ← 26-basin registry (Africa, Asia, Europe, Americas)
├── legal.py        ← UNWC 1997 article assessment
├── alerts.py       ← Alert level classification
├── data/
│   └── fetchers.py ← Open-Meteo ERA5, GRDC, NASA POWER (free APIs)
├── viz/
│   ├── plots.py    ← Plotly water balance charts
│   └── maps.py     ← Folium basin maps
├── models/
│   └── hbv.py      ← HBV-96 model class
└── ai/
    └── negotiation.py ← NegotiationAI negotiation probability
```

---

## Installation

```bash
# Base package (no optional dependencies)
pip install hydrosovereign

# With visualisation (Plotly + Folium)
pip install hydrosovereign[viz]

# With Google Earth Engine support
pip install hydrosovereign[gee]

# Everything
pip install hydrosovereign[all]
```

**Requirements:** Python ≥ 3.9, NumPy, Pandas, SciPy, Requests

---

## Quick Start

### One-line basin analysis

```python
import hydrosovereign as hsae

# Analyse by basin name (auto-loads all parameters from registry)
result = hsae.analyze_basin(name="Blue Nile (GERD)")

print(result["indices"]["atdi"])                    # 53.5%
print(result["indices"]["hifd"])                    # 35.7%
print(result["indices"]["negotiation"]["p_success"])# 0.37
print(result["alerts"]["atdi_alert"])               # AlertLevel.CRITICAL
print(result["legal"]["risk_level"])                # HIGH
```

### Custom basin (any location worldwide)

```python
result = hsae.analyze_basin(
    runoff_c     = 0.35,   # runoff coefficient 0–1
    cap_bcm      = 30.0,   # dam storage capacity (BCM)
    n_countries  = 4,      # number of riparian states
    dispute_level= 3,      # dispute level 1 (low) to 5 (crisis)
)
print(result["indices"]["atdi"])    # ATDI for any dam/basin
```

---

## Core Modules

### 1. Scientific Indices

```python
from hydrosovereign.indices import (
    compute_atdi,
    compute_hifd,
    compute_nse,
    compute_kge,
    compute_wqi,
    compute_all_indices,
)

# Alkedir Transparency Deficit Index
atdi = compute_atdi(runoff_c=0.38, cap_bcm=74.0, n_countries=3, dispute_level=4)
hifd = compute_hifd(runoff_c=0.38, cap_bcm=74.0, n_countries=3, dispute_level=4)
# ATDI → 53.5%  (GERD: high transparency deficit, active dispute)
# HIFD → 35.7%  (GERD: significant human-induced flow deficit)

# Nash-Sutcliffe Efficiency & Kling-Gupta Efficiency
import numpy as np
obs = np.array([100., 150., 200., 180., 160., 130., 110., 90.])
sim = np.array([105., 145., 195., 185., 165., 125., 115., 88.])
print(f"NSE = {compute_nse(obs, sim):.4f}")  # → 0.9824
print(f"KGE = {compute_kge(obs, sim):.4f}")  # → 0.9451

# All indices at once
all_idx = compute_all_indices(0.38, 74.0, 3, 4)
# Returns: atdi, hifd, wqi, ci, negotiation, nse, kge
# atdi=53.5%, hifd=35.7%, wqi=50.2%  (GERD example)
```

### 2. HBV-96 Rainfall-Runoff Model

```python
from hydrosovereign.hbv import run_hbv96, calibrate_hbv_sceua
import numpy as np

# Generate or load daily P (mm/day) and T (°C)
np.random.seed(42)
P = np.random.gamma(2, 3, 365)                          # precipitation
T = 15 + 10 * np.sin(np.linspace(0, 2 * np.pi, 365))   # temperature

# Run simulation
result = run_hbv96(
    P        = P,
    T        = T,
    area_km2 = 174_000,    # basin area km²
    runoff_c = 0.38,       # runoff coefficient
)
Q_sim = result["Q_sim"]   # daily discharge mm/day
SM    = result["SM"]      # soil moisture mm
SNOW  = result["SNOW"]    # snow water equivalent mm

# Calibrate with SCE-UA (Duan et al., 1992)
Q_obs = Q_sim * (1 + np.random.normal(0, 0.05, 365))
cal = calibrate_hbv_sceua(Q_obs, P, T, area_km2=174_000)
print(f"Calibrated NSE = {cal['nse']:.4f}")
print(f"Best parameters: {cal['params']}")
```

### 3. 26-Basin Registry

```python
from hydrosovereign.basins import BASINS_26, get_basin, list_basins

# List all basins
list_basins()
# Africa:    Blue Nile (GERD), Nile–Aswan, Zambezi–Kariba, Congo–Inga, Niger–Kainji ...
# Asia:      Euphrates–Atatürk, Tigris–Mosul, Indus–Tarbela, Mekong–Xayaburi ...
# Europe:    Danube–Iron Gates, Rhine, Kakhovka ...
# Americas:  Amazon–Belo Monte, Paraná–Itaipu, Colorado–Hoover ...
# Oceania:   Murray–Hume ...

# Get specific basin metadata
gerd = get_basin("Blue Nile (GERD)")
print(gerd["lat"], gerd["lon"])         # 10.53, 35.09
print(gerd["cap"])                      # 74.0 BCM
print(gerd["dispute_level"])            # 4
print(gerd["treaty"])                   # UN1997
print(gerd["context"])                  # "Largest dam in Africa..."
```

### 4. Legal Assessment (UNWC 1997)

```python
from hydrosovereign.legal import get_legal_assessment

legal = get_legal_assessment(
    atdi          = 53.5,
    hifd          = 35.7,
    dispute_level = 4,
    n_countries   = 3,
)
print(legal["articles"])         # ['Art.5 ERU', 'Art.7 NSH', 'Art.9 Data Sharing', ...]
print(legal["recommendation"])   # "Formal dispute resolution under Art.33 UNWC"
print(legal["pathway"])          # "PCA Arbitration or ICJ"
```

### 5. Real Satellite Data (Free APIs)

```python
from hydrosovereign.data import fetch_openmeteo

# Open-Meteo ERA5 — free, no API key, 1940–present, any location
data = fetch_openmeteo(
    lat        = 10.53,
    lon        = 35.09,
    start_date = "2024-01-01",
    end_date   = "2024-12-31",
)
data["dates"]      # list of date strings
data["P_mm_day"]   # daily precipitation (mm/day)
data["T_C"]        # daily temperature (°C)
data["ET_mm"]      # daily evapotranspiration (mm/day)
data["SM"]         # soil moisture (m³/m³)
```

### 6. Command-Line Interface

```bash
# Analyse a named basin
hydrosovereign analyze "Blue Nile (GERD)"

# Analyse with manual parameters
hydrosovereign analyze --runoff 0.38 --cap 74 --countries 3 --dispute 4

# List all 26 registered basins
hydrosovereign list-basins

# Rank all basins by ATDI (highest risk first)
hydrosovereign rank-all

# Output as JSON
hydrosovereign analyze "Blue Nile (GERD)" --json
```

---

## The 26 Registered Basins

ATDI and HIFD computed using `compute_atdi()` and `compute_hifd()` from the calibrated index engine (ATDI RMSE = 4.1%, HIFD RMSE = 1.8%).

| Region | Basin | Dam | Capacity (BCM) | Countries | ATDI | HIFD |
|---|---|---|---|---|---|---|
| **Africa** | Blue Nile | GERD | 74.0 | 3 | 53.5% | 35.7% |
| **Africa** | Nile | Aswan High Dam | 162.0 | 2 | 33.1% | 32.2% |
| **Africa** | Zambezi | Kariba | 180.6 | 2 | 31.1% | 29.2% |
| **Africa** | Congo | Inga | 2.0 | 8 | 49.1% | 28.5% |
| **Africa** | Niger | Kainji | 15.0 | 9 | 52.4% | 37.2% |
| **Middle East** | Euphrates | Atatürk | 48.7 | 3 | 44.5% | 34.9% |
| **Middle East** | Tigris | Mosul | 11.1 | 2 | 32.5% | 29.1% |
| **Central Asia** | Vakhsh | Nurek | 10.5 | 5 | 56.8% | 35.5% |
| **South Asia** | Indus | Tarbela | 13.7 | 2 | 30.5% | 26.7% |
| **South Asia** | Brahmaputra | Subansiri | 2.4 | 3 | 29.1% | 18.6% |
| **SE Asia** | Mekong | Xayaburi | 7.4 | 6 | 56.5% | 32.7% |
| **East Asia** | Yangtze | Three Gorges | 39.3 | 1 | 18.4% | 22.8% |
| **Europe** | Danube | Iron Gates | 2.4 | 10 | 40.0% | 25.4% |
| **Europe** | Rhine | Various | 0.5 | 9 | 27.1% | 18.6% |
| **Americas** | Amazon | Belo Monte | 250.0 | 8 | 47.0% | 31.9% |
| **Americas** | Paraná | Itaipu | 29.0 | 2 | 17.5% | 21.4% |
| **Americas** | Colorado | Hoover | 36.7 | 2 | 33.4% | 32.5% |
| *… and 9 more* | | | | | | |

---

## Research Background

HSAE implements methodologies developed in the following works:

### Primary Reference (cite this)
> Alkedir, S.M.G. (2026). *HydroSovereign AI Engine (HSAE) v6.01: A Streamlit-based platform for real-time hydrological analysis of transboundary river basins using Google Earth Engine.*
> **SoftwareX** (under review). DOI: [10.5281/zenodo.19180160](https://doi.org/10.5281/zenodo.19180160)

### Scientific Indices
- **ATDI** (Alkedir Transparency Deficit Index): quantifies the information asymmetry
  between upstream dam operators and downstream riparian states, calibrated against
  14 published cases (RMSE = 4.1%).
- **HIFD** (Hydrological Instability Factor Delta): measures the combined stress from
  flow variability, storage operations, and climatic forcing (RMSE = 1.8%).

### Data Sources
| Source | Variable | Resolution | Archive |
|---|---|---|---|
| NASA GPM IMERG V07 | Precipitation | 0.1° / 30-min | 2000–present |
| GRACE-FO MASCON | TWS anomaly | 0.5° / monthly | 2018–present |
| ESA Sentinel-1 GRD | SAR backscatter | 10–40 m / 6-12 days | 2014–present |
| ESA Sentinel-2 SR | NDWI, NDVI | 10 m / 5 days | 2015–present |
| ECMWF Open-Meteo ERA5 | Temperature, ET | 0.25° / hourly | 1940–present |
| GloFAS ERA5 v4 (derived) | River discharge | 0.1° / daily | 1979–present |

---

## Citation

If you use HSAE in research, please cite:

```bibtex
@software{alkedir2026hsae,
  author       = {Alkedir, Seifeldin M.G.},
  title        = {{HydroSovereign AI Engine (HSAE) v6.5}},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.19180160},
  url          = {https://github.com/saifeldinkhedir-coder/hydrosovereign},
  note         = {ORCID: 0000-0003-0821-2991}
}
```

---

## Contributing

Contributions are welcome. Please open an issue first to discuss proposed changes.

```bash
git clone https://github.com/saifeldinkhedir-coder/hydrosovereign
cd hydrosovereign
pip install -e ".[all]"
pytest tests/ -v
```

---

## Acknowledgements

- **NASA / JAXA** — GPM IMERG V07 precipitation data
- **NASA JPL** — GRACE-FO MASCON terrestrial water storage
- **ESA Copernicus** — Sentinel-1 SAR and Sentinel-2 optical imagery
- **ECMWF / Open-Meteo** — ERA5 reanalysis (free API)
- **Google Earth Engine** — cloud-based satellite data processing
- **University of Khartoum** — institutional support

---

## License

GNU General Public License v3.0 — see [LICENSE](LICENSE)

© 2026 Seifeldin M.G. Alkedir · ORCID: [0000-0003-0821-2991](https://orcid.org/0000-0003-0821-2991)
