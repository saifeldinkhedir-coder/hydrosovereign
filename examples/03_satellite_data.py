"""
Example 3 — Real satellite data ingestion
==========================================
Fetch real Open-Meteo ERA5 data for any basin location.
No API key required.
"""
from hydrosovereign.data    import fetch_openmeteo
from hydrosovereign.basins  import get_basin
from hydrosovereign.hbv     import run_hbv96
from hydrosovereign.indices import compute_nse
import numpy as np

# ── Basin ──────────────────────────────────────────────────────
basin = get_basin("Blue Nile (GERD)")
lat, lon = basin["lat"], basin["lon"]

# ── Fetch real ERA5 data ────────────────────────────────────────
print(f"Fetching ERA5 data for ({lat}°N, {lon}°E) ...")
data = fetch_openmeteo(lat, lon, "2023-01-01", "2023-12-31")

P = np.array(data["P_mm_day"])   # daily precipitation
T = np.array(data["T_C"])        # daily temperature
days = len(data["dates"])

print(f"  Days fetched : {days}")
print(f"  P mean       : {P.mean():.3f} mm/day")
print(f"  T mean       : {T.mean():.1f} °C")
print(f"  P annual sum : {P.sum():.1f} mm/year")

# ── Run HBV-96 on real forcing ──────────────────────────────────
sim = run_hbv96(P, T, area_km2=basin["eff_cat_km2"], runoff_c=basin["runoff_c"])
Q   = sim["Q_sim"]
print(f"  Q_sim mean   : {Q.mean():.2f} mm/day")
print(f"  Q_sim max    : {Q.max():.2f} mm/day  (peak flow)")
