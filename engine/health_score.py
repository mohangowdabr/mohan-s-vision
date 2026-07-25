"""Mohan's Vision Financial Health Score Engine.
Computes a composite 0-900 score from four SEBI-relevant signals."""

from data.portfolio import compute_holdings, user_profile, equities

# Ideal allocations by risk profile
IDEAL_ALLOCATIONS = {
    "Conservative": {"equities": 20, "mutual_funds": 25, "bonds": 30, "gold": 15, "nps": 8, "reits_invits": 2},
    "Moderate":     {"equities": 35, "mutual_funds": 25, "bonds": 15, "gold": 10, "nps": 10, "reits_invits": 5},
    "Aggressive":   {"equities": 50, "mutual_funds": 20, "bonds": 5,  "gold": 5,  "nps": 10, "reits_invits": 10},
}


def compute_diversification_score(holdings, risk_profile):
    """Measures how well the portfolio matches the ideal allocation."""
    ideal = IDEAL_ALLOCATIONS.get(risk_profile, IDEAL_ALLOCATIONS["Moderate"])
    actual = holdings["by_class"]

    total_deviation = 0
    details = {}

    for asset_class, ideal_pct in ideal.items():
        actual_pct = actual.get(asset_class, {}).get("pct", 0)
        deviation = abs(actual_pct - ideal_pct)
        total_deviation += deviation
        details[asset_class] = {
            "ideal": ideal_pct,
            "actual": round(actual_pct, 1),
            "deviation": round(deviation, 1),
        }

    score = max(0, round(100 - (total_deviation / 2)))

    if score >= 75:
        label = "Well Diversified"
    elif score >= 50:
        label = "Moderately Diversified"
    else:
        label = "Poorly Diversified"

    return {"score": score, "details": details, "ideal": ideal, "label": label}


def compute_concentration_risk(holdings):
    """Penalizes over-concentration in single stocks, sectors, or high-risk instruments."""
    total = holdings["total_current"]
    penalties = 0
    flags = []

    # Single-stock concentration (>15%)
    for stock in equities:
        pct = (stock["quantity"] * stock["current_price"] / total) * 100
        if pct > 15:
            penalties += (pct - 15) * 2
            flags.append(f"{stock['symbol']} is {pct:.1f}% of portfolio (>15% threshold)")

    # Equity concentration (>60%)
    eq_pct = holdings["by_class"]["equities"]["pct"]
    if eq_pct > 60:
        penalties += (eq_pct - 60) * 1.5
        flags.append(f"Equities are {eq_pct:.1f}% of total (>60% threshold)")

    # Sector concentration (>25%)
    sector_map = {}
    for stock in equities:
        value = stock["quantity"] * stock["current_price"]
        sector_map[stock["sector"]] = sector_map.get(stock["sector"], 0) + value
    for sector, value in sector_map.items():
        pct = (value / total) * 100
        if pct > 25:
            penalties += (pct - 25) * 1.5
            flags.append(f"{sector} sector is {pct:.1f}% of total (>25% threshold)")

    # Social media driven trades
    behaviour = user_profile["trading_behaviour"]
    if behaviour["social_media_driven_trades"] > 2:
        penalties += behaviour["social_media_driven_trades"] * 3
        flags.append(f"{behaviour['social_media_driven_trades']} trades driven by social media tips")

    score = max(0, round(100 - penalties))

    if score >= 75:
        label = "Low Risk"
    elif score >= 50:
        label = "Moderate Risk"
    else:
        label = "High Concentration"

    return {"score": score, "flags": flags, "label": label}


def compute_advisor_trust_score(profile):
    """Checks if advisors/influencers are SEBI-registered."""
    advisors = profile.get("advisors", [])
    if not advisors:
        return {"score": 70, "details": [], "label": "No Advisors Linked"}

    total_weight = 0
    trusted_weight = 0
    details = []

    for advisor in advisors:
        weight = 2 if advisor["type"] in ("RIA", "RA") else 1
        total_weight += weight

        if advisor["verified"]:
            trusted_weight += weight
            details.append({"name": advisor["name"], "status": "Verified", "type": advisor["type"], "reg_number": advisor["reg_number"]})
        else:
            details.append({"name": advisor["name"], "status": "Unverified", "type": advisor["type"], "reg_number": None})

    score = round((trusted_weight / total_weight) * 100) if total_weight > 0 else 70

    if score >= 75:
        label = "Trusted Sources"
    elif score >= 50:
        label = "Mixed Sources"
    else:
        label = "Risky Sources"

    return {"score": score, "details": details, "label": label}


def compute_behavioural_risk(profile):
    """Detects churn, panic-selling, and social-media-driven trading patterns."""
    behaviour = profile["trading_behaviour"]
    penalties = 0
    flags = []

    if behaviour["churn_rate"] > 0.3:
        penalties += (behaviour["churn_rate"] - 0.3) * 100
        flags.append(f"High portfolio churn rate: {behaviour['churn_rate'] * 100:.0f}%")

    if behaviour["avg_trades_per_month"] > 15:
        penalties += (behaviour["avg_trades_per_month"] - 15) * 2
        flags.append(f"{behaviour['avg_trades_per_month']} trades/month (above 15 threshold)")

    if behaviour["panic_sell_events"] > 0:
        penalties += behaviour["panic_sell_events"] * 8
        flags.append(f"{behaviour['panic_sell_events']} panic-sell events detected")

    if behaviour["social_media_driven_trades"] > 1:
        penalties += behaviour["social_media_driven_trades"] * 5
        flags.append(f"{behaviour['social_media_driven_trades']} trades influenced by social media")

    if behaviour["fomo_buys"] > 0:
        penalties += behaviour["fomo_buys"] * 6
        flags.append(f"{behaviour['fomo_buys']} FOMO-driven purchases at 52-week highs")

    score = max(0, round(100 - penalties))

    if score >= 75:
        label = "Disciplined"
    elif score >= 50:
        label = "Needs Improvement"
    else:
        label = "Risky Behaviour"

    return {"score": score, "flags": flags, "label": label}


def compute_health_score():
    """Compute the composite Financial Health Score (0-900)."""
    holdings = compute_holdings()
    profile = user_profile

    diversification = compute_diversification_score(holdings, profile["risk_profile"])
    concentration = compute_concentration_risk(holdings)
    advisor_trust = compute_advisor_trust_score(profile)
    behavioural = compute_behavioural_risk(profile)

    composite = (
        diversification["score"] * 0.30 +
        concentration["score"] * 0.25 +
        advisor_trust["score"] * 0.20 +
        behavioural["score"] * 0.25
    ) * 9

    rounded_score = round(composite)

    if rounded_score >= 750:
        band, band_color = "Excellent", "#00d4aa"
    elif rounded_score >= 550:
        band, band_color = "Good", "#f0c000"
    elif rounded_score >= 350:
        band, band_color = "Needs Attention", "#ff8c00"
    else:
        band, band_color = "At Risk", "#ff3b5c"

    return {
        "score": rounded_score,
        "max_score": 900,
        "band": band,
        "band_color": band_color,
        "signals": {
            "diversification": diversification,
            "concentration": concentration,
            "advisor_trust": advisor_trust,
            "behavioural": behavioural,
        },
        "holdings": holdings,
        "profile": profile,
    }
