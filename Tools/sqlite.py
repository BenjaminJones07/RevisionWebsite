from sqlNone import SQLWrapper
import os

if not os.path.isfile(database := input("Database file: ")):
    open(database, "w").close()
db = SQLWrapper(f"sqlite:///{database}")

while True:
    if (cmd := input(f"{database}> "))[0] == "&": continue
    try: print(db.execute(cmd))
    except Exception as e: print(e)
    open("sql_log.txt", "a").write(cmd + "\n")