from subjects import subjAndTopicListInput
from questions import typeListInput
from sqlNone import SQLWrapper
import random

db, (subj, topic), (qType, _) = SQLWrapper("sqlite:///revWeb.db"), subjAndTopicListInput(), typeListInput()

question = input("Question: ")
if qType == 1:
    answers, space, rand = [input("Correct answer: "), input("Postlude (optional): ")], bool(input("Is the postlude a separate word? (0 or 1) ") != 0), 0
    if space and answers[1]: answers[1] = f" {answers[1]}"
else:
    random.shuffle((answers := [input("Incorrect answer " + str(x + 1) + ": ") for x in range(int(input("No. of answers: "))-1)]))
    answers.insert((rand := random.randint(0, len(answers))), (corrAns := input("Correct Answer: ")))

reason = input("Reason (optional): ")

db.execute("INSERT INTO questions (question, answers, ansNo, reason, subj, topic, type) VALUES (?, ?, ?, ?, ?, ?, ?)", question[0].upper() + question[1:], ';'.join(answers), rand+1, reason if reason.replace(" ", "") != "" else None, subj, topic, qType)
print("Question added!")