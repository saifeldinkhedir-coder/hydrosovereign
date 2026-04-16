# HydroSovereign AI Engine (HSAE)

[![PyPI version](https://badge.fury.io/py/hydrosovereign.svg)](https://pypi.org/project/hydrosovereign/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19180160.svg)](https://doi.org/10.5281/zenodo.19180160)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

**Author:** Seifeldin M.G. Alkedir · ORCID: [0000-0003-0821-2991](https://orcid.org/0000-0003-0821-2991)  
**Affiliation:** University of Khartoum  
**DOI:** [10.5281/zenodo.19180160](https://doi.org/10.5281/zenodo.19180160)

---

## Overview

HydroSovereign AI Engine (HSAE) v6.5.0 is a Python package for:

- **Hydrological basin analysis** — water balance, inflow, outflow, storage
- **Real satellite data ingestion** — GPM IMERG, GRACE-FO, Sentinel-1/2, SMAP, GloFAS, ERA5
- **Water sovereignty assessment** — Alkedir Transparency Deficit Index (ATDI)
- **Forensic hydrology** — closure error, mass balance analysis
- **HBV rainfall-runoff modelling** — calibration and simulation
- **AI ensemble forecasting** — Random Forest, ensemble methods

## Installation

```bash
pip install hydrosovereign
```

With optional dependencies:
```bash
pip install hydrosovereign[gee]      # Google Earth Engine support
pip install hydrosovereign[viz]      # Plotly + Folium visualizations
pip install hydrosovereign[all]      # All dependencies
```

## Quick Start

```python
import hydrosovereign as hsae

# Analyze a basin
result = hsae.analyze_basin(
    basin_id   = "GERD_ETH",
    start_date = "2024-01-01",
    end_date   = "2024-12-31",
)

print(result["nse"])      # Nash-Sutcliffe Efficiency
print(result["atdi"])     # Alkedir Transparency Deficit Index
print(result["volume"])   # Reservoir volume (BCM)
```

```python
# Fetch real satellite data
from hydrosovereign.data import fetch_basin_forcing

forcing = fetch_basin_forcing("GERD_ETH", "2024-01-01", "2024-12-31")
print(forcing["gpm"]["mean_P"])    # GPM precipitation mm/day
print(forcing["grace"]["tws_cm"])  # GRACE-FO TWS anomaly
```

```python
# HBV rainfall-runoff model
from hydrosovereign.models import HBVModel

model = HBVModel()
model.fit(P=forcing["P"], T=forcing["T"], Q_obs=forcing["Q"])
print(f"NSE = {model.nse:.3f}")
```

## CLI

```bash
hydrosovereign analyze --basin GERD_ETH --year 2024
hydrosovereign fetch-gee --basin KAINJI_NGA --start 2023-01-01 --end 2023-12-31
```

## Live Application

The full HSAE v6.01 Streamlit application:  
🌐 [https://hydrosovereign-ai-engine-hsae-v601-6euz2zxcmerkzxgordmvxf.streamlit.app](https://hydrosovereign-ai-engine-hsae-v601-6euz2zxcmerkzxgordmvxf.streamlit.app)

## Citation

```bibtex
@software{alkedir2026hsae,
  author    = {Alkedir, Seifeldin M.G.},
  title     = {HydroSovereign AI Engine (HSAE) v6.5.0},
  year      = {2026},
  doi       = {10.5281/zenodo.19180160},
  url       = {https://github.com/saifeldinkhedir-coder/hydrosovereign},
  orcid     = {0000-0003-0821-2991},
}
```

## License

GNU General Public License v3.0 — see [LICENSE](LICENSE)
