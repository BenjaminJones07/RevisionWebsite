from subjects import SUBJECTS as loadSubj
from cs50 import SQL

db, SUBJECTS = SQL("sqlite:///revWeb.db"), loadSubj().getSubjectsArr()

print("Subjects:")
[print("\t{0}) {1}".format(str(x+1), SUBJECTS[x].title())) for x in range(len(SUBJECTS))]
subj = SUBJECTS[int(input("Question subject number: "))-1]
question = "True or False? {0}".format(input("Statement: "))
isTrue = 1 if input("True or False: ").title() == "True" else 2
reason = input("Reason (optional): ")
db.execute("INSERT INTO {0} (question, answers, ansNo, reason) VALUES (?, 'True;False', ?, ?)".format(subj), question[0].upper() + question[1:], isTrue, reason if reason.replace(" ", "") != "" else None)
print("Question added!")