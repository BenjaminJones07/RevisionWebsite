from flask import Flask, render_template, request, session, flash, redirect
from Tools.subjects import SUBJECTS as loadSubj
from flask_session import Session
from cs50 import SQL
import random

app, db, SUBJECTS = Flask(__name__), SQL("sqlite:///revWeb.db"), loadSubj().getSubjectsArr()

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["TEMPLATES_AUTO_RELOAD"] = True
Session(app)

empty = lambda x: x == "" or not x

@app.route("/", methods=["GET", "POST"])
def index():
    session["subjects"] = SUBJECTS if not session.get("subjects") else session["subjects"]
    if request.method == "GET": return render_template("index.html", subj=SUBJECTS)
    session["subjects"] = list(dict.fromkeys([x for x in request.form.getlist("subjects") if x in SUBJECTS]))
    return redirect("/")

@app.route("/question", methods=["GET", "POST"])
def question():
    if request.method == "GET":
        session["subjects"] = SUBJECTS if not session.get("subjects") else session["subjects"]
        session["subj"] = random.choice([subj for subj in session["subjects"]]) # Select random subject
        max = db.execute("SELECT MAX(id) FROM {0}".format(session["subj"]))[0]['MAX(id)'] # Get max ID
        session["id"] = random.choice([x for x in range(1, max+1) if x != session.get("id")]) # Get ID in range not equal to previous ID
        row = db.execute("SELECT id, question, answers FROM {0} WHERE id = ?".format(session["subj"]), session["id"])[0] # Get the random row
        return render_template("question.html", question=row["question"], answers=dict(zip(range(1, len(row["answers"].split(';'))+1), row["answers"].split(';')))) # Render question template
    
    id, choice = session.get("id"), request.form.get("choice") # Get form params
    if empty(id) or empty(choice): return redirect("/question") # Check that choice and id exist, therefore also proving subj exists
    
    try: choice = int(choice) # If choice not int...
    except: return redirect("/question") # ...redirect to question
    
    row = db.execute("SELECT ansNo, answers, reason FROM {0} WHERE id = ?".format(session["subj"]), id)[0]
    (answer, answers, reason) = (row["ansNo"], row["answers"], row["reason"])
    
    flashMsg, cat = ("Correct!", "good") if answer == choice else ("Incorrect, the answer was '{0}'.".format(answers.split(';')[answer-1]), "bad")
    
    flash(flashMsg if reason == None else "{0} {1}".format(flashMsg, reason), cat)
    return redirect("/question")

app.run(host="0.0.0.0", port=8080)