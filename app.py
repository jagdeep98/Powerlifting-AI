from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        exp = request.form["experience"].lower()
        squat = int(request.form["squat"])
        bench = int(request.form["bench"])
        deadlift = int(request.form["deadlift"])
        freq = int(request.form["frequency"])

        # Training % based on experience
        if exp == "beginner":
            percents = {"main": 0.65, "secondary": 0.6}
        elif exp == "intermediate":
            percents = {"main": 0.7, "secondary": 0.65}
        else:
            percents = {"main": 0.75, "secondary": 0.7}

        # 1-week plan (3-day template)
        plan = {
            "Day 1 - Squat Focus": [
                f"Squat: 4x5 @ {squat*percents['main']:.0f}",
                f"Bench: 4x6 @ {bench*percents['secondary']:.0f}",
                "Accessories: rows, abs"
            ],
            "Day 2 - Bench Focus": [
                f"Bench: 5x5 @ {bench*percents['main']:.0f}",
                f"Deadlift: 4x4 @ {deadlift*percents['secondary']:.0f}",
                "Accessories: pull-ups, triceps"
            ],
            "Day 3 - Deadlift Focus": [
                f"Deadlift: 4x5 @ {deadlift*percents['main']:.0f}",
                f"Squat (light): 3x6 @ {squat*percents['secondary']:.0f}",
                "Accessories: hamstrings, core"
            ]
        }

        return render_template("plan.html", plan=plan)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
