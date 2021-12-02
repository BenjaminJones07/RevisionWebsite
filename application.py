# Imports
from flask import Flask, render_template, request, session, flash, redirect
from Tools.subjects import SUBJECTS as loadSubj
from Tools.questions import questionFuncts as qF, answerFuncts as aF
from flask_session import Session
from cs50 import SQL
import random

# Config
subjObj = loadSubj()
app, db, TOPICS = Flask(__name__), SQL("sqlite:///revWeb.db"), subjObj.getFTopicsArr()

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["TEMPLATES_AUTO_RELOAD"] = True
Session(app)

# Helpers
empty = lambda x: x == "" or not x # Return True if variable is empty
topicSet = lambda : TOPICS if not session.get("topics") else session["topics"] # If session topics empty, set to default (all topics)

# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    session["topics"] = topicSet()
    if request.method == "GET": return render_template("index.html", subj=subjObj.getRawTopicsArr()) # Render index page
    session["topics"] = list(dict.fromkeys([x for x in request.form.getlist("topics") if x in TOPICS])) # Remove duplicates and set session
    return redirect("/")

@app.route("/factSearch")
def factsearch():
    return "nice"

@app.route("/factFile")
def factfile():
    if not (id := request.args.get("id")): return redirect("/factSearch")
    if id < int(db.execute("SELECT MAX(id) FROM facts;")[0]): return "Bad ID"
    return "Nice"

@app.route("/question", methods=["GET", "POST"])
def question():
    session["topics"] = topicSet()
    if request.method == "GET":
        row = random.choice(db.execute("SELECT id, question, answers, subj, type FROM questions WHERE topic = ? AND id != ?", random.choice(session["topics"]), session.get("id", 0))) # Get random row
        session["id"], session["subject"] = row["id"], row["subj"]
        
        if row["type"] == 0: return render_template("multichoice.html", question=row["question"], answers=dict(zip(range(1, len(row["answers"].split(';'))+1), row["answers"].split(';')))) # Render question template
        if row["type"] == 1: return render_template("openanswer.html", question=row["question"], postlude=row["answers"].split(';')[1])

    if empty(id := session.get("id")) or empty(choice := request.form.get("choice")): # Check that choice and id exist, therefore also proving subj exists
        flash("No answer supplied", "warn")
        return redirect("/question")
    
    row = db.execute("SELECT ansNo, answers, reason, type FROM questions WHERE id = ?", id)[0] # Get question row

    flashMsg, cat = ("Correct!", "good") if qF[row["type"]](row, choice) else ("Incorrect, the answer was {0}.".format(aF[row["type"]](row)), "bad") # Correct or incorrect
    flash(flashMsg if row["reason"] == None else "{0} {1}".format(flashMsg, row["reason"]), cat) # Flash message
    
    return redirect("/question") # Get new question

app.run(host="0.0.0.0", port=8080)