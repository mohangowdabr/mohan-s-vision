"""Goal Tracker — projects goal completion and generates nudges."""

from datetime import datetime
import math


def compute_goal_progress(goal):
    now = datetime.now()
    target = datetime.strptime(goal["target_date"], "%Y-%m-%d")
    start = datetime.strptime(goal["start_date"], "%Y-%m-%d")

    total_months = (target.year - start.year) * 12 + (target.month - start.month)
    elapsed_months = (now.year - start.year) * 12 + (now.month - start.month)
    remaining_months = max(0, total_months - elapsed_months)

    funded_pct = min(100, (goal["current_amount"] / goal["target_amount"]) * 100)

    # Project future value with SIP
    monthly_rate = goal["expected_return_rate"] / 100 / 12
    projected_value = goal["current_amount"]

    for _ in range(remaining_months):
        projected_value = projected_value * (1 + monthly_rate) + goal["monthly_sip"]

    on_track = projected_value >= goal["target_amount"]
    shortfall = max(0, goal["target_amount"] - projected_value)

    # Required SIP to meet goal
    required_sip = goal["monthly_sip"]
    if not on_track and remaining_months > 0:
        fv_factor = ((math.pow(1 + monthly_rate, remaining_months) - 1) / monthly_rate) * (1 + monthly_rate)
        current_fv = goal["current_amount"] * math.pow(1 + monthly_rate, remaining_months)
        required_sip = math.ceil((goal["target_amount"] - current_fv) / fv_factor)
        required_sip = max(required_sip, 0)

    sip_increase = max(0, required_sip - goal["monthly_sip"])

    result = {**goal}
    result.update({
        "funded_pct": round(funded_pct, 1),
        "remaining_months": remaining_months,
        "projected_value": round(projected_value),
        "on_track": on_track,
        "shortfall": round(shortfall),
        "required_sip": round(required_sip),
        "sip_increase": round(sip_increase),
    })
    return result


def generate_nudge(goal_progress):
    funded_pct = goal_progress["funded_pct"]
    on_track = goal_progress["on_track"]
    sip_increase = goal_progress["sip_increase"]
    name = goal_progress["name"]
    shortfall = goal_progress["shortfall"]
    remaining_months = goal_progress["remaining_months"]

    if funded_pct >= 100:
        return {"type": "success", "message": f'🎉 Congratulations! Your "{name}" goal is fully funded!',
                "message_hi": f'🎉 बधाई हो! आपका "{name}" लक्ष्य पूरी तरह से पूरा हो गया है!', "action": None}

    if on_track:
        return {"type": "on_track", "message": f'✅ Your "{name}" goal is on track. Keep up the SIPs!',
                "message_hi": f'✅ आपका "{name}" लक्ष्य सही दिशा में है। SIP जारी रखें!', "action": None}

    if sip_increase > 0 and remaining_months > 6:
        return {"type": "increase_sip",
                "message": f'📈 Increase your SIP by ₹{sip_increase:,}/month to reach "{name}" on time.',
                "message_hi": f'📈 "{name}" समय पर पूरा करने के लिए SIP ₹{sip_increase:,}/महीना बढ़ाएं।',
                "action": f"Increase SIP by ₹{sip_increase:,}"}

    return {"type": "at_risk",
            "message": f'⚠️ "{name}" has a projected shortfall of ₹{shortfall:,}. Consider extending the timeline or increasing contributions.',
            "message_hi": f'⚠️ "{name}" में ₹{shortfall:,} की कमी हो सकती है। समय बढ़ाने या योगदान बढ़ाने पर विचार करें।',
            "action": "Review Goal"}


def compute_all_goals(goals):
    results = []
    for goal in goals:
        progress = compute_goal_progress(goal)
        nudge = generate_nudge(progress)
        progress["nudge"] = nudge
        results.append(progress)
    return results
