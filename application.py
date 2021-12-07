# Imports
from flask import Flask, render_template, request, session, flash, redirect
from Tools.questions import questionFuncts as qF, answerFuncts as aF
from Tools.subjects import SUBJECTS as loadSubj
from flask_session import Session
from functools import wraps
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

def clearFlash(func):
    @wraps(func)
    def deco(*args, **kwargs):
        session.pop('_flashes', None)
        return func(*args, **kwargs)
    return deco

# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    session["topics"] = session.get("topics", TOPICS)
    if request.method == "GET": return render_template("index.html", subj=subjObj.getRawTopicsArr()) # Render index page
    session["topics"] = list(dict.fromkeys([x for x in request.form.getlist("topics") if x in TOPICS])) # Remove duplicates and set session
    return redirect("/")

@app.route("/factSearch")
@clearFlash
def factsearch(): # Browse fact files
    if not (x := request.args.get("topic")) or x not in subjObj.getFTopicsArr(): return render_template("factSearch1.html", subj=subjObj.getRawTopicsArr())
    return render_template("factSearch2.html", topic=x, files=db.execute("SELECT * FROM factfiles WHERE topic = ?", x))

@app.route("/factFile")
@clearFlash
def factfile(): # Display fact file
    if not (id := request.args.get("id")) or not isinstance(id, int): return redirect("/factSearch") # Check if id exists
    if len(rows := db.execute("SELECT * FROM factfiles WHERE id = ?", int(id))) != 1: return "Bad ID" # Check if id exists
    return render_template("factfile.html", **rows[0])

@app.route("/question", methods=["GET", "POST"])
def question():
    if request.method == "GET":
        print(session.get("topics", TOPICS)) # Error Tanzania (Implement ACTUAL FIX, DONT JUST FIX THIS OCCURANCE!!!)
        print(session.get("id", 0))
        row = random.choice(db.execute("SELECT id, question, answers, subj, type FROM questions WHERE topic = ? AND id != ?", random.choice(session.get("topics", TOPICS)), session.get("id", 0))) # Get random row
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)