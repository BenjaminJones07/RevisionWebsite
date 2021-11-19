from subjects import subjAndTopicListInput, typeListInput
from cs50 import SQL
import random

db, (subj, topic), (qType, _)  = SQL("sqlite:///revWeb.db"), subjAndTopicListInput(), typeListInput()

question = input("Question: ")
if qType == 1: answers = ';'.join([input("Correct answer: "), input("Correct answer: ")])
else:
    random.shuffle((answers := [input("Incorrect answer " + str(x + 1) + ": ") for x in range(int(input("No. of answers: "))-1)]))
    answers.insert((rand := random.randint(0, len(answers))), (corrAns := input("Correct Answer: ")))

reason = input("Reason (optional): ")
db.execute("INSERT INTO questions (question, answers, ansNo, reason, subj, topic, type) VALUES (?, ?, ?, ?, ?, ?, ?)", question[0].upper() + question[1:], ';'.join(answers), rand+1, reason if reason.replace(" ", "") != "" else None, subj, topic, qType)
print("Question added!")