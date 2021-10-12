from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from cs50 import SQL
import random

app = Flask(__name__)
db = SQL("sqlite:///revision.db")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "GET":
		return render_template("index.html")
	session["mode"] = request.form.get("mode")
	return redirect("/")

@app.route("/question", methods=["GET", "POST"])
def question():
	if request.method == "GET":
		max = db.execute("SELECT MAX(id) AS max FROM revision")[0]["max"]
		id = random.randint(1, max)
		if session.get("id"):
			while session["id"] == id:
				id = random.randint(1, max)
		x = db.execute("SELECT * FROM revision WHERE id = ?", id)[0]
		answers = range(1, x["ans"] + 1)
		question = x["answers"].split("#")
		return render_template("question.html", x=x, answers=answers, q=question)
	id = request.form.get("id")
	if id == None or id == "":
		return redirect("/question")
	session["id"] = id
	ans = request.form.get("answer")
	if ans == None or ans == "":
		return redirect("/question")
	x = db.execute("SELECT * FROM revision WHERE id = ?", id)[0]
	if int(ans) != int(x["answer"]):
		answers = x["answers"].split("#")
		question = x["question"]
		a = int(x["answer"])
		return render_template("wrong.html", q=question, ans=answers, answer=a)
	return render_template("right.html")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
