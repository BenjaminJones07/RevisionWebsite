from subjects import SUBJECTS as loadSubj

SUBJECTS = loadSubj()

print("Existing subjects:")
[print("\t- {0}".format(i.title())) for i in SUBJECTS.getSubjectsArr()]
subjName = input("New subject name: ").strip().lower()
if SUBJECTS.inSubjects(subjName):
    print("Subject already exists")
    exit()

SUBJECTS.addSubj(subjName)
print("Subject added!")