import json
class SUBJECTS():
    def __init__(self, file="config/data.json"):
            self.file, self.data = file, json.load(open(file))

    save = lambda self: json.dump(self.data, open(self.file, "w"), indent=4)

    # Get methods
    getSubjectsArr = lambda self: self.data["subjects"]
    getRawTopicsArr = lambda self: self.data["topics"]
    getFTopicsArr = lambda self: sum([self.data["topics"][x] for x in self.data["topics"].keys()], []) # Flattened topics array
    getSubjTopicArr = lambda self, subject: self.data["topics"].get(subject)
    def getSubjByTopic(self, topic):
        for x in self.getSubjectsArr():
            if topic in getSubjTopicArr(x):
                return x
        return None

    # In methods
    isTopicInSubjects = lambda self, topic, subjects: True in [topic in self.data["topics"].get(x) for x in subjects]
    inSubjects = lambda self, subject: subject in self.data["subjects"]
    inTopics = lambda self, topic: topic in [self.getSubjTopicArr(x) for x in self.getSubjectsArr()]

    # Add methods
    def addSubj(self, subject):
        if not self.inSubjects(subject):
            self.data["subjects"].append(subject)
            self.data["topics"][subject] = []
            self.save()

    def addTopic (self, topic, subject):
        if self.inSubjects(subject):
            self.data["topics"][subject] = [topic]
            self.save()

"""
test = SUBJECTS()
print(test.getTopicsArr())
print(test.getSubjectsArr())
print(test.getSubjTopicArr("biology"))
print(test.isTopicInSubjects("ww1 causes", ["history", "biology"]))
test.addSubj("test")
print(test.getSubjectsArr())
print(test.getTopicsArr())
"""