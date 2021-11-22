from cs50 import SQL
import os

database = input("Database file: ")
if not os.path.isfile(database):
    open(database, "w").close()
db = SQL("sqlite:///{0}".format(database))

while True:
    cmd = input("{0}> ".format(database))
    if cmd[0] == "&": continue
    try:
        print(db.execute(cmd))
    except Exception as e:
        print(e)
    open("sql_log.txt", "a").write(cmd + "\n")