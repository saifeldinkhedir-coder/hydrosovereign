"""
Example 4 — Legal and geopolitical assessment
=============================================
Demonstrates ATDI-based legal article triggering under UNWC 1997.
"""
from hydrosovereign.indices import compute_atdi, compute_hifd
from hydrosovereign.legal   import get_legal_assessment
from hydrosovereign.basins  import BASINS_26

print(f"{'Basin':<30} {'ATDI':>6} {'HIFD':>6} {'Risk':<10} Articles")
print("-" * 90)

for b in BASINS_26:
    atdi  = compute_atdi(b["runoff_c"], b["cap"],
                          len(b["country"]), b["dispute_level"])
    hifd  = compute_hifd(b["runoff_c"], b["cap"],
                          len(b["country"]), b["dispute_level"])
    legal = get_legal_assessment(atdi, hifd, b["dispute_level"], len(b["country"]))

    arts = ", ".join(legal["articles"][:2])
    print(f"{b['name']:<30} {atdi:>5.1f}% {hifd:>5.1f}%  {legal['risk_level']:<10} {arts}")
