"""Fraud Shield — checks advisors, schemes, and apps against SEBI registry."""

import re
from data.sebi_registry import sebi_intermediaries, scam_alerts, known_finfluencers


def normalize(text):
    return re.sub(r'[^a-z0-9\s]', '', text.lower()).strip()


def fuzzy_match(query, target):
    nq = normalize(query)
    nt = normalize(target)
    if not nq or not nt:
        return 0

    if nt in nq or nq in nt:
        return 1.0

    q_tokens = nq.split()
    t_tokens = nt.split()
    match_count = sum(1 for qt in q_tokens if any(tt in qt or qt in tt for tt in t_tokens))
    return match_count / max(len(q_tokens), 1)


def check_entity(query):
    if not query or len(query.strip()) < 2:
        return {"status": "empty", "message": "Please enter a name to check."}

    results = {
        "query": query.strip(),
        "registered_matches": [],
        "scam_matches": [],
        "finfluencer_matches": [],
        "status": "not_found",
        "risk_level": "unknown",
        "message": "",
    }

    # 1. Check SEBI registered intermediaries
    for entity in sebi_intermediaries:
        name_score = fuzzy_match(query, entity["name"])
        reg_score = fuzzy_match(query, entity["reg_number"]) if entity.get("reg_number") else 0
        best_score = max(name_score, reg_score)
        if best_score >= 0.5:
            results["registered_matches"].append({**entity, "match_score": best_score})

    results["registered_matches"].sort(key=lambda x: x["match_score"], reverse=True)

    # 2. Check scam alerts
    for scam in scam_alerts:
        name_score = fuzzy_match(query, scam["scheme_name"])
        keyword_score = max((fuzzy_match(query, kw) for kw in scam["keywords"]), default=0)
        best_score = max(name_score, keyword_score)
        if best_score >= 0.5:
            results["scam_matches"].append({**scam, "match_score": best_score})

    results["scam_matches"].sort(key=lambda x: x["match_score"], reverse=True)

    # 3. Check finfluencers
    for fin in known_finfluencers:
        score = fuzzy_match(query, fin["name"])
        if score >= 0.5:
            results["finfluencer_matches"].append({**fin, "match_score": score})

    # Determine status
    if results["scam_matches"]:
        s = results["scam_matches"][0]
        results["status"] = "scam_alert"
        results["risk_level"] = "critical"
        results["message"] = f'⚠️ SCAM ALERT: "{s["scheme_name"]}" matches a known SEBI advisory. Do NOT invest.'
    elif results["registered_matches"]:
        m = results["registered_matches"][0]
        if m["status"] == "Active":
            results["status"] = "verified"
            results["risk_level"] = "safe"
            results["message"] = f'✅ "{m["name"]}" is SEBI-registered ({m["category"]}) — Registration: {m["reg_number"]}'
        else:
            results["status"] = "suspended"
            results["risk_level"] = "warning"
            results["message"] = f'⚠️ "{m["name"]}" registration is {m["status"]}. Exercise caution.'
    elif results["finfluencer_matches"]:
        f = results["finfluencer_matches"][0]
        results["status"] = "finfluencer"
        results["risk_level"] = "warning"
        results["message"] = f'⚠️ "{f["name"]}" is a social media influencer and is NOT SEBI-registered.'
    else:
        results["status"] = "not_found"
        results["risk_level"] = "unknown"
        results["message"] = f'❓ "{query}" was not found in SEBI\'s registered intermediary database.'

    return results


def get_recent_scam_alerts(count=6):
    return sorted(scam_alerts, key=lambda x: x["alert_date"], reverse=True)[:count]


def get_search_suggestions(query):
    if not query or len(query) < 2:
        return []

    suggestions = []
    for entity in sebi_intermediaries:
        if fuzzy_match(query, entity["name"]) >= 0.3:
            suggestions.append({"label": entity["name"], "type": "registered", "category": entity["category"]})
    for scam in scam_alerts:
        if fuzzy_match(query, scam["scheme_name"]) >= 0.3:
            suggestions.append({"label": scam["scheme_name"], "type": "scam", "category": scam["type"]})
    for fin in known_finfluencers:
        if fuzzy_match(query, fin["name"]) >= 0.3:
            suggestions.append({"label": fin["name"], "type": "finfluencer", "category": fin["platform"]})

    return suggestions[:8]
