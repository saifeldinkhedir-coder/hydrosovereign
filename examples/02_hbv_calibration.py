"""
Example 2 — HBV-96 rainfall-runoff modelling
=============================================
Simulates daily discharge from precipitation and temperature,
then calibrates the model using SCE-UA.
"""
import numpy as np
from hydrosovereign.hbv     import run_hbv96, calibrate_hbv_sceua
from hydrosovereign.indices import compute_nse, compute_kge
from hydrosovereign.basins  import get_basin

# ── Basin parameters ─────────────────────────────────────────────
basin    = get_basin("Blue Nile (GERD)")
area_km2 = basin["eff_cat_km2"]   # 174,000 km²
runoff_c = basin["runoff_c"]      # 0.38

# ── Synthetic forcing (replace with real data) ───────────────────
np.random.seed(42)
n_days = 365 * 5       # 5 years
P = np.maximum(0, np.random.gamma(1.5, 4.0, n_days))         # mm/day
T = 20 + 12 * np.sin(np.linspace(0, 2 * np.pi * 5, n_days))  # °C

# ── Forward simulation ───────────────────────────────────────────
sim = run_hbv96(P, T, area_km2=area_km2, runoff_c=runoff_c)
Q_sim = sim["Q_sim"]   # mm/day
SM    = sim["SM"]      # soil moisture (mm)
SNOW  = sim["SNOW"]    # snow water equivalent (mm)

print(f"Simulation — {n_days} days")
print(f"  Q_sim mean : {Q_sim.mean():.2f} mm/day")
print(f"  Q_sim max  : {Q_sim.max():.2f} mm/day")
print(f"  SM mean    : {SM.mean():.2f} mm")

# ── Add noise to create synthetic observations ───────────────────
Q_obs = Q_sim * (1 + np.random.normal(0, 0.08, n_days))
Q_obs = np.maximum(Q_obs, 0)

# ── Calibration (SCE-UA) ─────────────────────────────────────────
print("\nCalibrating HBV-96 with SCE-UA ...")
cal = calibrate_hbv_sceua(Q_obs, P, T, area_km2=area_km2)

print(f"  Calibrated NSE : {cal['nse']:.4f}  (target ≥ 0.70)")
print(f"  Best parameters: {cal['params']}")

# ── Validation metrics ───────────────────────────────────────────
Q_cal = cal["Q_sim"]
print(f"  NSE  = {compute_nse(Q_obs, Q_cal):.4f}")
print(f"  KGE  = {compute_kge(Q_obs, Q_cal):.4f}")
