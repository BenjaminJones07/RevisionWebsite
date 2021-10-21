import json
class SUBJECTS():
    def __init__(self, file="config/data.json"):
            self.file, self.data = file, json.load(open(file))
            self.subjects, self.topics = [self.data[x] for x in self.data.keys()]

    save = lambda self: json.dump(self.data, open(self.file, "w"), indent=4)

    # Get methods
    getSubjectsArr = lambda self: self.subjects
    getTopicsArr = lambda self: self.topics
    getSubjTopicArr = lambda self, subject: self.topics.get(subject)

    # In methods
    isTopicInSubjects = lambda self, topic, subjects: True in [topic in self.topics.get(x) for x in subjects]
    inSubjects = lambda self, subject: subject in self.subjects
    inTopics = lambda self, topic: topic in self.topics

    # Add methods
    def addSubj(self, subject):
        if not self.inSubjects(subject):
            self.data[subject] = []
            self.save()

    def addTopic (self, topic, subject):
        if self.inSubjects(subject):
            self.data[subject] = [topic]
            self.save()

test = SUBJECTS()
print(test.getTopicsArr())
print(test.getSubjectsArr())
print(test.getSubjTopicArr("biology"))
print(test.isTopicInSubjects("ww1 causes", ["history", "biology"]))
test.addSubj("test")
print(test.getTopicsArr())