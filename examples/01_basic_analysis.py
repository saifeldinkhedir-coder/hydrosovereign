"""
Example 1 — Basic basin analysis
=================================
Demonstrates the one-call interface for any of the 26 registered basins.
"""
import hydrosovereign as hsae

# ── Analyse GERD (Blue Nile, Ethiopia) ──────────────────────────
result = hsae.analyze_basin(name="Blue Nile (GERD)")

idx  = result["indices"]
meta = result["metadata"]

print(f"Basin:        {meta['name']}")
print(f"ATDI:         {idx['atdi']:.1f}%   (Transparency Deficit)")
print(f"HIFD:         {idx['hifd']:.1f}%   (Hydrological Instability)")
print(f"Negotiation:  p_success={idx['negotiation']['p_success']:.0%}")
print(f"Strategy:     {idx['negotiation']['strategy']}")
print(f"Alert:        {result['alerts']['atdi_alert']}")
print(f"Legal risk:   {result['legal']['risk_level']}")
print(f"Articles:     {result['legal']['articles'][:3]}")

# ── Compare multiple basins ──────────────────────────────────────
basins = [
    "Blue Nile (GERD)",
    "Niger – Kainji Dam",
    "Mekong – Xayaburi Dam",
    "Nile – High Aswan Dam",
]

print("\n{:<28} {:>8} {:>8} {:>12}".format("Basin","ATDI","HIFD","Risk"))
print("-" * 60)
for name in basins:
    r = hsae.analyze_basin(name=name)
    print("{:<28} {:>7.1f}% {:>7.1f}% {:>12}".format(
        name[:27],
        r["indices"]["atdi"],
        r["indices"]["hifd"],
        r["legal"]["risk_level"],
    ))
