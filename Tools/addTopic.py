from json import loads
from subjects import SUBJECTS as loadSubj
from cs50 import SQL

SUBJECTS = loadSubj()
sArr = SUBJECTS.getSubjectsArr() # Add this in below!!!

print("Existing Subjects and topics:")
[[print("\t{0} - {1}".format(s.title(), t.title())) for t in SUBJECTS.getSubjTopicArr(s)]for s in SUBJECTS.getSubjectsArr()]
print("Existing Subjects:")
[print("\t {0}) {1}".format(i, SUBJECTS.getSubjects.Arr()[i].title())) for i in range(len(SUBJECTS.getSubjectsArr()))]
try: subjId = int(input("Topic's subject: "))
except: (print("Not a number"), exit())
if not SUBJECTS.inSubjects(SUBJECTS.getSubjectArr()[subjId])
topicName = input("New topic name: ").strip().lower()
if SUBJECTS.isTopicInSubjects(topicName, ):
    print("Subject already exists")
    exit()

SUBJECTS.addTopic(topicName, subjId)
print("Topic added!")