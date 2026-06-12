from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_score(travel, electricity):
    """Calculate estimated carbon footprint score."""
    return (travel * 0.12) + (electricity * 0.5)


def get_recommendation(score):
    """Return recommendation based on footprint score."""

    if score > 100:
        category = "High Impact"
        recommendation = "Your carbon footprint is high. Consider reducing vehicle usage and electricity consumption."
        tips = [
            "Use public transport at least twice a week",
            "Switch to LED lighting",
            "Reduce air-conditioner usage",
            "Consider cycling for short trips"
        ]

    elif score > 50:
        category = "Moderate Impact"
        recommendation = "Your carbon footprint is moderate. Small lifestyle changes can make a big difference."
        tips = [
            "Turn off unused appliances",
            "Reduce unnecessary travel",
            "Use energy-efficient devices",
            "Track monthly electricity usage"
        ]

    else:
        category = "Low Impact"
        recommendation = "Excellent! Your carbon footprint is relatively low."
        tips = [
            "Continue sustainable habits",
            "Promote eco-friendly practices",
            "Plant trees in your community",
            "Encourage family members to reduce emissions"
        ]

    return category, recommendation, tips


@app.route("/", methods=["GET", "POST"])
def home():

    score = None
    category = None
    recommendation = ""
    tips = []

    if request.method == "POST":

        try:
            travel = max(0, float(request.form["travel"]))
            electricity = max(0, float(request.form["electricity"]))
            diet = request.form["diet"]

            score = calculate_score(travel, electricity)

            category, recommendation, tips = get_recommendation(score)

            if diet == "non-vegetarian":
                recommendation += " Consider reducing meat consumption to lower emissions."
            else:
                recommendation += " Great choice! Plant-based diets generally have a lower carbon footprint."

        except ValueError:
            recommendation = "Invalid input."

    return render_template(
        "index.html",
        score=score,
        category=category,
        recommendation=recommendation,
        tips=tips
    )


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)