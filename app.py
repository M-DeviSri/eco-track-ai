from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    recommendation = ""

    if request.method == "POST":
        travel = float(request.form["travel"])
        electricity = float(request.form["electricity"])

        score = (travel * 0.12) + (electricity * 0.5)

        if score > 100:
            recommendation = "High footprint. Reduce vehicle usage and energy consumption."
        elif score > 50:
            recommendation = "Moderate footprint. Consider switching to sustainable habits."
        else:
            recommendation = "Great job! Your footprint is relatively low."

    return render_template(
        "index.html",
        score=score,
        recommendation=recommendation
    )

if __name__ == "__main__":
    app.run(debug=True)