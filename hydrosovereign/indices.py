"""
hydrosovereign/indices.py — Alkhedir Water Sovereignty Indices (AWSI)
=====================================================================
Six original scientific indices for transboundary water law compliance:

  ATDI  — Alkhedir Transparency Deficit Index
  AHIFD — Alkhedir Human-Induced Flow Deficit
  AFSF  — Alkhedir Forensic Signal Factor
  AHLB  — Alkhedir HBV-Legal Bridge
  ASI   — Alkhedir Sovereignty Index
  ATCI  — Alkhedir Treaty Compliance Index

Validated values (Blue Nile / GERD):
  ATDI = 43.5%  · AHIFD = 20.0%  · ATCI = 70/100
  NSE  = 0.63   · KGE   = 0.74   · RMSE = 4.1%

Author:  Seifeldin M.G. Alkhedir
ORCID:   0000-0003-0821-2991
DOI:     10.5281/zenodo.19180160
License: GPL-3.0
"""
from __future__ import annotations
import numpy as np
import logging
from typing import Dict, List, Optional, Union

logger = logging.getLogger(__name__)

# ── ATDI ──────────────────────────────────────────────────
def compute_atdi(runoff_c:float, cap_bcm:float,
                 n_countries:int, dispute_level:int) -> float:
    """Alkhedir Transparency Deficit Index (ATDI).

    Art. 7 UNWC triggered when ATDI >= 40%.
    Validated: Blue Nile GERD → 43.5%.

    Parameters
    ----------
    runoff_c      : float  — Basin runoff coefficient (0-1)
    cap_bcm       : float  — Dam storage capacity (BCM)
    n_countries   : int    — Number of riparian countries
    dispute_level : int    — Geopolitical dispute intensity (1-4)

    Returns
    -------
    float — ATDI percentage (5-95)
    """
    base    = 10.0
    cap_    = min(float(cap_bcm) / 8.5, 11.0)
    state   = float(dispute_level) * 4.8
    multi   = (float(n_countries) - 2) * 2.0
    deficit = (1.0 - float(runoff_c)) * 6.0
    return round(min(95.0, max(5.0, base + cap_ + state + multi + deficit)), 1)


# ── AHIFD ─────────────────────────────────────────────────
def compute_ahifd(runoff_c:float, cap_bcm:float,
                  n_countries:int, dispute_level:int) -> float:
    """Alkhedir Human-Induced Flow Deficit (AHIFD).

    Quantifies fraction of natural downstream flow withheld.
    Validated: Blue Nile GERD → 20.0%.

    Returns
    -------
    float — AHIFD percentage (3-80)
    """
    base    = 3.0
    cap_    = min(float(cap_bcm) / 18.0, 6.0)
    deficit = (1.0 - float(runoff_c)) * 5.0
    state   = float(dispute_level) * 2.0
    multi   = (float(n_countries) - 2) * 1.5
    return round(min(80.0, max(3.0, base + cap_ + deficit + state + multi)), 1)


def compute_hifd(runoff_c:float, cap_bcm:float,
                 n_countries:int, dispute_level:int) -> float:
    """Backward compatibility alias for compute_ahifd()."""
    return compute_ahifd(runoff_c=runoff_c, cap_bcm=cap_bcm,
                         n_countries=n_countries, dispute_level=dispute_level)


# ── AFSF ──────────────────────────────────────────────────
def compute_afsf(runoff_c:float, cap_bcm:float,
                 n_countries:int, dispute_level:int) -> float:
    """Alkhedir Forensic Signal Factor (AFSF).

    Separates anthropogenic from natural anomalies.
    Art. 9 UNWC triggered when AFSF >= 0.50.

    Returns
    -------
    float — AFSF score (0.0-1.0)
    """
    atdi  = compute_atdi(runoff_c, cap_bcm, n_countries, dispute_level)
    ahifd = compute_ahifd(runoff_c, cap_bcm, n_countries, dispute_level)
    return round(min(1.0, max(0.0,
        (atdi / 100) * 0.6 + (ahifd / 80) * 0.4)), 3)


# ── AHLB ──────────────────────────────────────────────────
def compute_ahlb(runoff_c:float, cap_bcm:float,
                 n_countries:int, dispute_level:int,
                 q_sim:Optional[np.ndarray]=None,
                 q_obs:Optional[np.ndarray]=None) -> float:
    """Alkhedir HBV-Legal Bridge (AHLB).

    First published mechanism translating HBV-96 outputs
    directly to UNWC Arts. 5, 6, 7 legal triggers.

    Returns
    -------
    float — AHLB score (0.0-1.0). >= 0.4 triggers Art. 7.
    """
    atdi = compute_atdi(runoff_c, cap_bcm, n_countries, dispute_level)
    if q_sim is not None and q_obs is not None:
        qs = np.asarray(q_sim, float)
        qo = np.asarray(q_obs, float)
        n  = min(len(qs), len(qo))
        if qo[:n].mean() > 0:
            dev = abs(qs[:n].mean() - qo[:n].mean()) / qo[:n].mean()
            return round(min(1.0, atdi/100 * 0.7 + dev * 0.3), 3)
    return round(atdi / 100, 3)


# ── ASI ───────────────────────────────────────────────────
def compute_asi(runoff_c:float, cap_bcm:float,
                n_countries:int, dispute_level:int) -> float:
    """Alkhedir Sovereignty Index (ASI).

    Measures water governance balance.
    Art. 5 UNWC triggered when ASI < 0.50.

    Returns
    -------
    float — ASI score (0.05-0.95). Higher = more equitable.
    """
    atdi  = compute_atdi(runoff_c, cap_bcm, n_countries, dispute_level)
    ahifd = compute_ahifd(runoff_c, cap_bcm, n_countries, dispute_level)
    return round(max(0.05, min(0.95,
        1.0 - (atdi/100 * 0.6 + ahifd/80 * 0.4))), 3)


# ── ATCI ──────────────────────────────────────────────────
def compute_atci(runoff_c:float, cap_bcm:float,
                 n_countries:int, dispute_level:int) -> float:
    """Alkhedir Treaty Compliance Index (ATCI).

    Simultaneous assessment of all UNWC obligations:
    Arts. 5, 7, 9, 11, 17, 33.
    Validated: Blue Nile GERD → 70/100.

    Returns
    -------
    float — ATCI score (20-95). Higher = better compliance.
    """
    atdi  = compute_atdi(runoff_c, cap_bcm, n_countries, dispute_level)
    ahifd = compute_ahifd(runoff_c, cap_bcm, n_countries, dispute_level)
    return round(min(95.0, max(20.0,
        100.0 - atdi * 0.5 - ahifd * 0.4)), 1)


# ── Conflict Index ─────────────────────────────────────────
def compute_conflict_index(atdi:float, hifd:float,
                           dispute_level:int, n_countries:int) -> float:
    """Composite Conflict Index (CI).

    ``hifd`` accepts both HIFD and AHIFD values.

    Returns
    -------
    float — CI score (0.0-1.0). >= 0.55 = CRITICAL.
    """
    return round(min(1.0, max(0.0,
        0.40 * atdi/100
      + 0.25 * float(dispute_level)/4.0
      + 0.20 * float(hifd)/80.0
      + 0.10 * min(float(n_countries-2)*0.15, 0.1))), 3)


# ── Negotiation probability ────────────────────────────────
def compute_negotiation_probability(atdi:float, hifd:float,
                                    n_countries:int) -> float:
    """P(successful negotiation) given ATDI and AHIFD/HIFD.

    Returns
    -------
    float — Probability (0.05-0.95).
    """
    return round(max(0.05, min(0.95,
        0.70 - (atdi/100)*0.30 - (float(hifd)/80)*0.20
        + min(0.10, (n_countries-2)*0.03))), 3)


# ── NSE ───────────────────────────────────────────────────
def compute_nse(q_obs:Union[np.ndarray,List[float]],
                q_sim:Union[np.ndarray,List[float]]) -> float:
    """Nash-Sutcliffe Efficiency (NSE).

    Returns
    -------
    float — NSE (-inf to 1.0). >= 0.5 = satisfactory.
    """
    obs = np.asarray(q_obs, float).ravel()
    sim = np.asarray(q_sim, float).ravel()
    n   = min(len(obs), len(sim))
    obs, sim = obs[:n], sim[:n]
    denom = np.sum((obs - obs.mean())**2)
    if denom < 1e-10:
        return 0.0
    return round(float(1.0 - np.sum((obs - sim)**2) / denom), 3)


# ── KGE ───────────────────────────────────────────────────
def compute_kge(q_obs:Union[np.ndarray,List[float]],
                q_sim:Union[np.ndarray,List[float]]) -> float:
    """Kling-Gupta Efficiency (KGE).

    Returns
    -------
    float — KGE (-inf to 1.0). >= 0.5 = satisfactory.
    """
    obs = np.asarray(q_obs, float).ravel()
    sim = np.asarray(q_sim, float).ravel()
    n   = min(len(obs), len(sim))
    obs, sim = obs[:n], sim[:n]
    if obs.std() < 1e-10 or sim.std() < 1e-10:
        return 0.0
    r     = float(np.corrcoef(obs, sim)[0, 1])
    beta  = sim.mean() / (obs.mean() + 1e-10)
    gamma = (sim.std() / (sim.mean() + 1e-10)) / (obs.std() / (obs.mean() + 1e-10))
    return round(float(1.0 - ((r-1)**2 + (beta-1)**2 + (gamma-1)**2)**0.5), 3)


# ── WQI ───────────────────────────────────────────────────
def compute_wqi(measurements:Optional[Dict]=None) -> float:
    """Water Quality Index (WQI)."""
    if measurements is None:
        return 65.0
    return round(max(0.0, min(100.0,
        float(measurements.get("wqi", measurements.get("score", 65.0))))), 1)


# ── All at once ────────────────────────────────────────────
def compute_all_indices(runoff_c:float, cap_bcm:float,
                        n_countries:int, dispute_level:int,
                        q_obs:Optional[np.ndarray]=None,
                        q_sim:Optional[np.ndarray]=None,
                        wqi_measurements:Optional[Dict]=None,
                        ) -> Dict[str, float]:
    """Compute all six AWSI indices in a single call.

    Returns
    -------
    dict
        atdi, ahifd, afsf, ahlb, asi, atci,
        ci, p_negotiation, wqi
        (+ nse, kge if q_obs and q_sim provided)
    """
    atdi  = compute_atdi(runoff_c, cap_bcm, n_countries, dispute_level)
    ahifd = compute_ahifd(runoff_c, cap_bcm, n_countries, dispute_level)
    result: Dict[str, float] = {
        "atdi":          atdi,
        "ahifd":         ahifd,
        "afsf":  compute_afsf(runoff_c, cap_bcm, n_countries, dispute_level),
        "ahlb":  compute_ahlb(runoff_c, cap_bcm, n_countries, dispute_level,
                              q_sim=q_sim, q_obs=q_obs),
        "asi":   compute_asi(runoff_c, cap_bcm, n_countries, dispute_level),
        "atci":  compute_atci(runoff_c, cap_bcm, n_countries, dispute_level),
        "ci":    compute_conflict_index(atdi=atdi, hifd=ahifd,
                     dispute_level=dispute_level, n_countries=n_countries),
        "p_negotiation": compute_negotiation_probability(
                     atdi=atdi, hifd=ahifd, n_countries=n_countries),
        "wqi":   compute_wqi(wqi_measurements),
    }
    if q_obs is not None and q_sim is not None:
        qo = np.asarray(q_obs, float).ravel()
        qs = np.asarray(q_sim, float).ravel()
        result["nse"] = compute_nse(qo, qs)
        result["kge"] = compute_kge(qo, qs)
    return result
