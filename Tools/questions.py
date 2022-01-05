from typing import Dict, Union, Tuple
from flask import flash

# Multiple Choice
def multiChoice(row: Dict[str, Union[str, int]], choice: int) -> bool:
    try: choice = int(choice)
    except:
        flash("NaN", "warn")
        return False
    return row["ansNo"] == choice

def multiChoiceAns(row: Dict[str, Union[str, int]]) -> str:
    return f"\'{row['answers'].split(';')[row['ansNo']-1]}\'"

# Open Answer

def openAnswer(row: Dict[str, Union[str, int]], choice, int) -> bool:
    return row["answers"].split(';')[0].replace(' ', '').lower() == choice.replace(' ', '').lower()

def openAnswerAns(row: Dict[str, Union[str, int]]) -> str:
    return ''.join(row["answers"].split(';'))

questionTypes = ["Multiple Choice", "Open Answer"]
questionFuncts = [multiChoice, openAnswer]
answerFuncts = [multiChoiceAns, openAnswerAns]

# Input function
def typeListInput() -> Tuple[int, str]: # List question types and get user input
    (print("Question types:"), [print(f"\t{x+1} ) {questionTypes[x].title()}") for x in range(len(questionTypes))])
    return ((x := int(input("Question type number: "))-1), questionTypes[x])
