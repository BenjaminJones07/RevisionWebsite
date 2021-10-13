from cs50 import SQL

db = SQL("sqlite:///revWeb.db")

question = input("Question: ").title()
n = int(input("No. of answers: "))
answers = ""
for x in range(n):
	answers = answers + input("Answer " + str(x + 1) + ": ").title() + ";"
answers = answers[:-1]
db.execute("INSERT INTO questions (question, answers, ansNo) VALUES (?, ?, ?)", question[0].upper() + question[1:], answers, input("Correct number: "))
print("Question added!")