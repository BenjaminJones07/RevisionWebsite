from subjects import SUBJECTS as loadSubj
from cs50 import SQL
import random

db, SUBJECTS = SQL("sqlite:///revWeb.db"), loadSubj()
subj = SUBJECTS.getSubjectsArr()

print("Subjects:")
[print("\t{0} ) {1}".format(str(x+1), subj[x].title())) for x in range(len(subj))]
subj = subj[int(input("Question subject number: "))-1]

print("{0} topics:".format(subj.title()))
[print("\t{0} ) {1}".format(str(x+1), SUBJECTS.getSubjTopicsArr(subj)[x].title())) for x in range(len(SUBJECTS.getSubjTopicsArr(subj)))]

question = input("Question: ")
answers = [input("Incorrect answer " + str(x + 1) + ": ").title() for x in range(int(input("No. of answers: "))-1)]
random.shuffle(answers)
corrAns = input("Correct Answer: ").title()
reason = input("Reason (optional): ")
rand = random.randint(0, len(answers))
answers.insert(rand, corrAns)
db.execute("INSERT INTO {0} (question, answers, ansNo, reason) VALUES (?, ?, ?, ?)".format(subj), question[0].upper() + question[1:], ';'.join(answers), rand+1, reason if reason.replace(" ", "") != "" else None)
print("Question added!")