from subjects import subjAndTopicListInput
from cs50 import SQL

db, (subj, topic) = SQL("sqlite:///revWeb.db"), subjAndTopicListInput()

# Inputs
question = "True or False? {0}".format(input("Statement: "))
isTrue = 1 if (x := input("True or False: ").title()) == "True" else 2
if x not in ["True", "False"]: (print("Answer was not True or False"), quit())
reason = input("Reason (optional): ")

# Database write
db.execute("INSERT INTO questions (question, answers, ansNo, reason, subj, topic, type) VALUES (?, 'True;False', ?, ?, ?, ?, 0)", question[0].upper() + question[1:], isTrue, reason if reason.replace(" ", "") != "" else None, subj, topic)
print("Question added!")