from Tools.subjects import SUBJECTS as loadSubj
from cs50 import SQL

db, SUBJECTS = SQL("sqlite:///revWeb.db"), loadSubj()
