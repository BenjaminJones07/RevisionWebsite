# Move questions from separate tables into one
from cs50 import SQL

db, S = SQL("sqlite:///revWeb.db"), ["biology", "history", "french"]

for x in S:
    rows = db.execute("SELECT * FROM {0}".format(x))
    for row in rows:
        print("{id}, {x} : {question}".format(x=x, **row))
        row.pop("id")
        topic = input("Topic: ").strip().lower()
        db.execute("INSERT INTO questions (question, answers, ansNo, reason, subj, topic) VALUES (:question, :answers, :ansNo, :reason, :subj, :topic)", **row, subj=x, topic=topic)
    print("{0} done!".format(x.title()))
print("Questions transferred!")