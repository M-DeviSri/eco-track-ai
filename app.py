from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_score(travel, electricity):
    return (travel * 0.12) + (electricity * 0.5)

def get_recommendation(score):
    if score > 100:
        return "High footprint. Reduce vehicle usage and electricity consumption."
    elif score > 50:
        return "Moderate footprint. Consider adopting more sustainable habits."
    else:
        return "Great job! Your footprint is relatively low."

@app.route("/", methods=["GET", "POST"])
def home():

    score = None
    recommendation = ""

    if request.method == "POST":

        try:
            travel = max(0, float(request.form["travel"]))
            electricity = max(0, float(request.form["electricity"]))
            diet = request.form["diet"]

            score = calculate_score(travel, electricity)

            recommendation = get_recommendation(score)

            if diet == "non-vegetarian":
                recommendation += " Consider reducing meat consumption to lower emissions."
            else:
                recommendation += " Great choice! Plant-based diets generally have a lower carbon footprint."

        except ValueError:
            recommendation = "Invalid input. Please enter valid values."

    return render_template(
        "index.html",
        score=score,
        recommendation=recommendation
    )

if __name__ == "__main__":
    app.run(debug=True)