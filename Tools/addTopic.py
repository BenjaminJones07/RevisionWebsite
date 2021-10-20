from subjects import SUBJECTS as loadSubj
from cs50 import SQL

db, SUBJECTS = SQL("sqlite:///revWeb.db"), loadSubj()

print("Existing topics:")
[print("\t- {0}".format(i.title())) for i in SUBJECTS.getSubjectsArr()]
subjName = input("New subject name: ").strip().lower()
if SUBJECTS.inSubjects(subjName):
    print("Subject already exists")
    exit()

db.execute("CREATE TABLE {0} (id INTEGER, question TEXT, answers TEXT, ansNo INTEGER, reason TEXT, PRIMARY KEY (id));".format(subjName))
SUBJECTS.addSubject(subjName)
print("Subject added!")