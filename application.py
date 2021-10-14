from flask import Flask, render_template, request, session, flash
from flask_session import Session
from cs50 import SQL
import random

from werkzeug.utils import redirect

app = Flask(__name__)
db = SQL("sqlite:///revWeb.db")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

empty = lambda x: x == "" or not x

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/question", methods=["GET", "POST"])
def question():
    if request.method == "GET":
        max = db.execute("SELECT MAX(id) FROM questions")[0]["MAX(id)"] # Get max ID
        session["id"] = random.choice([x for x in range(1, max+1) if x != session.get("id")]) # Get ID in range not equal to previous ID
        row = db.execute("SELECT id, question, answers FROM questions WHERE id = ?", session["id"])[0] # Get the random row
        answersList = row["answers"].split(';')
        return render_template("question.html", question=row["question"], answers=dict(zip(range(1, len(answersList)+1), answersList)))
    
    id, choice = session.get("id"), request.form.get("choice")
    if empty(id) or empty(choice): return redirect("/question")
    
    try: choice = int(choice)
    except: return redirect("/question")
    
    answer = db.execute("SELECT ansNo FROM questions WHERE id = ?", id)[0]["ansNo"]
    if answer == choice:
        flash("Correct!", "good")
        return redirect("/question")
    
    
    flash("Incorrect, the answer was {0}".format())

app.run(host="0.0.0.0", port=8080)