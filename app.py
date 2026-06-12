from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route("/test")
def test():
    return "API Working"

# =========================
# CORE LOGIC
# =========================

def calculate_score(travel, electricity):
    """Calculate estimated carbon footprint score."""
    return (travel * 0.12) + (electricity * 0.5)


def get_recommendation(score):
    """Return category, recommendation, and tips based on score."""

    if score > 100:
        category = "High Impact"
        recommendation = (
            "Your carbon footprint is high. "
            "Consider reducing vehicle usage and electricity consumption."
        )
        tips = [
            "Use public transport at least twice a week",
            "Switch to LED lighting",
            "Reduce air-conditioner usage",
            "Cycle for short distances"
        ]

    elif score > 50:
        category = "Moderate Impact"
        recommendation = (
            "Your carbon footprint is moderate. "
            "Small lifestyle changes can make a big difference."
        )
        tips = [
            "Turn off unused appliances",
            "Reduce unnecessary travel",
            "Use energy-efficient devices",
            "Track monthly electricity usage"
        ]

    else:
        category = "Low Impact"
        recommendation = "Excellent! Your carbon footprint is low."
        tips = [
            "Continue sustainable habits",
            "Promote eco-friendly practices",
            "Plant trees in your community",
            "Encourage others to reduce emissions"
        ]

    return category, recommendation, tips


# =========================
# UI ROUTE (WEB PAGE)
# =========================

@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    category = None
    recommendation = ""
    tips = []

    if request.method == "POST":
        try:
            travel = max(0, float(request.form.get("travel", 0)))
            electricity = max(0, float(request.form.get("electricity", 0)))
            diet = request.form.get("diet", "vegetarian")

            score = calculate_score(travel, electricity)
            category, recommendation, tips = get_recommendation(score)

            if diet == "non-vegetarian":
                recommendation += " Consider reducing meat consumption."
            else:
                recommendation += " Great choice! Plant-based diets reduce emissions."

        except Exception:
            category = "Error"
            recommendation = "Invalid input. Please enter valid numbers."

    return render_template(
        "index.html",
        score=score,
        category=category,
        recommendation=recommendation,
        tips=tips
    )


# =========================
# API ROUTE (IMPORTANT FOR SCORE)
# =========================

@app.route("/api/calculate", methods=["POST"])
def api_calculate():
    data = request.get_json()

    travel = max(0, float(data.get("travel", 0)))
    electricity = max(0, float(data.get("electricity", 0)))
    diet = data.get("diet", "vegetarian")

    score = calculate_score(travel, electricity)
    category, recommendation, tips = get_recommendation(score)

    if diet == "non-vegetarian":
        recommendation += " Consider reducing meat consumption."
    else:
        recommendation += " Good choice!"

    return jsonify({
        "score": round(score, 2),
        "category": category,
        "recommendation": recommendation,
        "tips": tips
    })


# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)