from subjects import SUBJECTS as loadSubj
from json import loads
from cs50 import SQL

SUBJECTS = loadSubj()
sArr = SUBJECTS.getSubjectsArr()

# Subjects and Topics list
print("Existing Subjects and topics:")
[[print("\t{0} - {1}".format(s.title(), t.title())) for t in SUBJECTS.getSubjTopicArr(s)]for s in sArr]

# Subjects and IDs
print("Existing Subjects:")
[print("\t {0}) {1}".format(i+1, sArr[i].title())) for i in range(len(sArr))]

# Error Checking
try: subjId = int(input("Topic's subject: "))
except: (print("Not a number"), exit())
if not subjId-1 < len(sArr) or subjId-1 < 0: (print("Index not in range"), exit())

# Get name and check not exists
topicName = input("New topic name: ").strip().lower()
if SUBJECTS.isTopicInSubjects(topicName, sArr[subjId-1]): (print("Subject already exists"), exit())

# Add name
SUBJECTS.addTopic(topicName, sArr[subjId-1])
print("Topic added!")