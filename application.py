#Imports
from flask import Flask, render_template, request, session, flash, redirect
from Tools.subjects import SUBJECTS as loadSubj
from flask_session import Session
from cs50 import SQL
import random

# Config
subjObj = loadSubj()
app, db, SUBJECTS, TOPICS = Flask(__name__), SQL("sqlite:///revWeb.db"), subjObj.getSubjectsArr(), subjObj.getTopicsArr()

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["TEMPLATES_AUTO_RELOAD"] = True
Session(app)

# Helpers
empty = lambda x: x == "" or not x # Return True if variable is empty
#subjSet = lambda : SUBJECTS if not session.get("subjects") else session["subjects"] # If session subjects empty, set to default (all subjects)
topicSet = lambda : TOPICS if not session.get("topics") else session["topics"] # If session topics empty, set to default (all topics)

# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    session["topics"] = topicSet()
    if request.method == "GET": return render_template("index.html", subj=TOPICS) # Render index page
    session["subjects"] = list(dict.fromkeys([x for x in request.form.getlist("subjects") if x in SUBJECTS])) # Remove duplicates and set session
    return redirect("/")

@app.route("/question", methods=["GET", "POST"])
def question():
    session["topics"] = topicSet()
    if request.method == "GET":
        #session["subj"] = random.choice([subj for subj in session["subjects"]]) # Select random subject
        
        #max = db.execute("SELECT MAX(id) FROM {0}".format(session["subj"]))[0]['MAX(id)'] # Get max ID
        #session["id"] = random.choice([x for x in range(1, max+1) if x != session.get("id")]) # Get ID in range not equal to previous ID
        
        row = random.choice(db.execute("SELECT id, question, answers FROM questions WHERE topic = ?", random.choice(session["topics"])))[0] # Get random row
        session["id"] = row["id"]
        
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