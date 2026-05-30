# HydroSovereign AI Engine (HSAE) — Python Package

<div align="center">

[![QGIS Plugin](https://img.shields.io/badge/QGIS_Plugin-ID_5040-589632?style=for-the-badge&logo=qgis&logoColor=white)](https://plugins.qgis.org/plugins/hsae_qgis/)
[![PyPI](https://img.shields.io/badge/PyPI-hydrosovereign_v6.5.4-3775A9?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/hydrosovereign/)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19180160-1682D4?style=for-the-badge&logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.19180160)
[![SoftwareX](https://img.shields.io/badge/SoftwareX-Under_Review_2026-005A8E?style=for-the-badge)](https://www.sciencedirect.com/journal/softwarex)
[![Preprint](https://img.shields.io/badge/Preprint-SSRN_6661396-B31B1B?style=for-the-badge)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6661396)
[![License](https://img.shields.io/badge/License-GPL_3.0-blue?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0003--0821--2991-a6ce39?style=for-the-badge&logo=orcid&logoColor=white)](https://orcid.org/0000-0003-0821-2991)

**Author:** Seifeldin M.G. Alkhedir · [ORCID 0000-0003-0821-2991](https://orcid.org/0000-0003-0821-2991) · University of Khartoum

</div>

---

## 🔗 Quick Links

| Resource | Link |
|----------|------|
| 🔌 **QGIS Plugin** | [plugins.qgis.org/plugins/hsae_qgis/](https://plugins.qgis.org/plugins/hsae_qgis/) — Plugin ID: **5040** |
| 🐍 **PyPI Package** | [pypi.org/project/hydrosovereign/](https://pypi.org/project/hydrosovereign/) |
| 🌐 **Live Streamlit App** | [HSAE v6.0.8](https://hydrosovereign-ai-engine-hsae-v601-6euz2zxcmerkzxgordmvxf.streamlit.app) |
| 📦 **GitHub (Main Repo)** | [HydroSovereign-AI-Engine-HSAE-v601](https://github.com/saifeldinkhedir-coder/HydroSovereign-AI-Engine-HSAE-v601) |
| 🏛️ **Zenodo Archive** | [doi.org/10.5281/zenodo.19180160](https://doi.org/10.5281/zenodo.19180160) |
| 📄 **Preprint (SSRN)** | [papers.ssrn.com/abstract=6661396](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6661396) |
| 📰 **SoftwareX Paper** | SOFTX-D-26-00442 — Under Review · [Elsevier SoftwareX](https://www.sciencedirect.com/journal/softwarex) |
| 📖 **Manual (v6)** | [Download Complete Guide](https://github.com/saifeldinkhedir-coder/HydroSovereign-AI-Engine-HSAE-v601/raw/main/hsae_qgis/HSAE_v601_QGIS_Plugin_Manual_v6.docx) |
| 🤖 **GeoAgent** | [opengeos/GeoAgent PR #79](https://github.com/opengeos/GeoAgent/pull/79) — merged May 2026 |

---

## What is HSAE?

**HydroSovereign AI Engine (HSAE)** automates the full pipeline from live satellite observation to international water law compliance assessment — in under two minutes per basin. It covers **26 globally contested transboundary basins** using 9 satellite sensors, an HBV-96 hydrological model, and six original scientific indices collectively known as the **Alkhedir Water Sovereignty Indices (AWSI)**.

> 362+ downloads · 20 countries · 5 continents · 100% QGIS security scan · GeoAgent AI integration

---

## 🔬 Six Original Scientific Indices (AWSI)

| Index | Full Name | Legal Trigger |
|-------|-----------|---------------|
| **ATDI** | Alkhedir Transparency Deficit Index | Art. 7 UNWC — No Significant Harm (≥ 40%) |
| **AHIFD** | Alkhedir Human-Induced Flow Deficit | Art. 7 — volumetric downstream harm |
| **AFSF** | Alkhedir Forensic Signal Factor | Art. 9 — data exchange obligation |
| **AHLB** | Alkhedir HBV-Legal Bridge | Arts. 5, 6, 7 — HBV-96 → legal triggers |
| **ASI** | Alkhedir Sovereignty Index | Art. 5 — equitable utilisation |
| **ATCI** | Alkhedir Treaty Compliance Index | Arts. 5, 7, 9, 11, 17, 33 composite |

All six indices are validated against the Blue Nile (GERD) basin and benchmarked against 14 published values.

---

## ⚙️ Installation

```bash
pip install hydrosovereign             # base
pip install hydrosovereign[gee]        # + Google Earth Engine
pip install hydrosovereign[full]       # + Streamlit, Plotly, Folium, GEE
```

**Requirements:** Python ≥ 3.9, NumPy, Pandas, SciPy, scikit-learn, Requests

---

## Quick Start

```python
from hydrosovereign import ATDI, AHIFD, AFSF, AHLB, ASI, ATCI
from hydrosovereign import ConflictIndex, NegotiationAI

# Any basin — example: Blue Nile (GERD)
params = dict(
    runoff_coeff=0.38, dam_capacity_bcm=74.0,
    n_countries=3, dispute_level=4, basin_area_km2=174000
)

atdi  = ATDI(**params)    # → 43.5%  (Art. 7 UNWC triggered)
ahifd = AHIFD(**params)   # → 20.0%  (20% natural flow withheld)
ahlb  = AHLB(**params)    # → HBV-96 → legal bridge
asi   = ASI(**params)     # → equitable utilisation score
atci  = ATCI(**params)    # → 70     (composite compliance)
ci    = ConflictIndex(atdi=atdi, ahifd=ahifd, **params)  # → 0.44 HIGH

ai = NegotiationAI()
p  = ai.predict(atdi=atdi, ci=ci, n_countries=3, dispute_level=4)
print(f"P(Negotiation) = {p:.0%}")    # → 58% → Art.17 Mediation
```

---

## Architecture

```
hydrosovereign/
├── api.py            ← analyze_basin() entry point
├── indices.py        ← ATDI, AHIFD, AFSF, AHLB, ASI, ATCI
├── hbv.py            ← HBV-96 + SCE-UA calibration
├── basins.py         ← 26-basin registry (7 world regions)
├── legal.py          ← UNWC 1997 article assessment
├── alerts.py         ← Alert level classification
├── data/fetchers.py  ← Open-Meteo, GRDC, NASA POWER, GloFAS
├── viz/              ← Plotly charts + Folium maps
├── models/hbv.py     ← HBV-96 model class
└── ai/negotiation.py ← NegotiationAI (478 TFDD/ICOW cases)
```

---

## 📊 Key Results — 26 Globally Contested Basins

Sample results across five continents (full dataset: 26 basins):

| Basin | Region | ATDI | AHIFD | CI | ATCI | Risk |
|-------|--------|------|-------|----|------|------|
| Blue Nile (GERD) | Africa | 43.5% | 20.0% | 0.44 | 70 | HIGH |
| Euphrates – Atatürk | Middle East | 58.2% | 31.4% | 0.61 | 45 | CRITICAL |
| Mekong – Xayaburi | Asia | 51.8% | 27.6% | 0.53 | 52 | HIGH |
| Amu Darya – Nurek | Central Asia | 49.3% | 25.1% | 0.49 | 58 | HIGH |
| Danube – Iron Gates | Europe | 38.7% | 18.9% | 0.39 | 75 | MEDIUM |
| Colorado – Hoover | Americas | 44.1% | 22.3% | 0.45 | 68 | HIGH |

> NSE = 0.63 · KGE = 0.74 (pre-calibration vs GloFAS ERA5 v4) · 56 pytest tests passing

---

## 📝 Citation

```bibtex
@software{alkhedir2026hsae,
  author    = {Alkhedir, Seifeldin M.G.},
  title     = {{HydroSovereign AI Engine (HSAE) v6.5.4}},
  year      = {2026},
  publisher = {PyPI + QGIS Plugin Repository + Zenodo},
  version   = {6.5.4},
  note      = {QGIS Plugin ID: 5040. SoftwareX under review: SOFTX-D-26-00442.
               Preprint: SSRN 6661396.},
  url       = {https://pypi.org/project/hydrosovereign/},
  doi       = {10.5281/zenodo.19180160},
  orcid     = {0000-0003-0821-2991}
}
```

---

*hydrosovereign v6.5.4 · GPL-3.0 · Seifeldin M.G. Alkhedir · ORCID: 0000-0003-0821-2991*
