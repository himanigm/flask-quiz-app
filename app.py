from flask import Flask, render_template, request, redirect, session
from quiz import questions, options, answers

app = Flask(__name__)
app.secret_key = "quiz123"


@app.route("/")
def home():
    session["question_num"] = 0
    session["score"] = 0
    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    if request.method == "POST":

        guess = request.form["answer"]

        question_num = session["question_num"]

        if guess == answers[question_num]:
            session["score"] += 1

        session["question_num"] += 1

    question_num = session["question_num"]

    if question_num >= len(questions):
        return redirect("/result")

    return render_template(
        "quiz.html",
        question=questions[question_num],
        options=options[question_num],
        question_num=question_num
    )


@app.route("/result")
def result():

    score = session["score"]
    total = len(questions)
    percentage = (score / total) * 100

    return render_template(
        "result.html",
        score=score,
        total=total,
        percentage=percentage
    )


if __name__ == "__main__":
    app.run(debug=True)