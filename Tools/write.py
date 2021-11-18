from subjects import subjAndTopicListInput
from cs50 import SQL
import random

db, (subj, topic) = SQL("sqlite:///revWeb.db"), subjAndTopicListInput()

question = input("Question: ")
answers = [input("Incorrect answer " + str(x + 1) + ": ") for x in range(int(input("No. of answers: "))-1)]
random.shuffle(answers)
corrAns = input("Correct Answer: ")
reason = input("Reason (optional): ")
rand = random.randint(0, len(answers))
answers.insert(rand, corrAns)
db.execute("INSERT INTO questions (question, answers, ansNo, reason, subj, topic, type) VALUES (?, ?, ?, ?, ?, ?, 0)", question[0].upper() + question[1:], ';'.join(answers), rand+1, reason if reason.replace(" ", "") != "" else None, subj, topic)
print("Question added!")