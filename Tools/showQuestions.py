from subjects import SUBJECTS as loadSubj
from cs50 import SQL
[[print("{subj} - {id}: {question} :: {answers} :: {ansNo} :: {reason}".format(**database[x])) for x in range(len(database))] for database in [[dict({"subj": s.title()}, **x) for x in SQL("sqlite:///revWeb.db").execute("SELECT * FROM {0}".format(s))] for s in loadSubj().getSubjectsArr()]]