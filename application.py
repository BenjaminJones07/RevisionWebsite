#Imports
from flask import Flask, render_template, request, session, flash, redirect
from Tools.subjects import SUBJECTS as loadSubj
#from Tools.subjects import TOPICS as loadTopic
from flask_session import Session
from cs50 import SQL
import random

# Config
app, db, SUBJECTS = Flask(__name__), SQL("sqlite:///revWeb.db"), loadSubj().getSubjectsArr()

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["TEMPLATES_AUTO_RELOAD"] = True
Session(app)

# Helpers
empty = lambda x: x == "" or not x # Return True if variable is empty
subjSet = lambda : SUBJECTS if not session.get("subjects") else session["subjects"] # If session subjects empty, set to default (all subjects)

# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    session["subjects"] = subjSet()
    if request.method == "GET": return render_template("index.html", subj=SUBJECTS) # Render index page
    session["subjects"] = list(dict.fromkeys([x for x in request.form.getlist("subjects") if x in SUBJECTS])) # Remove duplicates and set session
    return redirect("/")

@app.route("/question", methods=["GET", "POST"])
def question():
    session["subjects"] = subjSet()
    if request.method == "GET":
        session["subj"] = random.choice([subj for subj in session["subjects"]]) # Select random subject
        
        max = db.execute("SELECT MAX(id) FROM {0}".format(session["subj"]))[0]['MAX(id)'] # Get max ID
        session["id"] = random.choice([x for x in range(1, max+1) if x != session.get("id")]) # Get ID in range not equal to previous ID
        
        row = db.execute("SELECT id, question, answers FROM {0} WHERE id = ?".format(session["subj"]), session["id"])[0] # Get the random row
        
        return render_template("question.html", question=row["question"], answers=dict(zip(range(1, len(row["answers"].split(';'))+1), row["answers"].split(';')))) # Render question template
    
    id, choice = session.get("id"), request.form.get("choice") # Get form params
    if empty(id) or empty(choice): return redirect("/question") # Check that choice and id exist, therefore also proving subj exists
    
    try: choice = int(choice) # If choice not int...
    except: return redirect("/question") # ...redirect to question
    
    row = db.execute("SELECT ansNo, answers, reason FROM {0} WHERE id = ?".format(session["subj"]), id)[0] # Get question row
    
    flashMsg, cat = ("Correct!", "good") if row["ansNo"] == choice else ("Incorrect, the answer was '{0}'.".format(row["answers"].split(';')[row["ansNo"]-1]), "bad") # Correct or incorrect
    flash(flashMsg if row["reason"] == None else "{0} {1}".format(flashMsg, row["reason"]), cat) # Flash message
    
    return redirect("/question") # Get new question

app.run(host="0.0.0.0", port=8080)