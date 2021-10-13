from flask import Flask, render_template, request, session
from flask_session import Session
from cs50 import SQL
import random

app = Flask(__name__)
db = SQL("sqlite:///revWeb.db")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/question", methods=["GET", "POST"])
def question():
    if request.method == "GET":
        max = db.execute("SELECT MAX(id) FROM questions")[0]["MAX(id)"] # Get max ID
        id = random.choice([x for x in range(1, max+1) if x != session.get("id")]) # Get ID in range not equal to previous ID
        return render_template("question.html", **db.execute("SELECT id, question, answers FROM questions WHERE id = ?", id)[0]) 
    return "haha post go brrr"

app.run(host="0.0.0.0", port=8080)