from cs50 import SQL

db = SQL("sqlite:///revision.db")

print("Question:")
q = input()
print("No. of answers:")
n = int(input())
answers = ""
for x in range(n):
	print("Answer " + str(x + 1) + ":")
	answers = answers + str(x + 1) + ") " + input() + "#"
	print()
answers = answers[:-1]
print("Correct number:")
a = input()
db.execute("INSERT INTO revision (question, answers, answer, ans, author) VALUES (?, ?, ?, ?, ?)", q, answers, a, n, "Benjamin Jones")
print("Question added!")
