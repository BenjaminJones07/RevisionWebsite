from subjects import subjAndTopicListInput
from cs50 import SQL
import myMarkdown, os

db, files = SQL("sqlite:///revWeb.db"), [x.replace('.md', '') for x in os.listdir("factFiles")]
for f in files:
    _, content = print("Converting {0}:".format(f)), myMarkdown.markdown("{0}\n".format(open("factFiles/{0}.md".format(f), encoding="utf-8").read()))
    if len(db.execute("SELECT subj, topic, title FROM factfiles WHERE filename = ?", f)) != 1: db.execute("INSERT INTO factfiles (subj, topic, title, filename, content) VALUES (?, ?, ?, ?, ?)", *subjAndTopicListInput(), input("Title for {0}: ".format(f)), f, content)
    else: (db.execute("UPDATE factfiles SET content = ? WHERE filename = ?", content, f), print("HTML Entry Refreshed\n"))
    
print("All entries converted")