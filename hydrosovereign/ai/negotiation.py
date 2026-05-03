"""
negotiation.py — NegotiationAI for basin dispute analysis
"""
from __future__ import annotations


class NegotiationAI:
    """AI-based negotiation probability estimator for transboundary basins."""

    _THRESHOLDS = {
        "low":    (0.0,  30.0),
        "medium": (30.0, 55.0),
        "high":   (55.0, 75.0),
        "crisis": (75.0, 100.0),
    }

    def predict(self, atdi: float, hifd: float, n_countries: int,
                dispute_level: int) -> dict:
        """
        Predict negotiation probability and recommend strategy.

        Parameters
        ----------
        atdi : float
            Alkhedir Transparency Deficit Index (0-100).
        hifd : float
            Hydrological Instability Factor Delta (0-100).
        n_countries : int
            Number of riparian states.
        dispute_level : int
            Dispute level 1-5.

        Returns
        -------
        dict
            p_success, strategy, un_path, risk
        """
        # Negotiation success probability (inverse of combined stress)
        stress = (0.4 * atdi + 0.3 * hifd +
                  0.15 * (dispute_level / 5.0) * 100 +
                  0.15 * min(n_countries / 6.0, 1.0) * 100)

        p_success = max(0.05, min(0.95, 1.0 - stress / 100.0))

        # Strategy recommendation
        if dispute_level >= 4 or atdi > 60:
            strategy  = "PCA Arbitration"
            un_path   = "Art.33 → PCA"
            risk      = "HIGH"
        elif dispute_level >= 3 or atdi > 40:
            strategy  = "Joint Technical Commission"
            un_path   = "Art.8 → JTC"
            risk      = "MEDIUM"
        else:
            strategy  = "Bilateral Negotiation"
            un_path   = "Art.3 → Bilateral"
            risk      = "LOW"

        return {
            "p_success": round(p_success, 2),
            "strategy":  strategy,
            "un_path":   un_path,
            "risk":      risk,
        }
