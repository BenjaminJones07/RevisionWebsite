from subjects import subjAndTopicListInput
from cs50 import SQL

db, (subj, topic), title, lines = SQL("sqlite:///revWeb.db"), subjAndTopicListInput(), input("Title: "), []
print("Fact file content (blank to exit):")
while (x := input().strip()): lines.append(x)
db.execute("INSERT INTO factfiles (subj, topic, title, content) VALUES (?, ?, ?, ?)", subj, topic, title[0].capitalize() + title[1:], '<br>'.join(lines))
