from subjects import subjAndTopicListInput
from cs50 import SQL

db, (subj, topic) = SQL("sqlite:///revWeb.db"), subjAndTopicListInput()
print("{0} ({1}) questions:".format(subj.title(), topic.title()))
[print("{id}: {question} :: {answers} :: {ansNo} :: {reason}".format(**row)) for row in db.execute("SELECT * FROM questions WHERE topic = ?", topic)]

# Old 'Print all' line: [[print("{subj} - {id}: {question} :: {answers} :: {ansNo} :: {reason}".format(**database[x])) for x in range(len(database))] for database in [[dict({"subj": s.title()}, **x) for x in SQL("sqlite:///revWeb.db").execute("SELECT * FROM {0}".format(s))] for s in loadSubj().getSubjectsArr()]]