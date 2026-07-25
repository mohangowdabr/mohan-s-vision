# Mock portfolio data — structured to mirror the AA (Account Aggregator) FI schema.
# All prices in INR. Data is realistic but fictional.

user_profile = {
    "id": "USR-001",
    "name": "Arjun Mehta",
    "age": 32,
    "email": "arjun.mehta@email.com",
    "phone": "+91 98765 43210",
    "pan": "ABCPM1234F",
    "risk_profile": "Moderate",  # Conservative | Moderate | Aggressive
    "income_range": "₹15-25 LPA",
    "investing_since": "2019",
    "kyc_status": "Verified",
    "aa_consent": True,
    "advisors": [
        {"name": "Priya Sharma", "reg_number": "INA000012345", "type": "RIA", "verified": True},
        {"name": "FinanceGuru_YT", "reg_number": None, "type": "Finfluencer", "verified": False},
    ],
    "trading_behaviour": {
        "avg_trades_per_month": 18,
        "panic_sell_events": 2,
        "churn_rate": 0.35,
        "social_media_driven_trades": 4,
        "fomo_buys": 3,
    },
}

equities = [
    {"symbol": "RELIANCE", "name": "Reliance Industries Ltd", "exchange": "NSE", "quantity": 25, "avg_buy_price": 2380, "current_price": 2945, "sector": "Energy / Conglomerate", "market_cap": "Large Cap", "day_change": 1.2},
    {"symbol": "TCS", "name": "Tata Consultancy Services", "exchange": "NSE", "quantity": 15, "avg_buy_price": 3520, "current_price": 3890, "sector": "IT Services", "market_cap": "Large Cap", "day_change": -0.4},
    {"symbol": "HDFCBANK", "name": "HDFC Bank Ltd", "exchange": "NSE", "quantity": 40, "avg_buy_price": 1580, "current_price": 1725, "sector": "Banking", "market_cap": "Large Cap", "day_change": 0.8},
    {"symbol": "INFY", "name": "Infosys Ltd", "exchange": "NSE", "quantity": 30, "avg_buy_price": 1420, "current_price": 1580, "sector": "IT Services", "market_cap": "Large Cap", "day_change": 1.5},
    {"symbol": "TATAMOTORS", "name": "Tata Motors Ltd", "exchange": "NSE", "quantity": 60, "avg_buy_price": 620, "current_price": 785, "sector": "Automobile", "market_cap": "Large Cap", "day_change": 2.1},
    {"symbol": "BAJFINANCE", "name": "Bajaj Finance Ltd", "exchange": "NSE", "quantity": 10, "avg_buy_price": 6950, "current_price": 7420, "sector": "Financial Services", "market_cap": "Large Cap", "day_change": -0.3},
    {"symbol": "SUNPHARMA", "name": "Sun Pharmaceutical", "exchange": "NSE", "quantity": 35, "avg_buy_price": 1180, "current_price": 1345, "sector": "Pharma", "market_cap": "Large Cap", "day_change": 0.6},
    {"symbol": "ITC", "name": "ITC Ltd", "exchange": "NSE", "quantity": 100, "avg_buy_price": 410, "current_price": 465, "sector": "FMCG", "market_cap": "Large Cap", "day_change": 0.2},
]

mutual_funds = [
    {"name": "Nifty 50 Index Fund – Direct Growth", "amc": "UTI AMC", "category": "Equity – Index", "units": 450.32, "nav": 185.6, "invested_amount": 65000, "sip_amount": 5000, "sip_active": True, "risk_level": "Moderate"},
    {"name": "HDFC Mid-Cap Opportunities Fund", "amc": "HDFC AMC", "category": "Equity – Mid Cap", "units": 280.15, "nav": 220.4, "invested_amount": 50000, "sip_amount": 3000, "sip_active": True, "risk_level": "High"},
    {"name": "ICICI Pru Short Term Fund – Direct Growth", "amc": "ICICI Prudential AMC", "category": "Debt – Short Duration", "units": 1200.5, "nav": 52.8, "invested_amount": 55000, "sip_amount": 0, "sip_active": False, "risk_level": "Low"},
    {"name": "Axis ELSS Tax Saver Fund – Direct Growth", "amc": "Axis AMC", "category": "Equity – ELSS", "units": 320.75, "nav": 98.5, "invested_amount": 25000, "sip_amount": 2500, "sip_active": True, "risk_level": "High"},
    {"name": "SBI Balanced Advantage Fund", "amc": "SBI AMC", "category": "Hybrid – Dynamic", "units": 550.0, "nav": 72.3, "invested_amount": 30000, "sip_amount": 2000, "sip_active": True, "risk_level": "Moderate"},
]

bonds = [
    {"name": "Sovereign Gold Bond 2024-25 Series II", "type": "SGB", "face_value": 6200, "units": 5, "purchase_price": 5800, "current_price": 6450, "maturity_date": "2032-09-15", "coupon_rate": 2.5, "issuer": "RBI / Government of India"},
    {"name": "Government Security 7.26% 2033", "type": "G-Sec", "face_value": 100, "units": 500, "purchase_price": 98.5, "current_price": 101.2, "maturity_date": "2033-01-15", "coupon_rate": 7.26, "issuer": "Government of India"},
    {"name": "RBI Floating Rate Bond 2028", "type": "FRB", "face_value": 1000, "units": 50, "purchase_price": 1000, "current_price": 1000, "maturity_date": "2028-07-01", "coupon_rate": 8.05, "issuer": "RBI"},
]

gold = [
    {"name": "Digital Gold (Augmont)", "type": "Digital Gold", "grams": 15.5, "avg_buy_price_per_gram": 5800, "current_price_per_gram": 7250, "platform": "Paytm Gold", "exclude_from_total": False},
    {"name": "Sovereign Gold Bond 2024-25", "type": "SGB", "grams": 5, "avg_buy_price_per_gram": 5800, "current_price_per_gram": 6450, "platform": "RBI Direct", "exclude_from_total": True},
]

nps = {
    "tier1": {
        "total_contribution": 180000,
        "current_value": 245000,
        "allocation": {"equity_e": 50, "corporate_bond_c": 30, "gov_sec_g": 15, "alternative_a": 5},
        "pfm": "SBI Pension Funds",
    },
    "tier2": {
        "total_contribution": 40000,
        "current_value": 48500,
        "allocation": {"equity_e": 60, "corporate_bond_c": 25, "gov_sec_g": 15, "alternative_a": 0},
        "pfm": "SBI Pension Funds",
    },
}

reits_invits = [
    {"name": "Brookfield India Real Estate Trust", "type": "REIT", "units": 50, "avg_buy_price": 280, "current_price": 315, "distribution_yield": 6.8, "sector": "Commercial Real Estate"},
    {"name": "India Grid Trust", "type": "InvIT", "units": 100, "avg_buy_price": 142, "current_price": 155, "distribution_yield": 11.2, "sector": "Power Transmission"},
]


def compute_holdings():
    eq_total = sum(e["quantity"] * e["current_price"] for e in equities)
    eq_invested = sum(e["quantity"] * e["avg_buy_price"] for e in equities)

    mf_total = sum(f["units"] * f["nav"] for f in mutual_funds)
    mf_invested = sum(f["invested_amount"] for f in mutual_funds)

    bond_total = sum(b["units"] * b["current_price"] for b in bonds)
    bond_invested = sum(b["units"] * b["purchase_price"] for b in bonds)

    gold_total = sum(g["grams"] * g["current_price_per_gram"] for g in gold if not g["exclude_from_total"])
    gold_invested = sum(g["grams"] * g["avg_buy_price_per_gram"] for g in gold if not g["exclude_from_total"])

    nps_total = nps["tier1"]["current_value"] + nps["tier2"]["current_value"]
    nps_invested = nps["tier1"]["total_contribution"] + nps["tier2"]["total_contribution"]

    reit_total = sum(r["units"] * r["current_price"] for r in reits_invits)
    reit_invested = sum(r["units"] * r["avg_buy_price"] for r in reits_invits)

    total_current = eq_total + mf_total + bond_total + gold_total + nps_total + reit_total
    total_invested = eq_invested + mf_invested + bond_invested + gold_invested + nps_invested + reit_invested

    by_class = {
        "equities":     {"current": eq_total,   "invested": eq_invested,   "pct": (eq_total / total_current) * 100},
        "mutual_funds": {"current": mf_total,   "invested": mf_invested,   "pct": (mf_total / total_current) * 100},
        "bonds":        {"current": bond_total, "invested": bond_invested, "pct": (bond_total / total_current) * 100},
        "gold":         {"current": gold_total, "invested": gold_invested, "pct": (gold_total / total_current) * 100},
        "nps":          {"current": nps_total,  "invested": nps_invested,  "pct": (nps_total / total_current) * 100},
        "reits_invits": {"current": reit_total, "invested": reit_invested, "pct": (reit_total / total_current) * 100},
    }

    return {
        "by_class": by_class,
        "total_current": total_current,
        "total_invested": total_invested,
        "total_gain": total_current - total_invested,
        "total_gain_pct": ((total_current - total_invested) / total_invested) * 100,
    }
