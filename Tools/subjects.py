from typing import Dict, List, Optional, Tuple
import json

class SUBJECTS():
    def __init__(self, file: str = "config/data.json") -> None:
        self.file, self.data = file, json.load(open(file))

    def save(self) -> Optional[bool]:
        json.dump(self.data, open(self.file, "w"), indent=4)
        return True

    # Get methods
    def getSubjectsArr(self) -> List[str]:
        return self.data["subjects"]
    
    def getRawTopicsArr(self) -> Dict[str, List[str]]:
        return self.data["topics"]
    
    def getFTopicsArr(self) -> List[str]:
        return sum([self.data["topics"][x] for x in self.data["topics"].keys()], []) # Flattened topics list (List of all topics)
    
    def getSubjTopicArr(self, subject: str) -> List[str]:
        return self.data["topics"].get(subject)
    
    def getSubjByTopic(self, topic: str) -> Optional[List[str]]:
        for x in self.getSubjectsArr():
            if topic in self.getSubjTopicArr(x):
                return x
        return None

    # In methods
    def isTopicInSubjects(self, topic: str, subjects: str) -> bool:
        return True in [(topic in self.data["topics"].get(x, [])) for x in subjects]
    
    def inSubjects(self, subject: str) -> bool:
        return subject in self.data["subjects"]
    
    def inTopics(self, topic: str) -> bool:
        return topic in sum([self.getSubjTopicArr(x) for x in self.getSubjectsArr()], [])

    # Add methods
    def addSubj(self, subject: str) -> bool:
        if not self.inSubjects(subject):
            self.data["subjects"].append(subject)
            self.data["topics"][subject] = []
            return True if self.save() else False
        else:
            return False

    def addTopic(self, topic: str, subject: str) -> bool:
        if not self.inSubjects(subject) or self.isTopicInSubjects(topic, subject):
            return False
        
        self.data["topics"][subject].append(topic)
        return True if self.save() else False
            
def subjectsListInput(subjObj: SUBJECTS = SUBJECTS()) -> str: # List subjects and get user input
    subjs = subjObj.getSubjectsArr()
    print("Subjects:")
    [print(f"\t{x+1} ) {subjs[x].title()}") for x in range(len(subjs))]
    return subjs[int(input("Question subject number: "))-1]

def subjAndTopicListInput(subjObj: SUBJECTS = SUBJECTS()) -> Tuple[str, str]: # List subjects and topics and get user inputs
    subj = subjectsListInput(subjObj)
    topics = subjObj.getSubjTopicArr(subj)
    print(f"{subj.title()} topics:")
    [print(f"\t{x+1} ) {topics[x].title()}") for x in range(len(topics))]
    return (subj, topics[int(input("Question topic number: "))-1])