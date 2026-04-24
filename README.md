# HydroSovereign AI Engine (HSAE) — Python Package

<div align="center">

[![QGIS Plugin](https://img.shields.io/badge/QGIS_Plugin-ID_5040-589632?style=for-the-badge&logo=qgis&logoColor=white)](https://plugins.qgis.org/plugins/hsae_qgis/)
[![PyPI](https://img.shields.io/badge/PyPI-hydrosovereign_v6.5.3-3775A9?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/hydrosovereign/)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19180160-1682D4?style=for-the-badge&logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.19180160)
[![SoftwareX](https://img.shields.io/badge/SoftwareX-SOFTX--D--26--00442-005A8E?style=for-the-badge)](https://doi.org/10.5281/zenodo.19180160)
[![License](https://img.shields.io/badge/License-GPL_3.0-blue?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0003--0821--2991-a6ce39?style=for-the-badge&logo=orcid&logoColor=white)](https://orcid.org/0000-0003-0821-2991)

**Author:** Seifeldin M.G. Alkedir · [ORCID 0000-0003-0821-2991](https://orcid.org/0000-0003-0821-2991) · University of Khartoum

</div>

---

## 🔗 Quick Links

| Resource | Link |
|----------|------|
| 🔌 **QGIS Plugin** | [plugins.qgis.org/plugins/hsae_qgis/](https://plugins.qgis.org/plugins/hsae_qgis/) — Plugin ID: **5040** |
| 🐍 **PyPI Package** | [pypi.org/project/hydrosovereign/](https://pypi.org/project/hydrosovereign/) |
| 🌐 **Live Streamlit App** | [HSAE v6.01](https://hydrosovereign-ai-engine-hsae-v601-6euz2zxcmerkzxgordmvxf.streamlit.app) |
| 📦 **GitHub (Main App)** | [HydroSovereign-AI-Engine-HSAE-v601](https://github.com/saifeldinkhedir-coder/HydroSovereign-AI-Engine-HSAE-v601) |
| 🏛️ **Zenodo DOI** | [10.5281/zenodo.19180160](https://doi.org/10.5281/zenodo.19180160) |
| 📄 **SoftwareX Paper** | SOFTX-D-26-00442 — Under Review 2026 |
| 📖 **Manual PDF** | [⬇️ Download Complete Guide](https://github.com/saifeldinkhedir-coder/HydroSovereign-AI-Engine-HSAE-v601/raw/main/hsae_qgis/HSAE_v601_QGIS_Plugin_Manual_v6.docx) |
| 🐛 **Issues** | [GitHub Issues](https://github.com/saifeldinkhedir-coder/HydroSovereign-AI-Engine-HSAE-v601/issues) |

---

## What is HSAE?

**HydroSovereign AI Engine (HSAE)** is a Python package for transboundary river basin analysis, combining satellite remote sensing, physics-based hydrological modelling, geopolitical water law, and AI-powered negotiation assessment.

Two novel scientific indices:

| Index | Full Name | Range | Blue Nile Result |
|-------|-----------|-------|------------------|
| **ATDI** | Alkedir Transparency Deficit Index | 0–100% | **43.5%** — Art. 7 UNWC zone |
| **HIFD** | Human-Induced Flow Deficit | 0–100% | **20.0%** — 20% withheld |

---

## ⚙️ Installation

```bash
pip install hydrosovereign            # base
pip install hydrosovereign[viz]       # + Plotly & Folium
pip install hydrosovereign[gee]       # + Google Earth Engine
pip install hydrosovereign[all]       # everything
```

**Requirements:** Python ≥ 3.9, NumPy, Pandas, SciPy, Requests

---

## Quick Start

```python
from hydrosovereign import ATDI, HIFD, ConflictIndex, NegotiationAI

# Blue Nile (GERD)
params = dict(runoff_coeff=0.38, dam_capacity_bcm=74.0,
              n_countries=3, dispute_level=4, basin_area_km2=174000)

atdi = ATDI(**params)   # → 43.5%
hifd = HIFD(**params)   # → 20.0%
ci   = ConflictIndex(atdi=atdi, hifd=hifd, **params)  # → 0.44 HIGH

ai = NegotiationAI()
p  = ai.predict(atdi=atdi, ci=ci, n_countries=3, dispute_level=4)
print(f"P(Negotiation) = {p:.0%}")  # → 58% → Art.17 Mediation
```

---

## Architecture

```
hydrosovereign/
├── api.py          ← analyze_basin() entry point
├── indices.py      ← ATDI, HIFD, NSE, KGE, CI
├── hbv.py          ← HBV-96 + SCE-UA calibration
├── basins.py       ← 26-basin registry (7 world regions)
├── legal.py        ← UNWC 1997 article assessment (33 articles)
├── alerts.py       ← Alert level classification
├── data/fetchers.py ← Open-Meteo, GRDC, NASA POWER
├── viz/            ← Plotly charts + Folium maps
├── models/hbv.py   ← HBV-96 model class
└── ai/negotiation.py ← NegotiationAI (478 TFDD/ICJ cases)
```

---

## 📊 Key Results (Blue Nile / GERD)

| Metric | Value | Class |
|--------|-------|-------|
| NSE | 0.63 | Satisfactory |
| KGE | 0.74 | Satisfactory |
| ATDI | 43.5% | Art. 7 UNWC |
| HIFD | 20.0% | Moderate |
| CI | 0.44 | HIGH |
| P(Negotiation) | 58% | Mediation |

> **Note:** NSE and KGE are proxy-validated against GloFAS ERA5 v4 reanalysis — no open GRDC gauge data is available for the Blue Nile at basin scale for 2024.

---

## 📝 Citation

```bibtex
@software{alkedir2026hsae,
  author    = {Alkedir, Seifeldin M.G.},
  title     = {{HydroSovereign AI Engine (HSAE) v6.01}},
  year      = {2026},
  publisher = {QGIS Plugin Repository + PyPI + Zenodo},
  version   = {6.0.1},
  note      = {QGIS Plugin ID: 5040. SoftwareX SOFTX-D-26-00442.},
  url       = {https://plugins.qgis.org/plugins/hsae_qgis/},
  doi       = {10.5281/zenodo.19180160},
  orcid     = {0000-0003-0821-2991}
}
```

---

*hydrosovereign v6.5.3 · GPL-3.0 · Seifeldin M.G. Alkedir · ORCID: 0000-0003-0821-2991*
