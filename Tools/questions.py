from flask import flash

# Multiple Choice
def multiChoice(row, choice):
    try: choice = int(choice)
    except:
        flash("NaN", "warn")
        return False
    return row["ansNo"] == choice

multiChoiceAns = lambda row: "\'" + row["answers"].split(';')[row["ansNo"]-1] +"\'"

# Open Answer

openAnswer = lambda row, choice: row["answers"].split(';')[0].replace(' ', '') == choice.replace(' ', '')
openAnswerAns = lambda row: ''.join(row["answers"].split(';'))

questionTypes = ["Multiple Choice", "Open Answer"]
questionFuncts = [multiChoice, openAnswer]
answerFuncts = [multiChoiceAns, openAnswerAns]

# Input function
def typeListInput(): # List question types and get user input
    (print("Question types:"), [print("\t{0} ) {1}".format(str(x+1), questionTypes[x].title())) for x in range(len(questionTypes))])
    return ((x := int(input("Question type number: "))-1), questionTypes[x])
