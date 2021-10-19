import csv

class SUBJECTS():
    def __init__(self, file="subjects.csv"):#
            self.file = file
            self.subjects = [x.strip() for x in [x for x in csv.reader(open(file), delimiter=',')][0]]

    def addSubject(self, subject):
        open(self.file, "a").write(", {0}".format(subject))

    def getSubjectsArr(self):
        return self.subjects

    def inSubjects(self, subject):
        return subject in self.subjects