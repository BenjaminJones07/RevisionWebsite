from cs50 import SQL

db = SQL("sqlite:///revWeb.db")

question = "True or False? {0}".format(input("Statement: "))
isTrue = 1 if input("True or False: ").title() == "True" else 2
reason = input("Reason (optional): ")
db.execute("INSERT INTO questions (question, answers, ansNo, reason) VALUES (?, 'True;False', ?, ?)", question[0].upper() + question[1:], isTrue, reason if reason.replace(" ", "") != "" else None)
print("Question added!")