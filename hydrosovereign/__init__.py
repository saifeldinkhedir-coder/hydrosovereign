"""
HydroSovereign AI Engine (HSAE) v6.5.0
========================================
Author:  Seifeldin M.G. Alkedir · ORCID: 0000-0003-0821-2991
DOI:     10.5281/zenodo.19180160
"""

__version__   = "6.5.1"
__author__    = "Seifeldin M.G. Alkedir"
__email__     = "saifeldinkhedir@gmail.com"
__orcid__     = "0000-0003-0821-2991"
__doi__       = "10.5281/zenodo.19180160"
__license__   = "GPL-3.0"
__app_url__   = "https://hydrosovereign-ai-engine-hsae-v601-6euz2zxcmerkzxgordmvxf.streamlit.app"

# Core API — always available
from .api import analyze_basin, analyze_all_basins

# Models — always available (pure Python + numpy)
from .models import HBVModel

# Indices — always available
from .indices import compute_atdi, compute_kge, compute_nse

# Optional imports — only if dependencies installed
try:
    from .data import fetch_basin_forcing, fetch_openmeteo
except ImportError:
    pass

try:
    from .viz import plot_water_balance, plot_forcing
except ImportError:
    pass

__all__ = [
    "__version__", "__author__", "__orcid__", "__doi__",
    "analyze_basin", "analyze_all_basins",
    "HBVModel",
    "compute_atdi", "compute_kge", "compute_nse",
]
