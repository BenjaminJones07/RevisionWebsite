from flask import Flask, render_template, request, session, flash, redirect
from flask_session import Session
from cs50 import SQL
import random

app, db = Flask(__name__), SQL("sqlite:///revWeb.db")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["TEMPLATES_AUTO_RELOAD"] = True
Session(app)

empty = lambda x: x == "" or not x
SUBJECTS = ["biology", "history"]

@app.route("/")
def index(): return render_template("index.html")

@app.route("/question", methods=["GET", "POST"])
def question():
    if request.method == "GET":
        session["subj"] = random.choice([subj for subj in SUBJECTS]) # Select random subject
        max = db.execute("SELECT MAX(id) FROM {0}".format(session["subj"]))[0]['MAX(id)'] # Get max ID
        session["id"] = random.choice([x for x in range(1, max+1) if x != session.get("id")]) # Get ID in range not equal to previous ID
        row = db.execute("SELECT id, question, answers FROM {0} WHERE id = ?".format(session["subj"]), session["id"])[0] # Get the random row
        return render_template("question.html", question=row["question"], answers=dict(zip(range(1, len(row["answers"].split(';'))+1), row["answers"].split(';')))) # Render question template
    
    id, choice = session.get("id"), request.form.get("choice") # Get form params
    if empty(id) or empty(choice): return redirect("/question") # Check that choice and id exist, therefore also proving subj exists
    
    try: choice = int(choice) # If choice not int...
    except: return redirect("/question") # ...redirect to question
    
    row = db.execute("SELECT ansNo, answers, reason FROM {0} WHERE id = ?".format(session["subj"]), id)[0] # 
    (answer, answers, reason) = (row["ansNo"], row["answers"], row["reason"])
    
    if answer == choice: flash("Correct!", "good")
    else:
        flashMsg = "Incorrect, the answer was {0}.".format(answers.split(';')[answer-1])
        flash(flashMsg if reason == None else "{0} {1}".format(flashMsg, reason), "bad")
    
    return redirect("/question")

app.run(host="0.0.0.0", port=8080)