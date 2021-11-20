from flask import flash, redirect
questionTypes = ["Multiple Choice", "Open Answer"]

# Answer verification
def multiChoice(row, choice):
    try: choice = int(choice)
    except:
        flash("NaN", "warn")
        return redirect("/question")
    return row["ansNo"] == choice

openAnswer = lambda row, choice: row["answers"].split(';')[0] == choice

questionFuncts = [multiChoice, openAnswer]

# Answer Formating
multiChoiceAns = lambda row: "\'" + row["answers"].split(';')[row["ansNo"]-1] +"\'"
openAnswerAns = lambda row: ''.join(row["answers"].split(';'))

answerFuncts = [multiChoiceAns, openAnswerAns]

def typeListInput(): # List question types and get user input
    (print("Question types:"), [print("\t{0} ) {1}".format(str(x+1), questionTypes[x].title())) for x in range(len(questionTypes))])
    return ((x := int(input("Question type number: "))-1), questionTypes[x])

