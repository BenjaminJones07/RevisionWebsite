import csv

class SUBJECTS():
    def __init__(self, file="subjects.csv"):#
            self.file = file
            self.subjects = [x for x in csv.reader(open(file), delimiter=',')][0]
            self.subjects = [x.strip() for x in self.subjects]

    def addSubject(self, subject):
        open(self.file, "a").write(", {0}".format(subject))

    def getSubjectsArr(self):
        return self.subjects

    def inSubjects(self, subject):
        return subject in self.subjects