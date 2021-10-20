class SUBJECTS():
    def __init__(self, subj="subjects.txt", topic="topics.txt", folder="config"):
            self.files = ["{0}/{1}".format(folder, x) for x in [subj, topic]]
            self.subjects, self.topics = [[x.strip() for x in open(FILE).readlines() if x.strip() != "buffer"] for FILE in self.files]
            self.topics = [tuple(x.split(';')) for x in self.topics]

    add = lambda subject, file: open(file, "a").write("\n{0}".format(subject))
    addSubj = lambda self, subject: add(subject, self.files[0])
    addTopic = lambda self, topic: add(topic, self.files[1])
    getSubjectsArr = lambda self: self.subjects
    getTopicsArr = lambda self: self.topics
    inSubjects = lambda self, subject: subject in self.subjects
    inTopics = lambda self, topic: topic in self.topics

test = SUBJECTS()
print(test.getTopicsArr())