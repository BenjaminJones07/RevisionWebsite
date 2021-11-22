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
            if topic in self.getSubjTopicArr(x):
                return x
        return None

    # In methods
    isTopicInSubjects = lambda self, topic, subjects: True in [(topic in self.data["topics"].get(x, [])) for x in subjects]
    inSubjects = lambda self, subject: subject in self.data["subjects"]
    inTopics = lambda self, topic: topic in sum([self.getSubjTopicArr(x) for x in self.getSubjectsArr()], [])

    # Add methods
    def addSubj(self, subject):
        if not self.inSubjects(subject):
            self.data["subjects"].append(subject)
            self.data["topics"][subject] = []
            self.save()
        else: print("Subject already exists")

    addTopic = lambda self, topic, subject: (self.data["topics"][subject].append(topic), self.save()) if self.inSubjects(subject) else print("Subject does not exist")
            
def subjectsListInput(subjObj=SUBJECTS()): # List subjects and get user input
    subjs = subjObj.getSubjectsArr()
    print("Subjects:")
    [print("\t{0} ) {1}".format(str(x+1), subjs[x].title())) for x in range(len(subjs))]
    return subjs[int(input("Question subject number: "))-1]

def subjAndTopicListInput(subjObj=SUBJECTS()): # List subjects and topics and get user inputs
    subj = subjectsListInput(subjObj)
    topics = subjObj.getSubjTopicArr(subj)
    print("{0} topics:".format(subj.title()))
    [print("\t{0} ) {1}".format(str(x+1), topics[x].title())) for x in range(len(topics))]
    return (subj, topics[int(input("Question topic number: "))-1])
