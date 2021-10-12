import os
from cs50 import SQL

database = input("Database file: ")
if not os.path.isfile(database):
    open(database, "w").close()
db = SQL("sqlite:///{0}".format(database))

while True:
    cmd = input("{0}> ".format(database))
    try:
        print(db.execute(cmd))
    except Exception as e:
        print(e)
    open("sql_log.txt", "a").write(cmd + "\n")