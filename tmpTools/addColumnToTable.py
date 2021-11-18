from cs50 import SQL

db = SQL("sqlite:///revWeb.db")

rows = [x for x in db.execute("SELECT * FROM questions;")]
print(rows)

db.execute("DROP TABLE questions")
db.execute("CREATE TABLE questions (id INTEGER, question TEXT, answers TEXT, ansNo INTEGER, reason TEXT, subj TEXT, topic TEXT, type INTEGER, PRIMARY KEY (id));")

[db.execute("INSERT INTO questions (id, question, answers, ansNo, reason, subj, topic, type) VALUES (:id, :question, :answers, :ansNo, :reason, :subj, :topic, :type)", type=1, **x) for x in rows]