from subjects import SUBJECTS, subjAndTopicListInput
from questions import answerFuncts, questionTypes
from sqlNone import SQLWrapper
from sys import argv

DEV_MODE = False
PRINT_ALL = False

db = SQLWrapper("sqlite:///revWeb.db")
if not PRINT_ALL:
    match len(argv):
        case 1:
            (subj, topic) = subjAndTopicListInput()
        case 3:
            subjObj = SUBJECTS()
            subj = subjObj.getSubjectsArr()[int(argv[1]) - 1]
            topic = subjObj.getSubjTopicArr(subj)[int(argv[2]) - 1]
        case _:
            print("Usage: showQuestions.py [Subject ID] [Topic ID]")
            exit(1)

if PRINT_ALL:
    [print("{id}: {question} :: {answers} :: {ansNo} :: {reason} :: {typeF}".format(typeF=questionTypes[row["type"]], **row)) for row in db.execute("SELECT * FROM questions")]
else:
    print(f"{subj.title()} ({topic.title()}) questions:")

    if DEV_MODE: [print("{id}: {question} :: {answers} :: {ansNo} :: {reason} :: {typeF}".format(typeF=questionTypes[row["type"]], **row)) for row in db.execute("SELECT * FROM questions WHERE topic = ?", topic)]
    else: [print(f"{row['id']}: {row['question']} => {answerFuncts[row['type']](row).strip(chr(39))}") for row in db.execute("SELECT * FROM questions WHERE topic = ?", topic)]